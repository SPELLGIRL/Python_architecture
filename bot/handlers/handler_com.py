# -*- coding: utf-8 -*-

from .handler import Handler


class HandlerCommands(Handler):
    """
    Класс обрабатывает входящие команды /start и /help и т.п. ...
    """
    def __init__(self, bot):
        super(HandlerCommands, self).__init__(bot)

    def pressed_btn_start(self, message):
        """
        Обрабатывает входящие /start команды

        """
        self.bot.send_message(message.chat.id,
                              message.from_user.first_name +
                              ', здравствуйте! Жду дальнейших задач.',
                              reply_markup=self.keyboards.start_menu())

    def handle(self):
        # обработчик(декоратор) сообщений, который обрабатывает
        # входящие /start команды.
        @self.bot.message_handler(commands=['start'])
        def handle(message):
            if message.text == '/start':
                self.pressed_btn_start(message)
