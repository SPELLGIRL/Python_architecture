# -*- coding: utf-8 -*-

from .handler_all_text import HandlerAllText
from .handler_com import HandlerCommands
from .handler_inline_query import HandlerInlineQuery


class HandlerMain:
    """ Класс обработчик событий для бота """
    def __init__(self, bot):
        # получаем нашего бота
        self.bot = bot
        # инициализируем обработчики
        self.handler_commands = HandlerCommands(self.bot)
        self.handler_all_text = HandlerAllText(self.bot)
        self.handler_inline_query = HandlerInlineQuery(self.bot)

    def handle(self):
        """
        Запускает все обработчики бота
        """
        self.handler_commands.handle()
        self.handler_all_text.handle()
        self.handler_inline_query.handle()
