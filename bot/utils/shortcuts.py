"""Shortcuts of the bot."""
from telegram import Bot, Message
from telegram.error import BadRequest


def send_photo(url: str, bot: Bot, **kwargs) -> Message:
    """Send photo.

    Arguments:
        url - regarding the static folder.
        bot - the bot instance.
        **kwargs - bot.send_photo arguments.
    """
    with open(f'static/{url}', 'rb') as photo:
        message = bot.send_photo(photo=photo, **kwargs)
    return message


def edit_message_caption(query, *args, **kwargs) -> Message:
    """Edit message caption.

    Shortcuted to handle Message to edit not found message.
    """
    try:
        query.edit_message_caption(*args, **kwargs)
    except BadRequest as e:
        if not str(e) == 'Message to edit not found':
            raise
