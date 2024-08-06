"""Shortcuts of the bot."""
from telegram import Message
from telegram.error import BadRequest


def edit_message_caption_or_text(query, message, **kwargs) -> Message:
    """Edit message caption.

    Shortcuted to handle Message to edit not found message.
    """
    try:
        try:
            query.edit_message_caption(message, **kwargs)
        except BadRequest as e:
            if not str(e) == 'There is no caption in the message to edit':
                raise
            query.edit_message_text(message, **kwargs)
    except BadRequest as e:
        if not str(e) == 'Message to edit not found':
            raise
