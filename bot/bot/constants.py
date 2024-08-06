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
MAIN_IMAGE_ID = 'AgACAgIAAxkDAAICiWayBksXICgDfowMlVyuws4UctoJAAL65DEbq6qISYevw9bEKaKQAQADAgADcwADNQQ'
photo_gallery_urls = [
    'AgACAgQAAxkDAAIC1WayDISKQnGcabK2j5p6ShF8c4HNAAJBtTEbg6eNUVQqfPhjVh3TAQADAgADcwADNQQ',
    'AgACAgQAAxkDAAIC1mayDIQdKczy5RmdJmdIY3cDt4FjAAKbtDEbmkuVUTqV_x8Bl19zAQADAgADcwADNQQ',
    'AgACAgQAAxkDAAIC12ayDISVPxvC78BTZqetn1syECLvAALNtDEbfRWVUWAyj1D_B2bJAQADAgADcwADNQQ',
    'AgACAgQAAxkDAAIC2GayDISB97pQvPNFqMfCc5oAAfPoxAACp7QxG2YmjFFEw65ko0wGrAEAAwIAA3MAAzUE',
    'AgACAgQAAxkDAAIC2WayDIQd5XSOV1eDO7a7MFy2L6fFAAJ4tDEbEGqVUTWflZDyCTjpAQADAgADcwADNQQ',
    'AgACAgQAAxkDAAIC2mayDISaiX4o_gUxWSywA2ql0fkKAAIFtTEbx22UUS9Aw1yucWgoAQADAgADcwADNQQ',
    'AgACAgQAAxkDAAIC22ayDIRngjXRtFbQ81phU-I92r5EAAKBtDEbnsGVUYClLIi0NAd-AQADAgADcwADNQQ',
    'AgACAgQAAxkDAAIC3GayDIQZtHaglEXveUOs-xkIQRX2AAJztDEbcTaUUTLy2Ms5c3VRAQADAgADcwADNQQ',
]
