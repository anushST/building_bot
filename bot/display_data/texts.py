# flake8: noqa: E501
"""All texts to display."""
from bot.constants import TJ, RU

CHOOSE_LANG_TEXT = 'Забонро интихоб кунед / Выберите язык:'
ERROR_TEXT = (
    '❗ <b>Хатоги рух дод. Хохишмандем историяи ботро тоза кунед ва аз сари нав сар дихед.</b> ❗\n\n'
    '❗ <b>Произошла ошибка. Просим очистить историю бота и запустить его заного.</b> ❗'
)
LANG_NOT_CHOSEN_ERROR_TEXT = (
    '❗ <b>Забони бот интихоб нашудааст. Хохишмандем историяи ботро тоза кунед ва аз сари нав сар дихед.</b> ❗\n\n'
    '❗ <b>Не выбран язык бот. Просим очистить историю бота и запустить его заного.</b> ❗'
)
BUILDING_PLAN_TEXT = {
    TJ: '📌 Плани здание:',
    RU: '📌 План здания: ',
}
WELCOME_TEXT = {
    TJ: 'Хуш омадед ба хонаи мо',
    RU: '🌟 Добро пожаловать в наш дом! 🌟\n\n',
}
CONTACTS_TEXT = {
    TJ: 'Адреси мо: Шахри Душанбе\nТелефон: +992 987551165',
    RU: ('📞 Свяжитесь с нами для получения дополнительной информации и записи на курсы!\n\n'
         '<b>Телефон</b>: +992 987551165\n'
         '<b>Наш адрес</b>: г. Душанбе\n\n'
         '<b>Наши соц-сети</b> 👇'), }
ABOUT_COMPANY_TEXT = {
    TJ: 'Холо тексти точики нест.',
    RU: ('Здесть текст о компании'),
}

BUILDING_PARTS = {
    'block-a': {
        TJ: {'text': 'Информация дар блораи блок А',
             'button_text': 'Блок А' },
        RU: {'text': 'Информация о блоке А',
             'button_text': 'Блок А'},
        'default_photo': 'first_floor.jpg',
        'floors': {
            'floor-1': {
                TJ: {'text': 'Информация блоки А этажи 1',
                     'button_text': '1 этаж'},
                RU: {'text': 'Информация о блоке А этаж 1',
                     'button_text': '1 этаж'},
                'photo': 'first_floor.jpg'
            },
            'floor-2': {
                TJ: {'text': 'Информация блоки А этажи 2',
                     'button_text': '2 этаж'},
                RU: {'text': 'Информация о блоке А этаж 2',
                     'button_text': '2 этаж'},
                'photo': 'first_floor.jpg'
            }
        }
    },
    'block-b': {
        TJ: {'text': 'Информация дар блораи блок Б',
             'button_text': 'Блок Б'},
        RU: {'text': 'Информация о блоке Б',
             'button_text': 'Блок Б'},
        'default_photo': 'first_floor.jpg',
        'floors': {
            'floor-1': {
                TJ: {'text': 'Информация блоки Б этажи 1',
                     'button_text': '1 этаж'},
                RU: {'text': 'Информация о блоке Б этаж 1',
                     'button_text': '1 этаж'},
                'photo': 'first_floor.jpg'
            },
            'floor-2': {
                TJ: {'text': 'Информация блоки Б этажи 2',
                     'button_text': '2 этаж'},
                RU: {'text': 'Информация о блоке Б этаж 2',
                     'button_text': '2 этаж'},
                'photo': 'first_floor.jpg'
            }
        }
    },
    'block-c': {
        TJ: {'text': 'Информация дар бораи блок С',
             'button_text': 'Блок С'},
        RU: {'text': 'Информация о блоке С',
             'button_text': 'Блок С'},
        'default_photo': 'first_floor.jpg',
        'floors': {
            'floor-1': {
                TJ: {'text': 'Информация блоки С этажи 1',
                     'button_text': '1 этаж'},
                RU: {'text': 'Информация о блоке С этаж 1',
                     'button_text': '1 этаж'},
                'photo': 'first_floor.jpg'
            },
            'floor-2': {
                TJ: {'text': 'Информация блоки С этажи 2',
                     'button_text': '2 этаж'},
                RU: {'text': 'Информация о блоке С этаж 2',
                     'button_text': '2 этаж'},
                'photo': 'first_floor.jpg'
            }
        }
    },
}
