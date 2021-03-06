import functools

import click
import coloredlogs
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from telegram.ext import Updater, dispatcher, messagequeue as mq
from telegram.utils.request import Request

import bot
from bot.callbacks import HANDLERS
from bot.model import presets
from bot.helpers import MQBot


def setup_updater(token: str) -> Updater:
    q = mq.MessageQueue(all_burst_limit=29)  # 30 msgs/s limit
    request = Request(con_pool_size=8)
    mq_bot = MQBot(token, request=request, mqueue=q)
    updater = Updater(bot=mq_bot, use_context=True)

    return updater


def setup_handlers(updater: Updater):
    updater.dispatcher.groups = [dispatcher.DEFAULT_GROUP]
    updater.dispatcher.handlers[dispatcher.DEFAULT_GROUP] = HANDLERS


def setup_database_engine(db_uri):
    engine = create_engine(db_uri)
    Session = sessionmaker(engine)
    bot.Session = scoped_session(Session)


@click.group()
@click.option("--debug", default=False, is_flag=True)
def cli(debug: bool = False):
    level = "DEBUG" if debug else "WARNING"
    coloredlogs.install(level)


def pass_bot_settings(func):
    @click.option("--token", envvar="TOKEN", required=True)
    @click.option("--db-uri", envvar="DB_URI", required=True)
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@cli.command()
@pass_bot_settings
def start_polling(token: str, db_uri: str):
    setup_database_engine(db_uri)
    updater = setup_updater(token)
    setup_handlers(updater)
    updater.start_polling()
    updater.idle()


@cli.command()
@pass_bot_settings
@click.option("--port", default=8080, type=int)
def start_webhook(token: str, db_uri: str, port: int):
    setup_database_engine(db_uri)
    updater = setup_updater(token)
    setup_handlers(updater)
    updater.start_webhook(port=port)
    updater.idle()


@cli.command()
@click.option("--rm", is_flag=True, default=False)
@click.option("--db-uri", envvar="DB_URI", required=True)
def setup_database(rm: bool, db_uri: str):
    presets.setup_database(rm, db_uri)
    click.secho("Database setup complete", fg="green")
