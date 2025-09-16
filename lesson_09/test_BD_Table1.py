from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lesson_09.BD_Table1 import Users  # Импорт модели таблицы Users

# Строка подключения к базе данных PostgreSQL
db_connection_string = "postgresql://postgres:123@localhost:5432/postgres"

# Вспомогательная функция для создания сессии


def get_session():
    engine = create_engine(db_connection_string)
    Session = sessionmaker(bind=engine)
    return Session()

# 🧪 Тест добавления пользователя


def test_add_user():
    new_user_id = 777
    new_user_email = 'user1@mail.ru'
    user_subject_id = 1

    sess = get_session()
    try:
        # Создание нового пользователя
        new_user = Users(
            user_id=new_user_id,
            user_email=new_user_email,
            subject_id=user_subject_id
        )
        sess.add(new_user)
        sess.commit()

        # Проверка, что пользователь добавлен
        result = sess.query(Users).filter(Users.user_id == new_user_id).first()
        assert result is not None, "Пользователь не найден."

        # Проверка данных
        assert result.user_id == new_user_id
        assert result.user_email == new_user_email
        assert result.subject_id == user_subject_id

    finally:
        # Очистка тестовых данных
        sess.query(Users).filter(Users.user_id == new_user_id).delete()
        sess.commit()
        sess.close()

# 🧪 Тест обновления пользователя


def test_update_user():
    new_user_id = 777
    new_user_email = 'user2@mail.ru'
    user_subject_id = 3
    update_email = 'Update@mail.ru'

    sess = get_session()
    try:
        # Добавление пользователя
        new_user = Users(
            user_id=new_user_id,
            user_email=new_user_email,
            subject_id=user_subject_id
        )
        sess.add(new_user)
        sess.commit()

        # Обновление email
        sess.query(Users).filter(Users.user_id == new_user_id).update({
            Users.user_email: update_email
        })
        sess.commit()

        # Проверка обновления
        result = sess.query(Users).filter(Users.user_id == new_user_id).first()
        assert result is not None, "Пользователь не найден."
        assert result.user_email == update_email
        assert result.subject_id == user_subject_id

    finally:
        # Очистка
        sess.query(Users).filter(Users.user_id == new_user_id).delete()
        sess.commit()
        sess.close()

# 🧪 Тест удаления пользователя


def test_delete_user():
    new_user_id = 888
    new_user_email = 'user3@mail.ru'
    user_subject_id = 2

    sess = get_session()
    try:
        # Добавление пользователя
        new_user = Users(
            user_id=new_user_id,
            user_email=new_user_email,
            subject_id=user_subject_id
        )
        sess.add(new_user)
        sess.commit()

        # Удаление пользователя
        sess.query(Users).filter(Users.user_id == new_user_id).delete()
        sess.commit()

        # Проверка, что пользователь удалён
        result = sess.query(Users).filter(Users.user_id == new_user_id).all()
        assert len(result) == 0, "Пользователь не был удалён."

    finally:
        sess.close()
