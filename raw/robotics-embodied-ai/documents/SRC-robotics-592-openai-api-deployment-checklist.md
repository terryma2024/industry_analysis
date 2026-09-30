---
source_id: "SRC-robotics-592"
title: "OpenAI API deployment checklist"
source_type: "technical_documentation"
publisher: "OpenAI"
source_date: "2026-09-30"
url: "https://developers.openai.com/api/docs/guides/deployment-checklist"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-09-30T02:01:13+00:00"
tags:
  - raw/source
  - source-type/technical-documentation
  - evidence/s
aliases:
  - SRC-robotics-592
---
# OpenAI API deployment checklist

| Contents | Expected impact |
| --- | --- |
| [Use the Responses API](#use-the-responses-api) | Quality, cost, latency, reliability |
| [Choose a model for the workload](#choose-a-model-for-the-workload) | Quality, cost, latency |
| [Set up `reasoning.effort`](#set-up-reasoningeffort) | Quality, cost, latency |
| [Change reasoning effort mid-conversation](#change-reasoning-effort-mid-conversation) | Quality, cost, latency |
| [Set up `text.verbosity`](#set-up-textverbosity) | Quality, cost, latency |
| [Set up the assistant `phase` parameter](#set-up-the-assistant-phase-parameter) | Quality, cost |
| [Use `tool_search`](#use-toolsearch) | Cost, latency |
| [Use Programmatic Tool Calling](#use-programmatic-tool-calling) | Quality, cost, latency |
| [Use Multi-agent for parallel work](#use-multi-agent-for-parallel-work) | Quality, cost, latency |
| [Use async tool calling](#use-async-tool-calling) | Latency |
| [Leverage built-in tools](#leverage-built-in-tools) | Quality |
| [Leverage compaction](#leverage-compaction) | Cost |
| [Optimize prompt caching](#optimize-prompt-caching) | Latency, cost |
| [Use `reasoning.encrypted_content`](#use-reasoningencryptedcontent) | Quality, latency |
| [Set image detail intentionally](#set-image-detail-intentionally) | Quality, cost, latency |
| [Send a safety identifier](#send-a-safety-identifier) | Safety, reliability |
| [Handle misalignment monitoring](#handle-misalignment-monitoring) | Safety, reliability |
| [Handle rapid traffic increases and model overload](#handle-rapid-traffic-increases-and-model-overload) | Reliability |
| [Use `background=True`](#use-backgroundtrue) | Task continuity |
| [Use WebSocket mode](#use-websocket-mode) | Latency |
| [Use mid-turn steering](#use-mid-turn-steering) | Quality |

## Use the Responses API

**Always start** with the [Responses API](https://developers.openai.com/api/docs/guides/migrate-to-responses). It is OpenAI’s flagship API and the best place to access the newest model behavior, built-in tools, stateful workflows, and agent features.

## Choose a model for the workload

Evaluate the [GPT-6 model family](https://developers.openai.com/api/docs/guides/latest-model?model=gpt-6-astra) for your workload. Use [`gpt-6-astra`](https://developers.openai.com/api/docs/models/gpt-6-astra) for the highest capability, [`gpt-6.1-sol`](https://developers.openai.com/api/docs/models/gpt-6.1-sol) for complex coding and professional work at a lower cost than Astra, and [`gpt-6-luna`](https://developers.openai.com/api/docs/models/gpt-6-luna) for efficient, repeatable work. Choose the model that performs well on representative tasks rather than routing every request to the most capable model.

When migrating to GPT-6, preserve your current model’s workload role and effective reasoning effort where supported. Use the Responses API for reasoning with tools. GPT-6 Astra and [GPT-6.1 Sol](https://developers.openai.com/api/docs/guides/latest-model?model=gpt-6-astra#gpt-61-sol) require Responses for tool calling; GPT-6 Sol and GPT-6 Luna support function calling in Chat Completions only with `reasoning_effort: "none"`. When reasoning effort is not `none`, remove `temperature`, `top_p`, and `top_logprobs`; also remove `logprobs` from Chat Completions requests and `message.output_text.logprobs` from the Responses `include` array. Check [data residency eligibility](https://developers.openai.com/api/docs/guides/your-data#which-models-and-features-are-eligible-for-data-residency) before selecting a model or processing tier. See the [model migration guidance](https://developers.openai.com/api/docs/guides/latest-model?model=gpt-6-astra#migration-quickstart) for other compatibility checks. Run representative evals before changing prompts or adding new capabilities. Compare task success, latency, input, output, reasoning, and cache-write tokens, and cost per successful task.

## Set up reasoning.effort

Use `reasoning.effort` to decide how much thinking the model should do before it answers.

GPT-6 Astra, GPT-6.1 Sol, GPT-6 Sol, and GPT-6 Luna support `low`, `medium`, `high`, `xhigh`, and `max`. GPT-6 Sol and GPT-6 Luna also support `none`; GPT-6 Astra and GPT-6.1 Sol do not. Lower effort is faster and uses fewer reasoning tokens. Higher effort gives the model more time for planning, debugging, synthesis, and multi-step tradeoffs.

Use `low` when the job is mostly extraction, routing, classification, or a routine rewrite. Use `medium` or `high` when the model needs to diagnose a problem, compare options, write a plan, or reason through code. Use `xhigh` or `max` only when representative evals show that the quality gain justifies the extra latency and cost. When migrating from `minimal`, or from `none` to GPT-6 Astra or GPT-6.1 Sol, start with `low` and compare results. Otherwise, preserve your current effective effort and test changes against your quality, latency, and cost targets.

For the hardest quality-first workloads, also compare [`reasoning.mode: "pro"`](https://developers.openai.com/api/docs/guides/reasoning#reasoning-mode) with standard mode at the same effort. Reasoning mode and effort are independent. Pro mode can improve reliability by applying more model work before returning a single final answer, but it increases latency and token usage.

```python
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
from openai import OpenAI

client = OpenAI()

prompt = """
Our CI job started failing after a dependency bump.

Error:
TypeError: Timeout.__init__() got an unexpected keyword argument 'connect'

Identify the likeliest root cause and the smallest safe fix.
"""

response = client.responses.create(
    model="gpt-6-astra",
    reasoning={"effort": "xhigh", "mode": "pro"},
    input=prompt,
)

print(response.output_text)
```

## Change reasoning effort mid-conversation

For GPT-6 models in standard, single-agent mode, add a [`configuration_update`](https://developers.openai.com/api/docs/guides/reasoning#change-reasoning-mid-conversation) input item before the next user message to change effort between responses. Leave the request-level `reasoning.effort` unchanged so the original prompt prefix remains eligible for caching. The update applies to the next response and continues until another update overrides it. Configuration updates cannot be combined with automatic compaction or truncation, and `/responses/compact` rejects histories containing them. To compact the history, include a `compaction_trigger` item and add a fresh update afterward.

## Set up text.verbosity

`text.verbosity` is the main lever for balancing brevity against completeness. Use lower verbosity when the product needs a quick, compact answer, and higher verbosity when the response needs richer explanation, clearer structure, or complete context. Lower verbosity means fewer output tokens, so the model generates less and returns output faster.

For coding, `medium` and `high` tend to produce longer, more organized output with clearer structure. `low` keeps the answer tighter and more minimal.

When migrating, check whether broad instructions like “Be concise” still help. Prefer `text.verbosity` to control the default level of detail, then use the prompt to specify required content, structure, and length.

Prompts also affect quality, token usage, cost, and latency. Review the [latest-model prompting best practices](https://developers.openai.com/api/docs/guides/latest-model#prompting-best-practices) alongside your verbosity setting, including its testing and verification guidance for coding agents.

```python
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-6-astra",
    text={"verbosity": "low"},
    input="""
    Summarize this incident for the next on-call engineer.
    - checkout latency spiked from 220 ms to 4.8 s
    - only us-east-1 was affected
    - rollback is complete
    - likely trigger: cache stampede after deploy
    """,
)

print(response.output_text)
```

## Set up the assistant phase parameter

`phase` is a label on assistant messages in the conversation history. It indicates to the model whether a prior assistant message was an intermediate working commentary or the final answer. Use `phase: "commentary"` for progress updates, pre-tool-call notes, and other in-between messages. Use `phase: "final_answer"` for the completed response.

The assistant might say something like:

```json
2
3
4
5
{
  "role": "assistant",
  "phase": "commentary",
  "content": "I'm checking the logs and comparing them to the last successful deploy."
}
```

That is not the answer. It is a progress note. Later, the assistant might say:

```json
2
3
4
5
{
  "role": "assistant",
  "phase": "final_answer",
  "content": "The deploy failed because the migration referenced a column that does not exist in production."
}
```

This is useful in long-running or tool-heavy workflows where the assistant may produce visible progress updates before it finishes. When you send that history back on follow-up requests for `gpt-5.3-codex` and later models, **preserve and resend `phase`** on assistant messages so the model can distinguish progress updates from the final result. This helps reduce early stopping, making the agent more likely to continue until it reaches the final answer.

## Use tool\_search

Instead of loading the full tool catalog into every request, use [tool search](https://developers.openai.com/api/docs/guides/tools-tool-search): add `{"type": "tool_search"}` and mark expensive tool definitions with `defer_loading: true`. The model can then load the subset it needs at runtime. At request start, the model only sees the search tool name and description. If the model decides it needs a deferred tool, it runs tool search, and only then are the deferred tool definitions loaded into context. Only then will the model call them. This saves tokens and preserves cache performance.

Tool search has two modes:

- **Hosted tool search** is the simpler option. Use it when you already know which tools could be available for the request.
- **Client-executed tool search** is for cases where your app has to decide what tools are available, like based on the user’s tenant, project, permissions, or internal registry.

**Start with hosted tool search** unless your app really needs to control discovery itself.

Group your tools by user intent. Use a namespace or an MCP server when you can. It is easier for the model to choose between a few clear groups than a long flat list of functions. We recommend keeping each namespace under about 10 functions for optimal token efficiency and model performance.

Keep namespace descriptions short and discriminative. Put the detailed instructions inside the deferred tool definitions. Avoid making one giant namespace for everything.

```python
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
from openai import OpenAI

client = OpenAI()

billing_namespace = {
    "type": "namespace",
    "name": "billing",
    "description": "Billing tools for invoices, payments, taxes, and credits.",
    "tools": [
        {
            "type": "function",
            "name": "lookup_invoice",
            "description": "Look up invoice state, taxes, credits, and payment attempts.",
            "parameters": {
                "type": "object",
                "properties": {
                    "invoice_id": {"type": "string"},
                },
                "required": ["invoice_id"],
                "additionalProperties": False,
            },
            "strict": True,
            "defer_loading": True,
        }
    ],
}

crm_namespace = {
    "type": "namespace",
    "name": "crm",
    "description": "CRM tools for account ownership, plans, health, and payment history.",
    "tools": [
        {
            "type": "function",
            "name": "get_account",
            "description": "Fetch account owner, plan, health, and payment history.",
            "parameters": {
                "type": "object",
                "properties": {
                    "account_id": {"type": "string"},
                },
                "required": ["account_id"],
                "additionalProperties": False,
            },
            "strict": True,
            "defer_loading": True,
        }
    ],
}

response = client.responses.create(
    model="gpt-6-astra",
    input=(
        "Find the right billing tool and explain why invoice INV-1043 still "
        "shows overdue after a payment yesterday."
    ),
    tools=[billing_namespace, crm_namespace, {"type": "tool_search"}],
)

print(response.output)
```

## Use Programmatic Tool Calling

[Programmatic Tool Calling](https://developers.openai.com/api/docs/guides/tools-programmatic-tool-calling) lets supported models write JavaScript that calls eligible tools and reduces their intermediate results inside a hosted runtime. Use it for bounded stages where code can filter, join, rank, remove duplicates, combine, or check large tool results before returning a smaller structured result to the model.

Add the `programmatic_tool_calling` tool and opt in each eligible tool. Use `allowed_callers: ["programmatic"]` for program-only tools, or use `allowed_callers: ["direct", "programmatic"]` when the model may also call the tool directly. Keep calls direct when each result may change the model’s next decision, an action requires approval, or the final answer must preserve citations or native artifacts. Document tool return fields and error behavior so the model can write a correct program without first inspecting a result.

Your tool loop must handle `program` and `program_output` items, as well as program-issued `function_call` items and their `function_call_output` items. Preserve each `call_id`, and copy the function call’s `caller` into its output so the service can resume the correct program.

Test both the `program_output` and the final assistant message. A correct program result can still become an incomplete final answer. Compare task success, required evidence, total tokens, latency, and cost against the same workflow using direct tool calls.

## Use Multi-agent for parallel work

[Multi-agent](https://developers.openai.com/api/docs/guides/responses-multi-agent) lets supported models, including GPT-6 models, delegate independent workstreams to subagents and synthesize their results. Use it when you can split research, analysis, or implementation into concrete, bounded tasks that use separate context and run in parallel.

Set `multi_agent.enabled` to `true` in the request. For HTTP, use the beta Responses SDK with `client.beta.responses` and pass `responses_multi_agent=v1` in `betas`. For raw HTTP or WebSocket connections, send `OpenAI-Beta: responses_multi_agent=v1`. Item schemas can change while Multi-agent is in beta.

Prefer one agent for short tasks, ordered chains where each step depends on the last, or work that writes to the same mutable resource. Subagents can increase token usage, so start with the default `max_concurrent_subagents` value of `3` and measure end-to-end quality, latency, and cost. For tool-heavy or long-running Multi-agent workflows, WebSocket mode can reduce continuation overhead.

Before enabling Multi-agent, account for its current limitations: `/responses/compact`, `reasoning.summary`, and `max_tool_calls` are not supported. The server automatically compacts the root context and every subagent context.

## Use async tool calling

On GPT-6 models, set `async: true` on a function or custom tool when the model can keep working while your application runs it. Start slow tool calls early and let the model handle independent work. Your application still executes and tracks the call, then returns the result in a later Responses request with the original `call_id`. Async execution does not apply to built-in tools or programmatic tool calls. In Multi-agent mode, do not combine async tools with parallel tool calls. See [async tool calling](https://developers.openai.com/api/docs/guides/async-tool-calling) for the full flow.

## Leverage built-in tools

[Built-in tools](https://developers.openai.com/api/docs/guides/tools) are native capabilities of the API. Instead of building every tool yourself, you can give the model access to tools that already work inside the Responses API. The model can then decide when to use them.

OpenAI keeps adding more native tools, so start with built-in tools when they fit your workflow. Build custom tools when native options do not cover the task. Current built-in tools and related tool options include:

- **Web search**: Search the web for up-to-date information
- **File search**: Search uploaded files or vector stores
- **Code interpreter**: Run Python for analysis, math, charts, and file processing
- **Shell**: Run shell commands in a hosted container or your own runtime
- **Computer use**: Operate a UI through screenshots, clicks, typing, and scrolling
- **Image generation**: Generate or edit images
- **MCP/connectors**: Connect the model to external services and tools
- **Skills**: Attach reusable instruction bundles and workflow files
- **Apply patch**: Make structured code edits

Model quality is another reason to prefer them. Built-in tools are in-distribution for our post-training, meaning that the models are trained and evaluated around these tool shapes, behaviors, and outputs. With built-in tools, OpenAI models support better tool selection, cleaner execution, and fewer failures than with new tools.

## Leverage compaction

[Compaction](https://developers.openai.com/api/docs/guides/compaction) is a context engineering tool: it decides what information the model carries forward across many turns. In long-running agents, the problem is not just, “Will I hit the context limit?” It is that old messages, tool logs, retries, and stale details crowd out the state the model needs.

Compaction gives you a controlled way to reduce context size while preserving state needed for subsequent turns. After a meaningful milestone, like finishing a debugging phase or narrowing a root cause, you can compact the prior window and continue from the compacted output. This keeps the model sharp because the next turn is built around the important state, not every intermediate reasoning, failed command, and obsolete branch of reasoning.

You can use compaction in two ways:

- **Let the server handle it**: if you use `previous_response_id`, turn on `context_management` with a `compact_threshold`. The server will automatically compact the conversation when it gets too large. You keep sending only the newest user message.
- **Do it yourself**: if you manage the full input array yourself, call `client.responses.compact()`. It gives back a smaller context window. Use that returned output directly in the next `responses.create()` call.

**Do not edit the compacted output.** It is not a human summary, but the machine state that helps the model continue. Pass it forward as-is, then add the next user message.

```python
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
from openai import OpenAI

client = OpenAI()

# Full window collected from a long debugging session:
# user messages, assistant outputs, tool calls, and tool outputs.
long_window = session_items

compacted = client.responses.compact(
    model="gpt-6-astra",
    input=long_window,
)

next_response = client.responses.create(
    model="gpt-6-astra",
    store=False,
    input=[
        *compacted.output,  # Use compact output as-is.
        {
            "type": "message",
            "role": "user",
            "content": (
                "We found the bad cache invalidation path. Write the fix plan "
                "and the verification checklist."
            ),
        },
    ],
)

print(next_response.output_text)
```

## Optimize prompt caching

[Prompt caching](https://developers.openai.com/api/docs/guides/prompt-caching) automatically reduces latency and cost when requests reuse the same long prefix. Put stable instructions, examples, and reference material first, followed by dynamic user-specific content. Keep tool definitions and ordering stable, and append new conversation turns without rewriting earlier context.

GPT-5.6 introduced explicit prompt caching. Implicit caching remains the default, but GPT-5.6 models and later model families also support explicit cache breakpoints and request-wide cache policy. If a changing suffix comes after a stable prefix, add an explicit `prompt_cache_breakpoint` at the reusable boundary. Set `prompt_cache_options.mode` to `explicit` only when the request should use only the breakpoints you provide and no implicit breakpoint. Earlier models continue to use automatic prompt caching only.

When migrating from GPT-5.5 or earlier, replace `prompt_cache_retention` with `prompt_cache_options.ttl: "30m"`. See the [prompt caching model differences](https://developers.openai.com/api/docs/guides/prompt-caching#summary-of-model-differences) before changing cache settings.

On GPT-5.6 models and later model families, cache writes cost 1.25× the uncached input token rate. Log `cached_tokens` and `cache_write_tokens`, then compare write volume with later cache reads to measure net cost and tune breakpoint placement.

Use a stable `prompt_cache_key` for requests that share a reusable prefix to help route related requests to the same cache and optimize cache hit rates on models before GPT-5.6. For busy groups, follow the [guidance for distributing traffic across more keys](https://developers.openai.com/api/docs/guides/prompt-caching#prompt-cache-keys).

On GPT-5.6 and later, `prompt_cache_key` is optional: you can achieve optimal cache hit rates without it. You can use it to maintain separate cache accounting for customers, users, or workspaces. This can make cached token usage and billing easier to explain for each group. Assign a distinct key to each customer and keep it stable across that customer’s related requests. Separate keys also help prevent cache-hit probing across customers. See [Separate cache accounting with keys](https://developers.openai.com/api/docs/guides/prompt-caching#separate-prompts-with-cache-keys).

```python
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
from openai import OpenAI

client = OpenAI()

instructions = """
You are the support agent for Acme.
Follow the Acme support policy and escalation rubric.
Use the same tone, safety rules, and tool plan for each ticket.
"""

response = client.responses.create(
    model="gpt-6-astra",
    prompt_cache_key="tenant-acme-support-agent",
    instructions=instructions,
    input="Summarize the current escalation for the on-call lead.",
)

print(response.output_text)
```

## Use reasoning.encrypted\_content

Supported models, including GPT-6 models, can [preserve reasoning across calls](https://developers.openai.com/api/docs/guides/reasoning#preserve-reasoning-across-calls). Use `reasoning.context: "all_turns"` when the task’s goals, assumptions, and priorities remain stable. Use `current_turn` when earlier reasoning is no longer relevant and might anchor the model to an outdated approach. If you omit `reasoning.context` or set it to `auto`, inspect the response’s `reasoning.context` field to confirm the effective mode.

[Persisted reasoning](https://developers.openai.com/api/docs/guides/reasoning#keeping-reasoning-items-in-context) works only when earlier reasoning items are available. Use `previous_response_id` for stored responses. If your [Zero Data Retention (ZDR)](https://developers.openai.com/api/docs/guides/your-data#zero-data-retention) requirements do not allow storing response data, encrypted reasoning content enables a stateless handoff.

Reasoning items in the response output include encrypted reasoning content by default. You can access the encrypted reasoning content from each reasoning item’s `encrypted_content` property. Your app does not need to understand that value. It just keeps each reasoning item exactly as returned and sends it back during the next turn, so the model can use it to continue the workflow.

```python
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
from openai import OpenAI

client = OpenAI()

history = [
    {
        "role": "user",
        "content": "Investigate why invoice INV-1043 has mismatched tax totals.",
    }
]

first = client.responses.create(
    model="gpt-6-astra",
    store=False,
    reasoning={"effort": "medium", "context": "current_turn"},
    input=history,
)

history.extend(item.model_dump(exclude={"status"}) for item in first.output)
history.append(
    {
        "role": "user",
        "content": "Now write the customer-facing explanation in plain English.",
    }
)

second = client.responses.create(
    model="gpt-6-astra",
    store=False,
    reasoning={"effort": "medium", "context": "all_turns"},
    input=history,
)

print(second.output_text)
```

## Set image detail intentionally

Image `detail` defaults to `auto`, and its sizing behavior depends on the model. Large images can use more input tokens and add latency. Check the [sizing table for listed models](https://developers.openai.com/api/docs/guides/images-vision#model-sizing-behavior), and measure image token use and limits with your selected model before deployment.

Choose [`detail`](https://developers.openai.com/api/docs/guides/images-vision#choose-an-image-detail-level) for the task. Resize the image, use `low` when fine visual detail is not important, or use `high` for standard high-fidelity image understanding. Use `original` where supported for large, dense, coordinate-sensitive, OCR, localization, or visual-inspection tasks where the extra detail improves quality. Measure worst-case image tokens and latency before deployment.

## Send a safety identifier

If your application serves individual end users, send a stable, privacy-preserving [`safety_identifier`](https://developers.openai.com/api/docs/guides/safety-best-practices#implement-safety-identifiers) with each request. It helps OpenAI detect misuse and gives your team a stable way to trace policy violations. It also reduces the chance that one user’s misuse disrupts access for your broader organization.

Hash the user’s username or email address instead of sending identifying information. For logged-out experiences, use a stable session ID.

## Handle misalignment monitoring

For GPT-6 Astra agent workflows, plan for [misalignment monitoring](https://developers.openai.com/api/docs/guides/safety-checks/misalignment-monitoring). If a request returns `403` with `misalignment_policy_violation`, stop dispatching actions for that conversation and do not automatically retry the blocked workflow. Handle errors during streaming too, and review any actions that may already have run. Subscribe to `safety.alert.created` if your team needs project alerts; the webhook does not replace request error handling. Check the guide for which Responses requests can be stopped automatically.

## Handle rapid traffic increases and model overload

Check the HTTP status and `error.code` before choosing a recovery action. A `429` with `slow_down` means the request rate increased too quickly: follow `Retry-After` when present, reduce traffic, then ramp gradually. A `503` with `server_is_overloaded` means the requested model is temporarily overloaded: follow `Retry-After` when present, then retry. If the header is missing, increase retry delays exponentially with jitter and bound your retries. Billing, spend, and quota errors require action before retrying; do not treat every `429` as a temporary rate limit. See [rate limits](https://developers.openai.com/api/docs/guides/rate-limits#handle-rapid-traffic-increases-and-model-overload) and [error codes](https://developers.openai.com/api/docs/guides/error-codes).

## Use background=True

Use [`background=True`](https://developers.openai.com/api/docs/guides/background) for requests that may take a long time. Instead of keeping the client connection open, the API starts a job and returns an ID. Your app can poll that job until it finishes, fails, or is canceled. Use it for large analyses, long tool runs, or work that needs status and retry behavior.

```python
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
# Replace the illustrative IDs and URLs below with your own resource values.
from openai import OpenAI
import time

client = OpenAI()
log_bundle_file_id = "file_123"

job = client.responses.create(
    model="gpt-6-astra",
    background=True,
    store=False,
    input="Analyze this large log bundle and cluster the primary failure modes.",
    tools=[
        {
            "type": "code_interpreter",
            "container": {
                "type": "auto",
                "file_ids": [log_bundle_file_id],
            },
        }
    ],
)

while job.status in {"queued", "in_progress"}:
    time.sleep(2)
    job = client.responses.retrieve(job.id)

print(job.output_text)
```

You can combine it with `stream=True` for progress events, but the first event may take longer than a normal request.

From the UI perspective, background mode indicates, “This is running; here is the status; the result will appear here when it’s ready.”

## Use WebSocket mode

[WebSocket mode](https://developers.openai.com/api/docs/guides/websocket-mode) is built for long-running, tool-call-heavy workflows where you keep a persistent connection open and continue by sending only new input items plus `previous_response_id`. For workflows with 20 or more tool calls, we have seen up to roughly 40% faster end-to-end execution.

**How this works**: The first message will look like a normal Responses request: model, instructions, tools, and user input. The server streams events back. If the model asks for a tool, your app runs the tool. Then, instead of sending a new HTTP request, you send another `response.create` event on the same socket with the prior `previous_response_id` and the new item. That is where the latency win comes from. In plain HTTP, every follow-up is a fresh request. In WebSocket mode, the connection stays open and the most recent response state stays warm in memory on that connection. When the next turn continues from that response, the service has to do less setup work.

If your workflow is one request, one answer, then **keep HTTP**. If your workflow behaves like a long-running agent, try WebSocket mode.

Use different `stream_id` values for parallel conversations on one connection; route interleaved events by `stream_id`. A connection supports up to 16 active responses, while requests on the same stream run in order. Connections last up to 60 minutes. Continuation uses the same `previous_response_id` semantics as HTTP mode, with a connection-local cache for the latest response in each stream.

Note: WebSocket mode works with ZDR because your data is not stored to disk, only stored in memory.

The Python sample uses `pip install "openai[realtime]>=3.8.0"`. The JavaScript sample uses `npm install openai@^7.10.0 ws`. The Ruby sample uses `gem install openai async-websocket`.

```python
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
from openai import OpenAI

client = OpenAI()

with client.responses.connect() as connection:
    # Use the same typed parameters as client.responses.create(...).
    connection.response.create(
        model="gpt-6-astra",
        store=False,
        input=[
            {
                "type": "message",
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": (
                            "Find the flaky test in this run, call the tools "
                            "you need, and keep going until you can explain "
                            "the root cause."
                        ),
                    }
                ],
            }
        ],
        tools=[test_log_tool, code_search_tool],
    )
    first_event = connection.recv()
    print(first_event.type)
```

## Use mid-turn steering

If users may add requirements while a GPT-6 model is working, use a WebSocket connection to the Responses API. Send `response.steer` with the active response ID in `previous_response_id` and the new user input. Keep reading events for the continuation; `response.steer.accepted` means the update is queued. Steering does not change output already sent to your application or undo tools that have started. See [mid-turn steering](https://developers.openai.com/api/docs/guides/steering) for the event flow and tool-result handling.

## Final takeaway

Responses API is the foundation for building smarter, more capable OpenAI applications. The real advantage is that it lets developers move from one-off prompts to durable, tool-using, context-aware workflows that can adapt to the complexity of the task. Follow this guide to see higher performance in real deployments.
