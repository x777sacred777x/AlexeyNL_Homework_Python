# Импортируем стандартный модуль для работы с переменными окружения
import os

# Импортируем библиотеку для выполнения HTTP-запросов
import requests


# Класс для работы с API проектов Yougile
class ProjectsAPI:
    def __init__(self):
        # Базовый URL для всех запросов к API
        self.BASE_URL = "https://ru.yougile.com/api-v2"

        # Получаем токен API из переменной окружения
        self.API_TOKEN = os.getenv("YOUGILE_API_TOKEN")

        # Если токен не найден — выбрасываем исключение с понятным сообщением
        if not self.API_TOKEN:
            raise ValueError("Не найден токен API. Установите переменную окружения YOUGILE_API_TOKEN.")

        # Заголовки, которые будут отправляться с каждым запросом
        self.headers = {
            "Authorization": f"Bearer {self.API_TOKEN}",  # Авторизация через Bearer-токен
            "Content-Type": "application/json"            # Указываем, что тело запроса — это JSON
        }

    # Метод для создания нового проекта
    def create_project(self, payload):
        # Отправляем POST-запрос с данными проекта
        return requests.post(f"{self.BASE_URL}/projects", json=payload, headers=self.headers)

    # Метод для получения списка всех проектов
    def get_all_projects(self):
        # Отправляем GET-запрос без тела, только с заголовками
        return requests.get(f"{self.BASE_URL}/projects", headers=self.headers)

    # Метод для получения информации о конкретном проекте по его ID
    def get_project_by_id(self, project_id):
        # Формируем URL с ID проекта и отправляем GET-запрос
        return requests.get(f"{self.BASE_URL}/projects/{project_id}", headers=self.headers)

    # Метод для обновления проекта по ID
    def update_project(self, project_id, payload):
        # Отправляем PUT-запрос с обновлёнными данными проекта
        return requests.put(f"{self.BASE_URL}/projects/{project_id}", json=payload, headers=self.headers)
