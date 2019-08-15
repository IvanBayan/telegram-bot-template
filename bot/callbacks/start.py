from sqlalchemy.orm import Session
from telegram import Update
from telegram.ext import CallbackContext

from bot import model
from bot.helpers import get_session


# Imaginary attacker can start bot with something other than `/start` via
#  MTProto and raise exception somewhere(interaction with db), but who cares?
@get_session
def handle_start(update: Update, context: CallbackContext, session: Session):
    del context  # Not used
    update.effective_chat.send_message("Hello world!")
    user = (
        session.query(model.User)
        .filter_by(ext_user_id=update.effective_user.id)
        .first()
    )
    if not user:
        user = model.User(ext_user_id=update.effective_user.id)
        session.add(user)
        session.commit()
