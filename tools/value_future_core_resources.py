#!/usr/bin/env python3
"""Recompute the dated 21-company valuation study. No live prices or trading.

Run: uv run python tools/value_future_core_resources.py
Inputs explicitly distinguish observed quotes from analyst assumptions.
All returns are nominal, before investor taxes/fees, in the quoted currency.
"""
from pathlib import Path
import csv
import json
import math

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'knowledge/_syntheses/data'
STAMP = '2026-11-05'


def present_value(eps1, growth, terminal_pe, payout, discount, years=5):
    dividends = [eps1 * (1 + growth) ** (t - 1) * payout for t in range(1, years + 1)]
    terminal = eps1 * (1 + growth) ** (years - 1) * terminal_pe
    return sum(d / (1 + discount) ** t for t, d in enumerate(dividends, 1)) + terminal / (1 + discount) ** years


def implied_return(price, eps1, growth, terminal_pe, payout, years=5):
    low, high = -.95, 10.0
    for _ in range(150):
        rate = (low + high) / 2
        if present_value(eps1, growth, terminal_pe, payout, rate, years) > price:
            low = rate
        else:
            high = rate
    result = (low + high) / 2
    assert abs(present_value(eps1, growth, terminal_pe, payout, result, years) - price) < 1e-6
    return result


def round_down_price(x):
    step = 10 if x >= 1000 else 5 if x >= 50 else .1 if x >= 10 else .05
    return round(math.floor((x + 1e-9) / step) * step, 2)


def write_csv(path, rows):
    with path.open('w', newline='', encoding='utf-8-sig') as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)


def main():
    data = json.loads((DATA / f'future-core-resources-valuation-inputs-{STAMP}.json').read_text())
    assert len(data['rows']) == 21
    results = []
    for row in data['rows']:
        quote = row['quote']
        assert quote['date'] == data['price_date']
        conversion = row['quote_per_eps_currency']
        eps = row['eps1'] * conversion
        price = quote['price']
        values = {}
        for scenario in ('bear', 'base', 'bull'):
            prefix = '' if scenario == 'base' else scenario + '_'
            e, g, pe = (row[prefix + k] for k in ('eps1', 'growth', 'terminal_pe'))
            values[scenario] = present_value(e * conversion, g, pe, row['payout'], row['required_return'])
        assert values['bear'] < values['base'] < values['bull']
        value = values['base']
        irr = implied_return(price, eps, row['growth'], row['terminal_pe'], row['payout'])
        low = round_down_price(value * (1 - row['safety_max']))
        high = round_down_price(value * (1 - row['safety_min']))
        assert 0 < low < high < value
        result = dict(name=row['name'], ticker=row['ticker'], currency=quote['currency'], price_date=quote['date'], price=price,
                      eps1_model=round(eps, 6), eps1_reporting_currency=row['eps_currency'], eps1_before_fx=row['eps1'],
                      forward_normalized_pe=round(price / eps, 2), growth_bear=row['bear_growth'], growth_base=row['growth'], growth_bull=row['bull_growth'],
                      eps_year3=round(eps * (1 + row['growth']) ** 2, 6), eps_year5=round(eps * (1 + row['growth']) ** 4, 6),
                      terminal_pe=row['terminal_pe'], discount_rate=row['required_return'], payout_model=row['payout'],
                      value_bear=round(values['bear'], 4), value_base=round(value, 4), value_bull=round(values['bull'], 4),
                      margin_of_safety=round(1 - price / value, 6),
                      irr_base_3yr=round(implied_return(price, eps, row['growth'], row['terminal_pe'], row['payout'], 3), 6),
                      irr_base_5yr=round(irr, 6), excess_return_vs_hurdle=round(irr - row['required_return'], 6),
                      irr_bear_5yr=round(implied_return(price, row['bear_eps1'] * conversion, row['bear_growth'], row['bear_terminal_pe'], row['payout']), 6),
                      buy_low=low, buy_high=high, drop_to_buy_high=round(high / price - 1, 6),
                      base_dividend_yield=round(eps * row['payout'] / price, 6),
                      irr_at_buy_high=round(implied_return(high, eps, row['growth'], row['terminal_pe'], row['payout']), 6),
                      status='进入或低于模型买入区间' if price <= high else '等待价格',
                      price_source_id=quote['source_id'], price_source_url=quote['url'], financial_sources=row['financial_sources'])
        results.append(result)
    results.sort(key=lambda x: x['excess_return_vs_hurdle'], reverse=True)
    for rank, row in enumerate(results, 1):
        row['rank'] = rank
        row['top10'] = rank <= 10
    write_csv(DATA / f'future-core-resources-valuation-{STAMP}.csv', results)
    write_csv(DATA / f'future-core-resources-top10-{STAMP}.csv', results[:10])
    financial_fields = ('name', 'ticker', 'financial_period', 'financial_fact', 'cashflow_check', 'balance_check', 'eps_bridge', 'growth_and_multiple_reason', 'falsification', 'monitor', 'financial_sources')
    write_csv(DATA / f'future-core-resources-financial-model-bridge-{STAMP}.csv', [{k: r[k] for k in financial_fields} for r in data['rows']])
    # Same economic per-share rights; no unexplained premium assigned to A shares.
    counterparts = {'1816.HK': ('003816.SZ', 4.69), '0883.HK': ('600938.SH', 33.15), '1088.HK': ('601088.SH', 50.98), '2899.HK': ('601899.SH', 29.25)}
    ah = []
    fx = data['fx']['CNYHKD']
    for h in results:
        if h['ticker'] not in counterparts:
            continue
        a, price_a = counterparts[h['ticker']]
        assert h['eps1_reporting_currency'] == 'CNY'
        ah.append(dict(name=h['name'], h_ticker=h['ticker'], h_price_hkd=h['price'], a_ticker=a, a_price_cny=price_a,
                       cny_to_hkd=fx, h_price_cny=round(h['price']/fx, 4), a_premium=round(price_a/(h['price']/fx)-1, 6),
                       h_buy_low=h['buy_low'], h_buy_high=h['buy_high'],
                       a_buy_low=round_down_price(h['value_base']/fx*(1-next(x for x in data['rows'] if x['ticker']==h['ticker'])['safety_max'])),
                       a_buy_high=round_down_price(h['value_base']/fx*(1-next(x for x in data['rows'] if x['ticker']==h['ticker'])['safety_min'])),
                       tax_basis='pre-tax; dividend withholding/FX/fees depend on access route; not an arbitrage'))
    write_csv(DATA / f'future-core-resources-ah-comparison-{STAMP}.csv', ah)
    sensitive=[]
    for row in data['rows']:
        if row['ticker'] not in ('0700.HK','NVDA','TSM','0883.HK'):
            continue
        for dg in (-.05,0,.05):
            for dr in (-.02,0,.02):
                sensitive.append(dict(ticker=row['ticker'], growth=row['growth']+dg, discount_rate=row['required_return']+dr,
                                      value=round(present_value(row['eps1']*row['quote_per_eps_currency'], row['growth']+dg,row['terminal_pe'],row['payout'],row['required_return']+dr),4)))
    write_csv(DATA / f'future-core-resources-sensitivity-{STAMP}.csv', sensitive)
    for r in results:
        print(f"{r['rank']:2} {r['name']:16} {r['price']:8.2f} PE {r['forward_normalized_pe']:5.1f} value {r['value_base']:8.2f} buy {r['buy_low']:7.2f}–{r['buy_high']:7.2f} IRR {r['irr_base_5yr']:.1%} hurdle {r['discount_rate']:.1%} bear {r['value_bear']:.1f}")


if __name__ == '__main__':
    main()
