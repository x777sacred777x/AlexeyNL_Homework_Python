# Импортируем библиотеку pytest для написания тестов
import pytest

# Импортируем класс ProjectsAPI из модуля api
from api import ProjectsAPI


# Фикстура, создающая экземпляр API-клиента один раз за сессию тестов
@pytest.fixture(scope="session")
def api():
    """Инициализация API клиента с токеном из переменных окружения."""
    # Возвращаем экземпляр класса ProjectsAPI, который будет использоваться в
    # тестах
    return ProjectsAPI()


# Фикстура, предоставляющая корректные данные для создания проекта
@pytest.fixture
def valid_project_payload():
    """Корректные данные для создания проекта."""
    # Возвращаем словарь с обязательными полями: name и description
    return {"name": "Test Project", "description": "This is a test project"}


# Фикстура, предоставляющая некорректные данные (например, без поля name)
@pytest.fixture
def invalid_project_payload():
    """Некорректные данные (отсутствие обязательных полей)."""
    # Возвращаем словарь, в котором отсутствует обязательное поле name
    return {"description": "Missing required fields"}
