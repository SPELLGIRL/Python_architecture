# -*- coding: utf-8 -*-

# импортируем настройки и утилиты
from settings import config
from settings import utility
# импортируем ответ пользователю
from settings.message import MESSAGES
# импортируем класс родитель
from .handler import Handler


class HandlerAllText(Handler):
    """
    Класс обрабатывает входящие текстовые сообщения от нажатия на кнопки

    """
    def __init__(self, bot):
        super(HandlerAllText, self).__init__(bot)
        # шаг в заказе
        self.step = 0

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

    def pressed_btn_info(self, message):
        """
        Обрабатывает входящие текстовые сообщения от нажатия на кнопку
        TradingStore.

        """
        self.bot.send_message(message.chat.id,
                              MESSAGES['trading_store'],
                              parse_mode="HTML",
                              reply_markup=self.keyboards.info_menu())

    def pressed_btn_settings(self, message):
        """
        Обрабатывает входящие текстовые сообщения от нажатия на кнопку
        settings.

        """
        self.bot.send_message(message.chat.id,
                              MESSAGES['settings'],
                              parse_mode="HTML",
                              reply_markup=self.keyboards.settings_menu())

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

    def pressed_btn_order(self, message):
        """
        Обрабатывает входящие текстовые сообщения от нажатия на кнопку заказов.
        """
        # обнуляем данные шага
        self.step = 0
        # получаем список всех товаров в заказе
        count = self.BD.select_all_product_id()
        # получаем количество в каждой позиции товара в заказе
        quantity = self.BD.select_order_quantity(count[self.step])
        # отправляем ответ пользователю
        self.send_message_order(count[self.step], quantity, message)

    def pressed_btn_back_step(self, message):
        """
        Обрабатывает входящие текстовые сообщения от нажатия на кнопку
        back_step.
        """
        # уменьшаем шаг пока шаг не будет равет "0"
        if self.step > 0:
            self.step -= 1
        # получаем список всех товаров в заказе
        count = self.BD.select_all_product_id()
        quantity = self.BD.select_order_quantity(count[self.step])

        # отправляем ответ пользователю
        self.send_message_order(count[self.step], quantity, message)

    def pressed_btn_next_step(self, message):
        """
        Обрабатывает входящие текстовые сообщения от нажатия на кнопку
        next_step.
        """
        # увеличиваем шаг пока шаг не будет равет количеству строк полей
        # заказа с расчетом цены деления начиная с "0"
        if self.step < self.BD.count_rows_order() - 1:
            self.step += 1
        # получаем список всех товаров в заказе
        count = self.BD.select_all_product_id()
        # получаем еоличество конкретного товара в соответствие с шагом выборки
        quantity = self.BD.select_order_quantity(count[self.step])

        # отправляем ответ пользователю
        self.send_message_order(count[self.step], quantity, message)

    def pressed_btn_down(self, message):
        """
        обрабатывает входящие текстовые сообщения от нажатия на кнопку douwn.
        """
        # получаем список всех товаров в заказе
        count = self.BD.select_all_product_id()
        # получаем количество конкретной позиции в заказе
        quantity_order = self.BD.select_order_quantity(count[self.step])
        # получаем количество конкретной позиции в пролуктов
        quantity_product = self.BD.select_single_product_quantity(
            count[self.step])
        # если товар в заказе есть
        if quantity_order > 0:
            quantity_order -= 1
            quantity_product += 1
            # вносим изменения в БД orders
            self.BD.update_order_value(count[self.step], 'quantity',
                                       quantity_order)
            # вносим изменения в БД product
            self.BD.update_product_value(count[self.step], 'quantity',
                                         quantity_product)
        # отправляем ответ пользователю
        self.send_message_order(count[self.step], quantity_order, message)

    def pressed_btn_up(self, message):
        """
        обрабатывает входящие текстовые сообщения от нажатия на кнопку up.
        """
        # получаем список всех товаров в заказе
        count = self.BD.select_all_product_id()
        # получаем количество конкретной позиции в заказе
        quantity_order = self.BD.select_order_quantity(count[self.step])
        # получаем количество конкретной позиции в пролуктов
        quantity_product = self.BD.select_single_product_quantity(
            count[self.step])
        # если товар есть
        if quantity_product > 0:
            quantity_order += 1
            quantity_product -= 1
            # вносим изменения в БД orders
            self.BD.update_order_value(count[self.step], 'quantity',
                                       quantity_order)
            # вносим изменения в БД product
            self.BD.update_product_value(count[self.step], 'quantity',
                                         quantity_product)
        # отправляем ответ пользователю
        self.send_message_order(count[self.step], quantity_order, message)

    def pressed_btn_x(self, message):
        """
        Обрабатывает входящие текстовые сообщения от нажатия на кнопку x
        удалить позицию шага.
        """
        # получаем список всех product_id заказа
        count = self.BD.select_all_product_id()
        # если список не пуст
        if count.__len__() > 0:
            # получаем количество конкретной позиции в заказе
            quantity_order = self.BD.select_order_quantity(count[self.step])
            # получаем количество товара к конкретной позиции заказа для
            # возврата в product
            quantity_product = self.BD.select_single_product_quantity(
                count[self.step])
            quantity_product += quantity_order
            # вносим изменения в БД orders
            self.BD.delete_order(count[self.step])
            # вносим изменения в БД product
            self.BD.update_product_value(count[self.step], 'quantity',
                                         quantity_product)
            # уменьшаем шаг
            self.step -= 1

        count = self.BD.select_all_product_id()
        # если список не пуст
        if count.__len__() > 0:

            quantity_order = self.BD.select_order_quantity(count[self.step])
            # отправляем пользователю сообщение
            self.send_message_order(count[self.step], quantity_order, message)

        else:
            # если товара нет в заказе отправляем сообщение
            self.bot.send_message(message.chat.id,
                                  MESSAGES['no_orders'],
                                  parse_mode="HTML",
                                  reply_markup=self.keyboards.category_menu())

    def pressed_btn_apllay(self, message):
        """
        обрабатывает входящие текстовые сообщения от нажатия на кнопку apllay.
        """
        # отправляем ответ пользователю
        self.bot.send_message(message.chat.id,
                              MESSAGES['apply'].format(
                                  utility.get_total_cost(self.BD),
                                  utility.get_total_quantity(self.BD)),
                              parse_mode="HTML",
                              reply_markup=self.keyboards.category_menu())
        # отчищаем данные с заказа
        self.BD.delete_all_order()

    def send_message_order(self, product_id, quantity, message):
        """
        отправляет ответ пользователю при выполнении различных действий
        """
        self.bot.send_message(message.chat.id,
                              MESSAGES['order_number'].format(self.step + 1),
                              parse_mode="HTML")
        self.bot.send_message(
            message.chat.id,
            MESSAGES['order'].format(
                self.BD.select_single_product_name(product_id),
                self.BD.select_single_product_title(product_id),
                self.BD.select_single_product_price(product_id),
                self.BD.select_order_quantity(product_id)),
            parse_mode="HTML",
            reply_markup=self.keyboards.orders_menu(self.step, quantity))

    def handle(self):
        # обработчик(декоратор) сообщений, который обрабатывает входящие
        # текстовые сообщения от нажатия кнопок.
        @self.bot.message_handler(func=lambda message: True)
        def handle(message):
            # *** меню (выбор категории, настройки, сведения) ***
            if message.text == config.KEYBOARD['CHOOSE_GOODS']:
                self.pressed_btn_category(message)

            if message.text == config.KEYBOARD['INFO']:
                self.pressed_btn_info(message)

            if message.text == config.KEYBOARD['SETTINGS']:
                self.pressed_btn_settings(message)

            # *** меню (категории товара, ПФ, Бакалея, Мороженое) ***
            if message.text == config.KEYBOARD['SEMIPRODUCT']:
                self.pressed_btn_product(message, 'SEMIPRODUCT')

            if message.text == config.KEYBOARD['GROCERY']:
                self.pressed_btn_product(message, 'GROCERY')

            if message.text == config.KEYBOARD['ICE_CREAM']:
                self.pressed_btn_product(message, 'ICE_CREAM')

            if message.text == config.KEYBOARD['ORDER']:
                # если есть заказ
                if self.BD.count_rows_order() > 0:
                    self.pressed_btn_order(message)
                else:
                    self.bot.send_message(
                        message.chat.id,
                        MESSAGES['no_orders'],
                        parse_mode="HTML",
                        reply_markup=self.keyboards.category_menu())
            if message.text == config.KEYBOARD['<<']:
                self.pressed_btn_back(message)

            # *** меню (Заказа) ***
            if message.text == config.KEYBOARD['BACK_STEP']:
                self.pressed_btn_back_step(message)

            if message.text == config.KEYBOARD['NEXT_STEP']:
                self.pressed_btn_next_step(message)

            if message.text == config.KEYBOARD['DOWN']:
                self.pressed_btn_down(message)

            if message.text == config.KEYBOARD['UP']:
                self.pressed_btn_up(message)

            if message.text == config.KEYBOARD['X']:
                self.pressed_btn_x(message)

            if message.text == config.KEYBOARD['APPLY']:
                self.pressed_btn_apllay(message)
                # иные нажатия и ввод данных пользователем
            else:
                self.bot.send_message(message.chat.id, message.text)
