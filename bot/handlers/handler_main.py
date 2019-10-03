#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from markup.markup import Keyboards
from settings import config


class Handler:
    """ Класс обработчик событий для бота """
    def __init__(self, bot):
        # получаем нашего бота
        self.bot = bot
        # инициализируем разметку кнопок в меню и экрана
        self.keybords = Keyboards()

    def run_handlers(self):
        """ запускает все обработчики для бота в режиме 'прослушки'"""

        # обработчик(декоратор) сообщений,
        # который обрабатывает входящие /start и /help команды.
        @self.bot.message_handler(commands=['start'])
        def start_handler(message):
            self.bot.send_message(message.chat.id,
                                  message.from_user.first_name +
                                  ', здравствуйте! Жду дальнейших задач.',
                                  reply_markup=self.keybords.start_menu())

        # обработчик(декоратор) сообщений, который обрабатывает
        # входящие текстовые сообщения от нажатия кнопок.
        @self.bot.message_handler(func=lambda message: True)
        def echo_all(message):
            # если нажата кнопка Категории товара
            if message.text == config.KEYBOARD['CHOOSE_GOODS']:
                self.bot.send_message(message.chat.id,
                                      "Каталог категорий товара",
                                      reply_markup=self.keybords.remove_menu())
                self.bot.send_message(
                    message.chat.id,
                    "Сделайте свой выбор",
                    reply_markup=self.keybords.category_menu())

            # если нажата кнопка полуфабрикаты
            if message.text == config.KEYBOARD['SEMIPRODUCT']:
                self.bot.send_message(
                    message.chat.id,
                    'Категория ' + config.KEYBOARD['SEMIPRODUCT'],
                    reply_markup=self.keybords.set_select_category(
                        config.CATEGORY['SEMIPRODUCT']))
                self.bot.send_message(
                    message.chat.id,
                    "Ок",
                    reply_markup=self.keybords.category_menu())

            # если нажата кнопка бакалея
            if message.text == config.KEYBOARD['GROCERY']:
                self.bot.send_message(
                    message.chat.id,
                    'Категория ' + config.KEYBOARD['GROCERY'],
                    reply_markup=self.keybords.set_select_category(
                        config.CATEGORY['GROCERY']))
                self.bot.send_message(
                    message.chat.id,
                    "Ок",
                    reply_markup=self.keybords.category_menu())

            # если нажата кнопка мороженное
            if message.text == config.KEYBOARD['ICE_CREAM']:
                self.bot.send_message(
                    message.chat.id,
                    'Категория ' + config.KEYBOARD['ICE_CREAM'],
                    reply_markup=self.keybords.set_select_category(
                        config.CATEGORY['ICE_CREAM']))
                self.bot.send_message(
                    message.chat.id,
                    "Ок",
                    reply_markup=self.keybords.category_menu())
