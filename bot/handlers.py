#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import config
from markup import Keyboards
from dblighter import DbLighter
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


class Handler:
    def __init__(self, bot):
        self.bot = bot
        self.keybords = Keyboards()
        self.BD = DbLighter(config.DATABASE)
        self.row = self.BD.select_single(3)

    def set_str(self):
        st = ''
        for s in self.row:
            st += '  ' + str(s)

        return st

    def run_handlers(self):

        @self.bot.message_handler(commands=['start'])
        def start_handler(message):
            self.bot.send_message(
                message.chat.id,
                message.from_user.first_name +
                ', здравствуйте! Жду дальнейших задач.',
                reply_markup=self.keybords.start_menu())

        @self.bot.message_handler(func=lambda message: True)
        def echo_all(message):
            if message.text == config.KEYBOARD['CHOOSE_GOODS']:
                self.bot.send_message(message.chat.id,
                                      "Каталог категорий товара",
                                      reply_markup=self.keybords.remove_menu())
                self.bot.send_message(message.chat.id, "Сделайте свой выбор",
                                      reply_markup=self.keybords.category_menu())

            if message.text == config.KEYBOARD['SEMIPRODUCT']:
                self.bot.send_message(message.chat.id, self.set_str(),
                                      reply_markup=self.keybords.category_menu())

            if message.text == config.KEYBOARD['GROCERY']:
                self.bot.send_message(message.chat.id, self.set_str(),
                                      reply_markup=self.keybords.category_menu_in())

            if message.text == config.KEYBOARD['ICE_CREAM']:
                self.bot.send_message(message.chat.id, "Мороженое",
                                      reply_markup=self.keybords.category_menu())
