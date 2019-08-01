import logging

from telegram import Bot
from telegram.ext import messagequeue as mq

__log__ = logging.getLogger(__name__)


# Borrowed from:
# github.com/python-telegram-bot/python-telegram-bot/wiki/Avoiding-flood-limits
class MQBot(Bot):
    """Queued `Bot` wrapper for `send_message`"""

    def __init__(self, *args, is_queued_def=True, mqueue=None, **kwargs):
        super().__init__(*args, **kwargs)
        self._is_messages_queued_default = is_queued_def
        self._msg_queue = mqueue or mq.MessageQueue()

    def __del__(self):
        try:
            self._msg_queue.stop()
        except:
            __log__.exception("MQBot exception")
        super().__del__()

    @mq.queuedmessage
    def send_message(self, *args, **kwargs):
        return super().send_message(*args, **kwargs)
