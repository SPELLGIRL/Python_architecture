#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, \
    ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import config


class Keyboards:
    def __init__(self):
        self.markup = None

    def set_btn(self, name):
        return KeyboardButton(config.KEYBOARD[name])

    def set_inline_btn(self, name):
        return InlineKeyboardButton(config.KEYBOARD[name],
                                    callback_data=config.KEYBOARD[name])

    def remove_menu(self):
        return ReplyKeyboardRemove()

    def start_menu(self):
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_btn('CHOOSE_GOODS')
        itm_btn_2 = self.set_btn('INFO')
        itm_btn_3 = self.set_btn('SETTINGS')
        self.markup.row(itm_btn_1)
        self.markup.row(itm_btn_2, itm_btn_3)
        return self.markup

    def category_menu(self):
        self.markup = ReplyKeyboardMarkup(row_width=1)
        self.markup.add(self.set_btn('SEMIPRODUCT'))
        self.markup.add(self.set_btn('GROCERY'))
        self.markup.add(self.set_btn('ICE_CREAM'))
        return self.markup

    def category_menu_in(self):
        self.markup = InlineKeyboardMarkup(row_width=2)
        self.markup.add(self.set_inline_btn('SEMIPRODUCT'))
        return self.markup
