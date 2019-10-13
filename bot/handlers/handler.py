# -*- coding: utf-8 -*-

import abc

from DB.DBAlchemy import DBManager
from markup.markup import Keyboards


class Handler(metaclass=abc.ABCMeta):
    """
    Абстрактный класс патерна Chain of responsibility
    """
    def __init__(self, bot):
        # получаем нашего бота
        self.bot = bot
        # инициализируем разметку кнопок в меню и экрана
        self.keyboards = Keyboards()
        # инициализация менеджера для работы с БД
        self.BD = DBManager()

    @abc.abstractmethod
    def handle(self):
        pass
