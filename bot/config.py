#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

TOKEN = 'здесь будет ваш токен'

NAME_DB = 'db.sqlite3'

# Base folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATABASE = os.path.join(BASE_DIR, NAME_DB)

# Keyboard buttons
KEYBOARD = {
    'CHOOSE_GOODS': '📚 Выбрать товар',
    'INFO': 'ℹ имя вашего бота',
    'SETTINGS': '⚙ Настройки',
    'SEMIPRODUCT': 'Полуфабрикаты',
    'GROCERY': 'Бакалея',
    'ICE_CREAM': 'Мороженое',
}
