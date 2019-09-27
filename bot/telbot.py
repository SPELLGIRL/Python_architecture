#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import telebot
from telebot import types
import config
from handlers import Handler


class TelBot:

    def __init__(self):
        self.token = config.TOKEN
        self.bot = telebot.TeleBot(self.token)
        self.handler = Handler(self.bot)

    def render_markup(self):
        pass

    def render(self):
        pass

    def start(self):
        self.handler.run_handlers()

    def run_bot(self):
        self.start()
        self.bot.polling(none_stop=True)


if __name__ == '__main__':
    bot = TelBot()
    bot.run_bot()
