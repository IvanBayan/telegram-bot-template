from telegram.ext import CommandHandler

from bot.callbacks.start import handle_start

HANDLERS = [
    CommandHandler("start", handle_start),
]
