# -*- coding: utf-8 -*-

from settings import config
from settings.message import MESSAGES
from .handler import Handler


class HandlerAllText(Handler):
    """
    Класс обрабатывает входящие текстовые сообщения от нажатия на кнопки

    """
    def __init__(self, bot):
        super(HandlerAllText, self).__init__(bot)

    def pressed_btn_category(self, message):
        """
        Обрабатывает входящие текстовые сообщения от нажатия на
        кнопку Выбрать товар.

        """
        self.bot.send_message(message.chat.id,
                              "Каталог категорий товара",
                              reply_markup=self.keyboards.remove_menu())
        self.bot.send_message(message.chat.id,
                              "Сделайте свой выбор",
                              reply_markup=self.keyboards.category_menu())

    def pressed_btn_product(self, message, product):
        """
        Обрабатывает входящие текстовые сообщения от нажатия на кнопоки
        каталога товаров.

        """
        self.bot.send_message(message.chat.id,
                              'Категория ' + config.KEYBOARD[product],
                              reply_markup=self.keyboards.set_select_category(
                                  config.CATEGORY[product]))
        self.bot.send_message(message.chat.id,
                              "Ок",
                              reply_markup=self.keyboards.category_menu())

    def pressed_btn_back(self, message):
        """
        обрабатывает входящие текстовые сообщения от нажатия на кнопку назад.
        """
        self.bot.send_message(message.chat.id,
                              "Вы вернулись назад",
                              reply_markup=self.keyboards.start_menu())

    def pressed_btn_order(self, message, code=1):
        """
        обрабатывает входящие текстовые сообщения от нажатия на кнопку заказв.
        """
        self.bot.send_message(message.chat.id, "Ваш заказ")
        self.bot.send_message(
            message.chat.id,
            MESSAGES['product_order'].format(
                self.BD.select_single_product_name(code),
                self.BD.select_single_product_title(code),
                self.BD.select_single_product_price(code),
                self.BD.select_single_product_quantity(code)),
            reply_markup=self.keyboards.orders_menu())

    def handle(self):
        # обработчик(декоратор) сообщений, который обрабатывает входящие
        # текстовые сообщения от нажатия кнопок.
        @self.bot.message_handler(func=lambda message: True)
        def handle(message):
            # *** меню (выбор категории, настройки, сведения) ***
            if message.text == config.KEYBOARD['CHOOSE_GOODS']:
                self.pressed_btn_category(message)
            # *** меню (категории товара, ПФ, Бакалея, Мороженое) ***
            if message.text == config.KEYBOARD['SEMIPRODUCT']:
                self.pressed_btn_product(message, 'SEMIPRODUCT')

            if message.text == config.KEYBOARD['GROCERY']:
                self.pressed_btn_product(message, 'GROCERY')

            if message.text == config.KEYBOARD['ICE_CREAM']:
                self.pressed_btn_product(message, 'ICE_CREAM')

            if message.text == config.KEYBOARD['ORDER']:
                self.pressed_btn_order(message)

            if message.text == config.KEYBOARD['BACK']:
                self.pressed_btn_back(message)

            # *** меню (Заказа) ***
