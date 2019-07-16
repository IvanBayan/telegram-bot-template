# Telegram Bot Template [![Built on: Telegram Bot Template](https://img.shields.io/badge/Built%20On-Telegram%20Bot%20Template-brightgreen.svg)](https://github.com/yarfuo/telegram-bot-template)
SQLAlchemy bot template with simple console line interface.

Run `./clean.sh` before usage(removes `LICENSE` and reinit git repo in current folder)

## Usage:

First of all, you need to set `DB_URI` environment variable:
`export DB_URI=sqlite:////tmptest`
Or add argument to command:
`pytohn -m bot .. --db-uri sqlite:////tmp/test.db`

SQLAlchemy supports PostgreSQL, MySQL, SQLite, Oracle, etc..
You can read [here](https://docs.sqlalchemy.org/en/13/core/engines.html) about 
supported database drivers

Then, you need to set `TOKEN`:
`export TOKEN=123456:AAaaaaaaaaaaaaaaaaaaaaaaaaaa` 

You can get your bot token from [@BotFather](https://t.me/BotFather).

##### Database setup:
`python -m bot setup-database`

Also, you can drop all data before proceed database setup, if you pass `--rm` 
flag.

##### Start bot with local webhook server
`python -m bot start-webhook --port 8080`

I prefer to use `nginx` as reverse proxy for mine telegram bots. 

##### Start bot with polling worker
`python -m bot start-polling`
