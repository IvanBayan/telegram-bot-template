import functools

from telegram import Update
from telegram.ext import CallbackContext

import bot


def get_session(func):
    """Session decorator for handlers"""

    @functools.wraps(func)
    def wrapper(update: Update, context: CallbackContext):
        session = bot.Session()
        try:
            result = func(update, context, session)
        except Exception as e:
            session.rollback()
            raise e
        finally:
            bot.Session.remove()

        return result

    return wrapper
