# -*- coding: utf-8 -*-

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, \
    ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

from DB.DBAlchemy import DBManager
from settings import config
from settings import utility


class Keyboards:
    """ Класс Keyboards предназначен для создания и
    разметки клавиатуры бота

    """

    # инициализация разметки
    def __init__(self):
        self.markup = None
        # инициализация менеджера для работы с БД
        self.BD = DBManager()

    def set_btn(self, name, step=0, quantity=0):
        """ Создает и возвращает кнопку по входным параметрам """
        if name == "AMOUNT_ORDERS":
            config.KEYBOARD["AMOUNT_ORDERS"] = "{} {} {}".format(
                step + 1, ' из ', str(self.BD.count_rows_order()))

        if name == "AMOUNT_PRODUCT":
            config.KEYBOARD["AMOUNT_PRODUCT"] = "{}".format(quantity)

        if name == "APPLY":
            # создает кнопку оформить с данными о стоимости товара
            # округленного до 2 - го знака после запятой
            config.KEYBOARD["APPLY"] = "{}({}) руб".format(
                '✅ Оформить', round(utility.get_total_cost(self.BD), 2))

        return KeyboardButton(config.KEYBOARD[name])

    @staticmethod
    def set_inline_btn(name):
        """ Создает и возвращает инлайн кнопку по входным параметрам """
        return InlineKeyboardButton(str(name), callback_data=str(name.id))

    @staticmethod
    def remove_menu():
        """ Удаляет данны кнопки и возвращает ее """
        return ReplyKeyboardRemove()

    def info_menu(self):
        """
        Создает разметку кнопок в меню info
        """
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_btn('<<')
        # расположение кнопок в меню
        self.markup.row(itm_btn_1)
        return self.markup

    def settings_menu(self):
        """
        Создает разметку кнопок в меню settings
        """
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_btn('<<')
        # расположение кнопок в меню
        self.markup.row(itm_btn_1)
        return self.markup

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
        self.markup.row(self.set_btn('<<'), self.set_btn('ORDER'))
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

    def orders_menu(self, step, quantity):
        """
        Создает разметку кнопок в заказе товара и возвращает разметку
        """
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_btn('X', step, quantity)
        itm_btn_2 = self.set_btn('DOWN', step, quantity)
        itm_btn_3 = self.set_btn('AMOUNT_PRODUCT', step, quantity)
        itm_btn_4 = self.set_btn('UP', step, quantity)

        itm_btn_5 = self.set_btn('BACK_STEP', step, quantity)
        itm_btn_6 = self.set_btn('AMOUNT_ORDERS', step, quantity)
        itm_btn_7 = self.set_btn('NEXT_STEP', step, quantity)
        itm_btn_8 = self.set_btn('APPLY', step, quantity)
        itm_btn_9 = self.set_btn('<<', step, quantity)
        # рассположение кнопок в меню
        self.markup.row(itm_btn_1, itm_btn_2, itm_btn_3, itm_btn_4)
        self.markup.row(itm_btn_5, itm_btn_6, itm_btn_7)
        self.markup.row(itm_btn_9, itm_btn_8)

        return self.markup
