from telegram import Update
from telegram.ext import CallbackContext


def handle_start(update: Update, context: CallbackContext):
    del context  # Not used
    update.effective_chat.send_message("Hello world!")
