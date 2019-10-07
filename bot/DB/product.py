# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, Integer, Float, Boolean, \
    ForeignKey
from sqlalchemy.orm import relationship, backref

from .category import Category
from .dbcore import Base


class Products(Base):
    """
    Класс для создания таблицы Products, основан на декларативном стиле
    sqlalchemy

    """
    # Инициализация полей таблицы
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    title = Column(String)
    price = Column(Float)
    quantity = Column(Integer)
    is_active = Column(Boolean)
    category_id = Column(Integer, ForeignKey('category.id'))
    # используется cascade='delete,all' для каскадного удаления данных из
    # таблицы
    category = relationship(Category,
                            backref=backref('products',
                                            uselist=True,
                                            cascade='delete,all'))

    def __repr__(self):
        """
        Метод возвращает формальное строковое представление указанного объекта

        """
        return "{} {} {}".format(self.name, self.title, self.price)
