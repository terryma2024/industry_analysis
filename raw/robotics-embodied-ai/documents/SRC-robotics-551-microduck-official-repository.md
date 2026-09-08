---
source_id: "SRC-robotics-551"
title: "Microduck official repository"
source_type: "code_repository"
publisher: "Pollen Robotics"
source_date: "2026-09-02"
url: "https://github.com/pollen-robotics/microduck"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-09-08T01:07:13+00:00"
tags:
  - raw/source
  - source-type/code-repository
  - evidence/s
aliases:
  - SRC-robotics-551
---
# Microduck official repository

[![microduck](https://private-user-images.githubusercontent.com/6552564/641503621-c2f7c245-8217-46a1-8d1e-e0ba967cd969.webp?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODg4Mjk5MzQsIm5iZiI6MTc4ODgyOTYzNCwicGF0aCI6Ii82NTUyNTY0LzY0MTUwMzYyMS1jMmY3YzI0NS04MjE3LTQ2YTEtOGQxZS1lMGJhOTY3Y2Q5Njkud2VicD9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjA5MDglMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwOTA4VDAxMDcxNFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWQ5NDZmNjhjY2Y0YTAxNmQ4ZjJiNGNhMmFiYzgyNDU5YjAyZmY1ZGM1YTZhYWQxMTdlMjhhZDY5NDdlZWE2ZjUmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT1pbWFnZSUyRndlYnAifQ.ue3wHshnhM_j0CrLSrOjzvKlHdB6sCZwWXwc7g9KMrE)](https://private-user-images.githubusercontent.com/6552564/641503621-c2f7c245-8217-46a1-8d1e-e0ba967cd969.webp?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODg4Mjk5MzQsIm5iZiI6MTc4ODgyOTYzNCwicGF0aCI6Ii82NTUyNTY0LzY0MTUwMzYyMS1jMmY3YzI0NS04MjE3LTQ2YTEtOGQxZS1lMGJhOTY3Y2Q5Njkud2VicD9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjA5MDglMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwOTA4VDAxMDcxNFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWQ5NDZmNjhjY2Y0YTAxNmQ4ZjJiNGNhMmFiYzgyNDU5YjAyZmY1ZGM1YTZhYWQxMTdlMjhhZDY5NDdlZWE2ZjUmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT1pbWFnZSUyRndlYnAifQ.ue3wHshnhM_j0CrLSrOjzvKlHdB6sCZwWXwc7g9KMrE)

## Microduck

*A tiny biped robot that moves using reinforcement learning policies.*

[**Get yours here**](https://pollen-robotics.com/microduck) · [Cheat sheet](https://github.com/pollen-robotics/microduck/blob/main/docs/robot/cheatsheet.md) · [Training the policies](https://github.com/pollen-robotics/microduck_rl) · [How it works](https://github.com/pollen-robotics/microduck/blob/main/docs/design/architecture.md) · [Contributing](https://github.com/pollen-robotics/microduck/blob/main/CONTRIBUTING.md)

[![CI](https://github.com/pollen-robotics/microduck/actions/workflows/ci.yml/badge.svg)](https://github.com/pollen-robotics/microduck/actions/workflows/ci.yml)

---

**This repo is the duck's brain.** About 25 cm and 800 g of robot, run by a handful of daemons on a Rockchip RK3566: a 50 Hz control loop driving fifteen servos from neural policies, the radios and the camera, and the update machinery that gets new software onto a robot without bricking it.

Everything you need to run a Microduck is here. **If you want one, [get yours here](https://pollen-robotics.com/microduck).**

The policies it runs are trained next door, in **[microduck\_rl](https://github.com/pollen-robotics/microduck_rl)** — MuJoCo and PPO, the sim2real recipe, and the export to ONNX that this repo loads.

## It does things

| walk.MP4<video src="https://private-user-images.githubusercontent.com/4290742/641656559-356a6011-8e0d-4b28-bda9-da78646583a3.MP4?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODg4Mjk5MzQsIm5iZiI6MTc4ODgyOTYzNCwicGF0aCI6Ii80MjkwNzQyLzY0MTY1NjU1OS0zNTZhNjAxMS04ZTBkLTRiMjgtYmRhOS1kYTc4NjQ2NTgzYTMuTVA0P1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MDkwOCUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjA5MDhUMDEwNzE0WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9MmQ4ZTg0ZTY3MTA2NDE3ZDQ2MGFhZWMxMmU5ODA2M2ExODZiMGMwZmVlMWYxNjFlODdhNmU4ZmJhOTg0NzYwZSZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmcmVzcG9uc2UtY29udGVudC10eXBlPXZpZGVvJTJGbXA0In0.k5Riwl8Q2xN0Gi_CwxV63S4iYoUGzdX18kbKRlpcX9k" controls="controls"></video> | roller\_cut.mp4<video src="https://private-user-images.githubusercontent.com/6552564/641507835-abfbf250-1b1c-42cb-8430-00267e2b148a.mp4?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODg4Mjk5MzQsIm5iZiI6MTc4ODgyOTYzNCwicGF0aCI6Ii82NTUyNTY0LzY0MTUwNzgzNS1hYmZiZjI1MC0xYjFjLTQyY2ItODQzMC0wMDI2N2UyYjE0OGEubXA0P1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MDkwOCUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjA5MDhUMDEwNzE0WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9OWNhNzY5MGZjMjcxMTczNWI4Mjc3MWJjMDRlYTVhOWNmZDY1MjM5MjhiY2Y3ODk1M2VmMzg2ZThlMjBiYmY1MSZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmcmVzcG9uc2UtY29udGVudC10eXBlPXZpZGVvJTJGbXA0In0.fVE0viZMQldshcrRpzK9qhJZIoa4HX_jHYU3ZGvWSwk" controls="controls"></video> |
| --- | --- |
| **It walks.** Pick up a gamepad and drive. | **It rolls.** Put wheels on, hold D-pad up, and it loads the other brain. |
| grasp.MP4<video src="https://private-user-images.githubusercontent.com/4290742/641656543-7e70c1da-e120-428f-ae0b-f4de62f25984.MP4?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODg4Mjk5MzQsIm5iZiI6MTc4ODgyOTYzNCwicGF0aCI6Ii80MjkwNzQyLzY0MTY1NjU0My03ZTcwYzFkYS1lMTIwLTQyOGYtYWUwYi1mNGRlNjJmMjU5ODQuTVA0P1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MDkwOCUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjA5MDhUMDEwNzE0WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9YzBjMGE5MDVmYmU3ODlhN2Y4N2UyZDQ4YmIwNGUyYWJhODliNDcyZmJmYzQwNDljNzQ1ZmJhNDg3ZDcyMDNlNiZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmcmVzcG9uc2UtY29udGVudC10eXBlPXZpZGVvJTJGbXA0In0.JcaQMsTlEWemwKsloVwdqJWOvaROuG4HFULtBJYpd10" controls="controls"></video> | standup.MP4<video src="https://private-user-images.githubusercontent.com/4290742/641656555-3eef63a5-6f84-47cf-90de-e717e6d7f8f0.MP4?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODg4Mjk5MzQsIm5iZiI6MTc4ODgyOTYzNCwicGF0aCI6Ii80MjkwNzQyLzY0MTY1NjU1NS0zZWVmNjNhNS02Zjg0LTQ3Y2YtOTBkZS1lNzE3ZTZkN2Y4ZjAuTVA0P1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MDkwOCUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjA5MDhUMDEwNzE0WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9ODAyNzhlZThmOTY2NmM3OWFlZjEyNmU2MGU1ODFkOTBjMmUxMDVmOTJkYjY1NGY4OWE1MzExMjM0ZWRkYTBlZCZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmcmVzcG9uc2UtY29udGVudC10eXBlPXZpZGVvJTJGbXA0In0.8Wh6SODW4_Ryr_QSpdQ_7yneR7czo4sgwS1XSFGtaUw" controls="controls"></video> |
| **It picks things up.** Beak to the floor, one button. | **It gets back up.** Knock it over and it stands itself up. |

It also sits, kicks a ball, rolls forward on command, and quacks in a voice that is its own.

## Where to find things

### You have a duck

|  |  |
| --- | --- |
| [Cheat sheet](https://github.com/pollen-robotics/microduck/blob/main/docs/robot/cheatsheet.md) | Every `robotctl` command: drive, configure, voice, chorale, theremin, wifi, updates, logs. Start here. |
| [Gamepad](https://github.com/pollen-robotics/microduck/blob/main/docs/robot/cheatsheet.md#gamepad-configd) | The full button mapping, and pairing a pad — [once per pad](https://github.com/pollen-robotics/microduck/blob/main/docs/robot/pair-a-gamepad.md), plus what to do when it will not bond. |
| [`duckctl`](https://github.com/pollen-robotics/microduck/blob/main/docs/robot/duckctl.md) | The robot from a laptop over Bluetooth, with no network and no ssh. |
| [Updates](https://github.com/pollen-robotics/microduck/blob/main/docs/robot/cheatsheet.md#updates-updaterd) | Install, roll back, pin. Every update is verified, health-gated and reversible. |

### You are building on it

|  |  |
| --- | --- |
| [microduck\_rl](https://github.com/pollen-robotics/microduck_rl) | Where the policies come from: MuJoCo, PPO, domain randomisation, and the ONNX export this repo loads. |
| [How it works](https://github.com/pollen-robotics/microduck/blob/main/docs/design/architecture.md) | The whole system on one page — the daemons, the bus, how an update reaches a robot — then a page per part. |
| [Set up a dev board](https://github.com/pollen-robotics/microduck/blob/main/docs/robot/install-dev.md) | From a blank board to a robot that takes branch builds. |
| [Dev cheat sheet](https://github.com/pollen-robotics/microduck/blob/main/docs/robot/cheatsheet-dev.md) | Branch builds, release candidates, driving from a laptop, and the restart traps after an update. |
| [Push your branch](https://github.com/pollen-robotics/microduck/blob/main/docs/robot/dev-push.md) | Build on your machine, install over ssh, about a minute. |
| [CONTRIBUTING.md](https://github.com/pollen-robotics/microduck/blob/main/CONTRIBUTING.md) | Building, testing, layout, conventions, releasing. |
| [Docs index](https://github.com/pollen-robotics/microduck/blob/main/docs/README.md) | Everything, including the design pages and the open problems. |

## Under the hood

Rust, no framework, one workspace. `robotd` owns the control loop and the motor bus; `updaterd` installs signed releases and rolls them back when a robot comes up unhealthy; `configd` owns wifi and identity; `btd` is the Bluetooth path a phone uses; `padd` reads the gamepad; `mediad` streams the camera over WebRTC; `tofd` serves the depth sensor. They talk over one JSON-RPC contract on Unix sockets, and every client — the app, the console, the gamepad, your script — sends exactly the same calls.

The interesting decisions are written down: [`docs/design/`](https://github.com/pollen-robotics/microduck/blob/main/docs/design) is why things are the way they are, and [`docs/project/`](https://github.com/pollen-robotics/microduck/blob/main/docs/project) is what has gone wrong and what would close it.
