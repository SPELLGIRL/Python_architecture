#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .DB import Category, Products
from .dbcore import Base
from settings import config


class Singleton(type):
    """ Патерн Singleton предоставляет механизм создания одного и
    только один экземпляра объекта, и предоставление к нему
    глобальную точку доступа.

    """
    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls.__instance = None

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class DBManager(metaclass=Singleton):
    """ Класс менеджер для работы с БД """
    def __init__(self):
        """ Инициализация сесии и подключения к БД """
        self.engine = create_engine(config.DATABASE)
        session = sessionmaker(bind=self.engine)
        self._session = session()
        Base.metadata.create_all(self.engine)

    def set_tabs(self):
        """ Метод заполнения полей таблицы Тест """

        category_1 = Category(name='Полуфабрикаты', is_active=True)
        category_2 = Category(name='Бакалея', is_active=True)
        category_3 = Category(name='Мороженое', is_active=True)

        product_1 = Products(name='Вареники(Фирменные)',
                             title='ТМ Геркулес 400 гр',
                             price=542.01,
                             quantity=12,
                             is_active=True,
                             category=category_1)
        product_2 = Products(name='Пельмени(Домашние)',
                             title='ТМ Вкуснотеево 450 гр',
                             price=322.5,
                             quantity=23,
                             is_active=True,
                             category=category_1)
        product_3 = Products(name='Колбаса(Докторская)',
                             title='ТМ Доброе 500 гр',
                             price=420,
                             quantity=15,
                             is_active=True,
                             category=category_2)
        product_4 = Products(name='Сосиски(Молочные)',
                             title='ТМ Веселые 700 гр',
                             price=312.56,
                             quantity=36,
                             is_active=True,
                             category=category_2)
        product_5 = Products(name='Пьяная вишня',
                             title='ТМ Молочный берег 50 гр',
                             price=75,
                             quantity=102,
                             is_active=True,
                             category=category_3)
        product_6 = Products(name='Пломбир класический',
                             title='ТМ Молочный берег 100 гр',
                             price=80,
                             quantity=12,
                             is_active=True,
                             category=category_3)

        self._session.add_all([category_1, category_2, category_3])
        self._session.add_all(
            [product_1, product_2, product_3, product_4, product_5, product_6])

        self._session.commit()

    def select_single_product(self, rownum):
        """ Возвращает одну строку товара с номером rownum """

        return self._session.query(Products).filter_by(id=rownum).all()

    def select_all_products(self):
        """ Возвращает все строки товаров """

        return self._session.query(Products).all()

    def select_all_products_category(self, category):
        """ Возвращает все строки товара категории """

        return self._session.query(Products).filter_by(
            category_id=category).all()

    def select_all_id_category(self):
        """ Возвращает все строки товара категории """

        return self._session.query(Category.id).all()

    def select_count_products_category(self, category):
        """ Возвращает количество всех строк товара категории """

        return self._session.query(Products).filter_by(
            category_id=category).count()

    def count_rows_products(self):
        """ Возвращает количество строк товара """

        return self._session.query(Products).count()

    def update_product_value(self, rownum, name, value):
        """ Обновляет данные указанной строки товара """

        self._session.query(Products).filter_by(id=rownum).update(
            {name: value})
        self._session.commit()

    def delete_product(self, rownum):
        """ Удаляет данные указанной строки товара """
        self._session.query(Products).filter_by(id=rownum).delete()
        self._session.commit()

    def close(self):
        """ Закрывает сесию """
        self._session.close()
