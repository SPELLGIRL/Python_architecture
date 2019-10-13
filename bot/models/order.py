# -*- coding: utf-8 -*-

# импортируем специальные поля Алхимии для инициализации полей таблицы
from sqlalchemy import Column, DateTime, Integer, ForeignKey
# импортируем модуль для связки таблиц
from sqlalchemy.orm import relationship, backref

# импортируем модуль инициализации декларативного класса Алхимии
from DB.dbcore import Base
# импортируем модель продуктов для связки моделей
from .product import Products


class Order(Base):
    """
    Класс Orders, основан на декларативном стиле sqlalchemy, нужен для оформления заказов
    """
    # Инициализация полей таблицы
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer)
    data = Column(DateTime)
    product_id = Column(Integer, ForeignKey('products.id'))
    user_id = Column(Integer)
    # используется cascade='delete,all' для каскадного удаления данных из
    # таблицы
    products = relationship(Products,
                            backref=backref('orders',
                                            uselist=True,
                                            cascade='delete,all'))

    def __repr__(self):
        """
        Метод возвращает формальное строковое представление указанного объекта
        """
        return "{} {}".format(self.quantity, self.data)
