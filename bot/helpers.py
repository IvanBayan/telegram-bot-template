import functools

import bot


def get_session(func):
    """Session decorator for handlers"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        session = bot.Session()
        try:
            result = func(session, *args, **kwargs)
        except Exception as e:
            session.rollback()
            raise e
        finally:
            bot.Session.remove()

        return result

    return wrapper
