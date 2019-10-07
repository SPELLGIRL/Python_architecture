# -*- coding: utf-8 -*-

from settings import config
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

    def handle(self):
        # обработчик(декоратор) сообщений, который обрабатывает входящие
        # текстовые сообщения от нажатия кнопок.
        @self.bot.message_handler(func=lambda message: True)
        def handle(message):
            if message.text == config.KEYBOARD['CHOOSE_GOODS']:
                self.pressed_btn_category(message)

            if message.text == config.KEYBOARD['SEMIPRODUCT']:
                self.pressed_btn_product(message, 'SEMIPRODUCT')

            if message.text == config.KEYBOARD['GROCERY']:
                self.pressed_btn_product(message, 'GROCERY')

            if message.text == config.KEYBOARD['ICE_CREAM']:
                self.pressed_btn_product(message, 'ICE_CREAM')
