# -*- coding: utf-8 -*-

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, \
    ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

from DB.DBAlchemy import DBManager
from settings import config


class Keyboards:
    """ Класс Keyboards предназначен для создания и
    разметки клавиатуры бота

    """

    # инициализация разметки
    def __init__(self):
        self.markup = None
        # инициализация менеджера для работы с БД
        self.BD = DBManager()

    def set_btn(self, name):
        """ Создает и возвращает кнопку по входным параметрам """
        if name == "COUNT":
            config.KEYBOARD["COUNT"] = self.BD.count_rows_order()
        return KeyboardButton(config.KEYBOARD[name])

    @staticmethod
    def set_inline_btn(name):
        """ Создает и возвращает инлайн кнопку по входным параметрам """
        return InlineKeyboardButton(str(name), callback_data=str(name.id))

    @staticmethod
    def remove_menu():
        """ Удаляет данны кнопки и возвращает ее """
        return ReplyKeyboardRemove()

    def start_menu(self):
        """ Создает разметку кнопок в основном меню и возвращает разметку """
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_btn('CHOOSE_GOODS')
        itm_btn_2 = self.set_btn('INFO')
        itm_btn_3 = self.set_btn('SETTINGS')
        # рассположение кнопок в меню
        self.markup.row(itm_btn_1)
        self.markup.row(itm_btn_2, itm_btn_3)
        return self.markup

    def category_menu(self):
        """ Создает разметку кнопок в меню категорий товара и
        возвращает разметку

        """
        self.markup = ReplyKeyboardMarkup(True, True, row_width=1)
        self.markup.add(self.set_btn('SEMIPRODUCT'))
        self.markup.add(self.set_btn('GROCERY'))
        self.markup.add(self.set_btn('ICE_CREAM'))
        self.markup.row(self.set_btn('BACK'), self.set_btn('ORDER'))
        return self.markup

    def set_select_category(self, category):
        """ Создает разметку инлайн кнопок в выбранной категории товара и
        возвращает разметку

        """
        self.markup = InlineKeyboardMarkup(row_width=1)
        # загружаем в название инлайн кнопок данные с БД
        # в соответствие с категорией товара
        for item in self.BD.select_all_products_category(category):
            self.markup.add(self.set_inline_btn(item))

        return self.markup

    def orders_menu(self):
        """
        Создает разметку кнопок в заказе товара и возвращает разметку
        """
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_btn('X')
        itm_btn_2 = self.set_btn('DOWN')
        itm_btn_3 = self.set_btn('COUNT')
        itm_btn_4 = self.set_btn('UP')

        itm_btn_5 = self.set_btn('BACK')
        itm_btn_6 = self.set_btn('NEXT')
        itm_btn_7 = self.set_btn('APPLY')
        # рассположение кнопок в меню
        self.markup.row(itm_btn_1, itm_btn_2, itm_btn_3, itm_btn_4)
        self.markup.row(itm_btn_5, itm_btn_3, itm_btn_6)
        self.markup.row(itm_btn_7)

        return self.markup
