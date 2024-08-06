"""Constants of bot package."""
# flake8: noqa: E501

# Languages
TJ = 'tj'
RU = 'ru'
LANGUAGES = [TJ, RU]

# CallBack patters
LANG_PATTERN = 'lang_'
BLOCK_PATTERN = 'block_'
BLOCKS_PATTERN = 'blocks_page_'
FLOOR_PATTERN = 'floor_block_'
FLOORS_PATTERN = 'floors_block_page_'

# CallBacks
LANG_TJ_CALLBACK = 'lang_tj'
LANG_RU_CALLBACK = 'lang_ru'
CONTACT_INFO_CALLBACK = 'contact_info'
COMPANY_DESC_CALLBACK = 'company_desc'
BLOCK_PLAN_CALLBACK = BLOCKS_PATTERN + '1'
FLOORS_CALLBACK = FLOOR_PATTERN + '1'
MAIN_MENU_CALLBACK = 'main_menu'
PHOTO_GALLERY_CALLBACK = 'photo_gallery'

# Commands
START_COMMAND = 'start'

# Contacts
INSTAGRAM_URL = 'https://www.instagram.com/webacademy.tj?igsh=eWh4YzExOXNzaDRq'
REGISTER_URL = ('https://docs.google.com/forms/d/1Fkr0s_IPnkmeA1N4wfhqsrXFHLdy'
                'qPkKiuDttVDUxDU/viewform?fbclid=PAZXh0bgNhZW0CMTEAAaYhxSaAk_S'
                'X80ml_dsNNBqTm99CrjDLk9n5ag46gy7h9AQON_p8yiYYUDs_aem_AWjlqWOb'
                'aSqt13rBLiNvPsx4P_MCjG7raKg7SdkJQ9oNd0m112-byqjUbRBmZwDDlaV6j'
                'HUQCcf4KvAgXD1jPpsa&edit_requested=true')
TELEGRAM_CHANNEL_URL = 'https://t.me/webacademychannel'

# Paginator
ITEMS_PER_PAGE = 10

# Database
DATABASE = 'bot/db.sqlite3'

# Photos
MAIN_IMAGE = 'main.png'
photo_gallery_urls = [
    'https://raw.githubusercontent.com/anushST/building_bot/develop/bot/static/gallery/photo1.jpg',
    'https://raw.githubusercontent.com/anushST/building_bot/develop/bot/static/gallery/photo2.jpg',
    'https://raw.githubusercontent.com/anushST/building_bot/develop/bot/static/gallery/photo3.jpg',
    'https://raw.githubusercontent.com/anushST/building_bot/develop/bot/static/gallery/photo4.jpg',
    'https://raw.githubusercontent.com/anushST/building_bot/develop/bot/static/gallery/photo5.jpg',
    'https://raw.githubusercontent.com/anushST/building_bot/develop/bot/static/gallery/photo6.jpg',
    'https://raw.githubusercontent.com/anushST/building_bot/develop/bot/static/gallery/photo7.jpg',
    'https://raw.githubusercontent.com/anushST/building_bot/develop/bot/static/gallery/photo8.jpg',
]
