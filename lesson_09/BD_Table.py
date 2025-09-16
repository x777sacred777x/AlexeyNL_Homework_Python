# Импорт базового класса для декларативного описания моделей
from sqlalchemy.ext.declarative import declarative_base

# Импорт типов столбцов
from sqlalchemy import Column, Integer, String

# Создание базового класса для всех ORM-моделей
# Все модели должны наследоваться от Base, чтобы SQLAlchemy мог их отслеживать
Base = declarative_base()


# Описание модели Users, которая соответствует таблице 'users' в базе данных
class Users(Base):
    # Указываем имя таблицы, с которой будет связана модель
    __tablename__ = 'users'

    # Описание столбцов таблицы:

    # user_id — первичный ключ, уникальный идентификатор пользователя
    user_id = Column(Integer, primary_key=True)

    # user_email — строковое поле для хранения email пользователя
    user_email = Column(String)

    # subject_id — целочисленное поле ссылается на другую таблицу 'subject'
    subject_id = Column(Integer)

    # Метод строкового представления объекта
    def __str__(self):
        return f'user_id : {
            self.user_id}\tuser_email : {
            self.user_email}\tsubject_id : {
            self.subject_id}'
