# -*- coding: utf-8 -*-

import json
import os

from emoji import emojize

# название БД
NAME_DB = 'db.sqlite3'
# версия приложения
VERSION = '0.3'
# автор приложения
AUTHOR = 'SPELLGIRL'
# название приложения
APP_NAME = 'SpellStore'
# Base folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# DB folder
DB_DIR = os.path.join(BASE_DIR, 'DB')
# Path to DB
DATABASE = os.path.join('sqlite:///' + DB_DIR, NAME_DB)

COUNT = 0

with open(os.path.join(BASE_DIR, 'secrets.json')) as secrets_file:
    secrets = json.load(secrets_file)


def get_secret(setting, secrets_in=secrets):
    """Get secret setting or fail with ValueError"""
    try:
        return secrets_in[setting]
    except KeyError:
        raise ValueError(f'Set the {setting} setting')


TOKEN = get_secret('TOKEN')

PROXY = get_secret('PROXY')

# Keyboard buttons
KEYBOARD = {
    'CHOOSE_GOODS': emojize(':open_file_folder: Выбрать товар'),
    'INFO': emojize(':speech_balloon: TradingStore'),
    'SETTINGS': emojize(':globe_with_meridians: Настройки'),
    'SEMIPRODUCT': emojize(':pizza: Полуфабрикаты'),
    'GROCERY': emojize(':bread: Бакалея'),
    'ICE_CREAM': emojize(':shaved_ice: Мороженое'),
    '<<': emojize('⏪'),
    '>>': emojize('⏩'),
    'BACK_STEP': emojize('◀️'),
    'NEXT_STEP': emojize('▶️'),
    'ORDER': emojize(':heavy_check_mark: ЗАКАЗ'),
    'X': emojize('❌'),
    'DOWN': emojize('🔽'),
    'AMOUNT_PRODUCT': COUNT,
    'AMOUNT_ORDERS': COUNT,
    'UP': emojize('🔼'),
    'APPLY': '✅ Оформить заказ',
    'COPY': '©️',
}

# Id category to products
CATEGORY = {
    'SEMIPRODUCT': 1,
    'GROCERY': 2,
    'ICE_CREAM': 3,
}

# name commands
COMMANDS = {
    'START': "start",
    'HELP': "help",
}
