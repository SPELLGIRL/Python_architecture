#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import telebot

from handlers.handler_main import HandlerMain
from settings import config


class TelBot:
    """Основной класс телеграмм бота(Сервер), в основе которого
    используется библиотека pyTelegramBotAPI

    """

    __version__ = '0.1a'
    __author__ = 'SPELLGIRL'

    def __init__(self):
        """Инициализация бота(Сервера)"""
        # Установка прокси для бота
        telebot.apihelper.proxy = {'https': config.PROXY}
        # Получение токена
        self.token = config.TOKEN
        # Инициализация бота на основе зарегистрированного токена
        self.bot = telebot.TeleBot(self.token)
        # Инициализация оброботчика событий
        self.handler = HandlerMain(self.bot)

    def start(self):
        """Метод предназначен для старта обработчика событий"""
        self.handler.handle()

    def run_bot(self):
        """Метод запускает основные события сервера"""
        # обработчика событий
        self.start()
        # служит для запуска бота (работа в режиме нон-стоп)
        self.bot.polling(none_stop=True)


if __name__ == '__main__':
    bot = TelBot()
    bot.run_bot()
