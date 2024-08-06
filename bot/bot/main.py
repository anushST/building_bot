"""Bot's main file."""
import logging
from os import getenv

from dotenv import load_dotenv
from telegram import (InlineKeyboardButton, InlineKeyboardMarkup,
                      InputMediaPhoto, Update)
from telegram.ext import (CallbackContext, CallbackQueryHandler,
                          CommandHandler, Filters, MessageHandler, Updater)

from . import constants
from . import db_queries
from .decorators import safe_handler_method
from .exceptions import BadRequestError, LangNotChosenError, NoTokenError
from display_data import buttons, texts
from utils.paginators import Paginator
from utils.shortcuts import edit_message_caption, send_photo

logger = logging.getLogger('main')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s '
                              '(def %(funcName)s:%(lineno)d)')
handler = logging.handlers.RotatingFileHandler(
    'logs/bot.log', maxBytes=5*1024*1024, backupCount=2
)
handler.setFormatter(formatter)
logger.addHandler(handler)


def check_token(token) -> None:
    """Check if the token is None."""
    if token is None:
        logger.critical('Missing required environment variable(token)')
        raise NoTokenError('No Token')


@safe_handler_method
def start(update: Update, context: CallbackContext) -> None:
    """Send language choice.

    Calls on /start command.
    """
    db_queries.create_user(update.effective_chat.id)
    keyboard = [
        [InlineKeyboardButton(
             buttons.TJ_LANG_CHOOSE_BUTTON,
             callback_data=f'{constants.LANG_PATTERN}{constants.TJ}'),
         InlineKeyboardButton(
             buttons.RU_LANG_CHOOSE_BUTTON,
             callback_data=f'{constants.LANG_PATTERN}{constants.RU}')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    message = update.message.reply_text(texts.CHOOSE_LANG_TEXT,
                                        reply_markup=reply_markup)
    context.bot_data['lang_message_id'] = message.message_id
    update.message.delete()


@safe_handler_method
def save_lang(update: Update, context: CallbackContext) -> None:
    """Save users language and call main_menu."""
    query = update.callback_query
    chat_id = update.effective_chat.id
    lang = query.data.split(constants.LANG_PATTERN)[1]
    if lang in constants.LANGUAGES:
        db_queries.User(chat_id).edit_field('lang', lang)
    else:
        raise BadRequestError('Lang is in incorrect format.')
    main_menu(update, context)


@safe_handler_method
def main_menu(update: Update, context: CallbackContext) -> None:
    """Send main menu.

    Here are three navigation buttons: Contact Information, About Academy
    and Courses.
    """
    query = update.callback_query
    chat_id = update.effective_chat.id
    lang = db_queries.User(chat_id).get_field('lang')
    if lang is None:
        raise LangNotChosenError

    keyboard = [
        [InlineKeyboardButton(buttons.PHOTO_GALLERY_BUTTON[lang],
                              callback_data=constants.PHOTO_GALLERY_CALLBACK)],
        [InlineKeyboardButton(buttons.HOUSE_PLAN_BUTTON[lang],
                              callback_data=constants.BLOCK_PLAN_CALLBACK)],
        [InlineKeyboardButton(buttons.ABOUT_COMPANY_BUTTON[lang],
                              callback_data=constants.COMPANY_DESC_CALLBACK)],
        [InlineKeyboardButton(buttons.CONTACT_INFO_BUTTON[lang],
                              callback_data=constants.CONTACT_INFO_CALLBACK),],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    user_object = db_queries.User(chat_id)
    if not user_object.get_field('main_message_id'):
        message = send_photo(
            url=constants.MAIN_IMAGE,
            bot=context.bot,
            chat_id=chat_id,
            caption=texts.WELCOME_TEXT[lang],
            reply_markup=reply_markup,
            parse_mode='HTML'
        )
        user_object.edit_field('main_message_id', message.message_id)
    else:
        edit_message_caption(query, texts.WELCOME_TEXT[lang], reply_markup)
    if 'lang_message_id' in context.bot_data:
        context.bot.delete_message(chat_id,
                                   context.bot_data['lang_message_id'])
        context.bot_data.pop('lang_message_id')


@safe_handler_method
def contact_info(update: Update, context: CallbackContext) -> None:
    """Send contact info."""
    query = update.callback_query
    chat_id = update.effective_chat.id
    lang = db_queries.User(chat_id).get_field('lang')
    if lang is None:
        raise LangNotChosenError
    keyboard = [
        [InlineKeyboardButton(buttons.INSTAGRAM_BUTTON,
                              constants.INSTAGRAM_URL)],
        [InlineKeyboardButton(buttons.TELEGRAM_CHANNEL_BUTTON,
                              constants.TELEGRAM_CHANNEL_URL)],
        [InlineKeyboardButton(buttons.BACK_BUTTON[lang],
                              callback_data=constants.MAIN_MENU_CALLBACK)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    edit_message_caption(query, texts.CONTACTS_TEXT[lang], reply_markup,
                         parse_mode='HTML')


@safe_handler_method
def about_company(update: Update, context: CallbackContext) -> None:
    """Send information about academy."""
    query = update.callback_query
    chat_id = update.effective_chat.id
    lang = db_queries.User(chat_id).get_field('lang')
    if lang is None:
        raise LangNotChosenError
    keyboard = [
        [InlineKeyboardButton(buttons.BACK_BUTTON[lang],
                              callback_data=constants.MAIN_MENU_CALLBACK)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    edit_message_caption(query, texts.ABOUT_COMPANY_TEXT[lang], reply_markup,
                         parse_mode='HTML')


@safe_handler_method
def building_parts(update: Update, context: CallbackContext) -> None:
    """Send courses list."""
    query = update.callback_query
    chat_id = update.effective_chat.id
    lang = db_queries.User(chat_id).get_field('lang')
    if lang is None:
        raise LangNotChosenError
    page = int(query.data.split(constants.BLOCKS_PATTERN)[1])
    paginator = Paginator(texts.BUILDING_PARTS,
                          constants.BLOCKS_PATTERN,
                          constants.ITEMS_PER_PAGE)
    keyboard = [[]]

    for callback_data, block in paginator.get_page(page):
        callback = f'{constants.FLOORS_PATTERN}{callback_data}&{1}'
        button_text = block[lang]['button_text']
        keyboard[0].append(InlineKeyboardButton(button_text,
                                                callback_data=callback))

    keyboard.append(
        [InlineKeyboardButton(buttons.BACK_BUTTON[lang],
                              callback_data=constants.MAIN_MENU_CALLBACK)])

    reply_markup = InlineKeyboardMarkup(keyboard)
    main_message_id = db_queries.User(
        chat_id).get_field('main_message_id')
    caption = texts.BUILDING_PLAN_TEXT[lang]
    if not main_message_id:
        message = send_photo(
            url=constants.MAIN_IMAGE,
            bot=context.bot,
            chat_id=chat_id,
            caption=caption,
            reply_markup=reply_markup,
            parse_mode='HTML'
        )
        cureent_message_id, message_name = db_queries.User(
            chat_id).current_message_id()
        if cureent_message_id and message_name != 'main_message_id':
            query.delete_message(cureent_message_id)
            db_queries.User(chat_id).edit_field(message_name, None)
        db_queries.User(chat_id).edit_field('main_message_id',
                                            message.message_id)

    else:
        edit_message_caption(query, caption, reply_markup, parse_mode='HTML')


@safe_handler_method
def floors(update: Update, context: CallbackContext) -> None:
    """Send floors list."""
    query = update.callback_query
    chat_id = update.effective_chat.id
    lang = db_queries.User(chat_id).get_field('lang')
    if lang is None:
        raise LangNotChosenError
    block_name, page = query.data.split(constants.FLOORS_PATTERN)[1].split('&')
    page = int(page)
    paginator = Paginator(texts.BUILDING_PARTS[block_name]['floors'],
                          constants.FLOORS_PATTERN,
                          constants.ITEMS_PER_PAGE)
    keyboard = [[]]

    for callback_data, floor in paginator.get_page(page):
        callback = f'{constants.FLOOR_PATTERN}{callback_data}&{block_name}'
        button_text = floor[lang]['button_text']
        keyboard[0].append(InlineKeyboardButton(button_text,
                                                callback_data=callback))

    keyboard.append(
        [InlineKeyboardButton(buttons.BACK_BUTTON[lang],
                              callback_data=constants.BLOCK_PLAN_CALLBACK)])

    reply_markup = InlineKeyboardMarkup(keyboard)
    block_info_message_id = db_queries.User(
        chat_id).get_field('block_info_message_id')
    caption = texts.BUILDING_PARTS[block_name][lang]['text']
    if not block_info_message_id:
        message = send_photo(
            url=texts.BUILDING_PARTS[block_name]['default_photo'],
            bot=context.bot,
            chat_id=chat_id,
            caption=caption,
            reply_markup=reply_markup,
            parse_mode='HTML'
        )
        cureent_message_id, message_name = db_queries.User(
            chat_id).current_message_id()
        if cureent_message_id and message_name != 'block_info_message_id':
            query.delete_message(cureent_message_id)
            db_queries.User(chat_id).edit_field(message_name, None)
        db_queries.User(chat_id).edit_field('block_info_message_id',
                                            message.message_id)
    else:
        edit_message_caption(query, caption, reply_markup, parse_mode='HTML')


@safe_handler_method
def floor_info(update: Update, context: CallbackContext) -> None:
    """Send information about the block."""
    query = update.callback_query
    floor_name, block_name = (query.data.split(
        constants.FLOOR_PATTERN)[1].split('&'))
    chat_id = update.effective_chat.id
    lang = db_queries.User(chat_id).get_field('lang')
    if lang is None:
        raise LangNotChosenError
    keyboard = [
        [InlineKeyboardButton(buttons.BACK_BUTTON[lang],
                              callback_data=(constants.FLOORS_PATTERN +
                                             f'{block_name}&1'))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    course_info_message_id = db_queries.User(
        chat_id).get_field('floor_info_message_id')
    caption = (texts.BUILDING_PARTS[block_name]['floors'][floor_name]
               [lang]['text'])
    if not course_info_message_id:
        message = send_photo(
            url=(texts.BUILDING_PARTS[block_name]['floors'][floor_name]
                 ['photo']),
            bot=context.bot,
            chat_id=chat_id,
            caption=caption,
            reply_markup=reply_markup,
            parse_mode='HTML'
        )
        cureent_message_id, message_name = db_queries.User(
            chat_id).current_message_id()
        if cureent_message_id and message_name != 'floor_info_message_id':
            query.delete_message(cureent_message_id)
            db_queries.User(chat_id).edit_field(message_name, None)
        db_queries.User(chat_id).edit_field('floor_info_message_id',
                                            message.message_id)


@safe_handler_method
def show_gallery(update: Update, context: CallbackContext) -> None:
    """Send photo_gallery."""
    query = update.callback_query
    chat_id = update.effective_chat.id
    lang = db_queries.User(chat_id).get_field('lang')
    if lang is None:
        raise LangNotChosenError

    photos = []

    for photo_url in constants.photo_gallery_urls:
        photos.append(InputMediaPhoto(photo_url))

    query.message.reply_media_group(media=photos)


@safe_handler_method
def delete_user_message(update: Update, context: CallbackContext) -> None:
    """Delete all messages sent by user."""
    update.message.delete()


def main() -> None:
    """Start bot."""
    load_dotenv()
    TELEGRAM_TOKEN = getenv('TELEGRAM_TOKEN')
    check_token(TELEGRAM_TOKEN)
    try:
        updater = Updater(TELEGRAM_TOKEN)
        dispatcher = updater.dispatcher

        dispatcher.add_handler(CommandHandler(constants.START_COMMAND, start))
        dispatcher.add_handler(CallbackQueryHandler(
            save_lang, pattern=constants.LANG_PATTERN))
        dispatcher.add_handler(CallbackQueryHandler(
            main_menu, pattern=constants.MAIN_MENU_CALLBACK))
        dispatcher.add_handler(CallbackQueryHandler(
            contact_info, pattern=constants.CONTACT_INFO_CALLBACK))
        dispatcher.add_handler(CallbackQueryHandler(
            about_company, pattern=constants.COMPANY_DESC_CALLBACK))
        dispatcher.add_handler(CallbackQueryHandler(
            building_parts, pattern=f'^{constants.BLOCKS_PATTERN}'))
        dispatcher.add_handler(CallbackQueryHandler(
            show_gallery, pattern=constants.PHOTO_GALLERY_CALLBACK))
        dispatcher.add_handler(CallbackQueryHandler(
            floors, pattern=f'^{constants.FLOORS_PATTERN}'))
        dispatcher.add_handler(CallbackQueryHandler(
            floor_info, pattern=f'^{constants.FLOOR_PATTERN}'))
        dispatcher.add_handler(MessageHandler(Filters.all,
                                              delete_user_message))

        updater.start_polling()
        updater.idle()
    except Exception as e:
        logger.error(f'An error occured in: {e}', exc_info=True)
