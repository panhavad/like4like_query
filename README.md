# Like4Like Query Telegram Bot

![Language](https://img.shields.io/github/languages/top/panhavad/like4like_query) ![Last commit](https://img.shields.io/github/last-commit/panhavad/like4like_query) [![Release](https://img.shields.io/github/v/release/panhavad/like4like_query?include_prereleases)](https://github.com/panhavad/like4like_query/releases/latest)

A **Telegram bot** that reports the status of your **Like4Like** Facebook page campaigns. Send `/detail <page_id>` and the bot logs in with a headless Chrome session, reads the campaign table and replies with the current status and completed likes.

![System snapshot](docs/snapshot.svg)

## Features

- `/detail <page_id>` command
- Headless Selenium + webdriver-manager
- Session cookie login (no password stored)
- Request logging to `stat.log`

## How it works

```mermaid
flowchart LR
    U["Telegram user"] -->|"/detail id"| B["Bot - python-telegram-bot"]
    B --> S["Selenium headless Chrome"]
    S -->|"PHPSESSID cookie"| L["like4like.org"]
    L --> S
    S -->|"status + likes"| B
    B --> U
```

## Getting started

```bash
pip install -r requirement.txt
cp sample.env .env   # set TELEGRAM_BOT_TOKEN and SESS_ID
python main.py
```

## Download

Grab the packaged source from the [latest release](https://github.com/panhavad/like4like_query/releases/latest).

## Tech stack

- Python
- python-telegram-bot
- Selenium

## Project structure

```text
like4like_query/
├── __pycache__/
├── docs/
├── like4like/
├── .gitignore
├── main.py
├── README.md
├── requirement.txt
└── sample.env
```
