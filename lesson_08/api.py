# Импортируем библиотеку для выполнения HTTP-запросов
import requests


# Класс для работы с API проектов Yougile
class ProjectsAPI:

    def __init__(self):
        # Базовый URL для всех запросов к API
        self.BASE_URL = "https://ru.yougile.com/api-v2"

        # Токен авторизации для доступа к API
        self.API_TOKEN = "M490+1etfzdgHHlO9ki9fRvxNsukLmHjJRCjtfSHW+-Cmdzqra6QHBx8Xji-RXal"

        # Заголовки, включающие авторизацию и формат данных
        self.headers = {
            # Авторизация через Bearer-токен
            "Authorization": f"Bearer {self.API_TOKEN}",
            # Указываем, что данные передаются в формате JSON
            "Content-Type": "application/json"
        }

    def create_project(self, payload):
        """Создать новый проект."""
        url = f"{self.BASE_URL}/projects"  # Формируем URL для создания проекта
        # Отправляем POST-запрос с данными проекта
        return requests.post(url, json=payload, headers=self.headers)

    def get_all_projects(self):
        """Получить список всех проектов."""
        url = f"{self.BASE_URL}/projects"  # URL для получения всех проектов
        # Отправляем GET-запрос
        return requests.get(url, headers=self.headers)

    def get_project_by_id(self, project_id):
        """Получить конкретный проект по его ID."""
        url = f"{self.BASE_URL}/projects/{project_id}"  # URL с ID проекта
        # Отправляем GET-запрос для получения информации о проекте
        return requests.get(url, headers=self.headers)

    def update_project(self, project_id, payload):
        """Обновить данные проекта по его ID."""
        url = f"{
            self.BASE_URL}/projects/{project_id}"  # URL для обновления проекта
        # Отправляем PUT-запрос с новыми данными
        return requests.put(url, json=payload, headers=self.headers)
