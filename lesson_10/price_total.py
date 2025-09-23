# Импортируем класс By, который используется для указания типа локатора
# (например, поиск по CSS-селектору, XPATH, ID и т.д.)
from selenium.webdriver.common.by import By

# Импортируем allure для создания отчетов
import allure


class PriceTotal:
    """Класс для работы с итоговой суммой заказа."""

    def __init__(self, driver):
        """
        Инициализация страницы итоговой суммы.

        Args:
            driver: WebDriver для управления браузером
        """
        # Сохраняем переданный драйвер в атрибуте объекта для дальнейшего
        # использования
        self._driver = driver

    @allure.step("Получение итоговой суммы заказа")
    def checkout_price(self) -> str:
        """
        Получение итоговой суммы заказа.

        Returns:
            str: Текст итоговой суммы
        """
        # Находим элемент с итоговой суммой
        # по CSS-селектору "div.summary_total_label"
        # и получаем его текстовое содержимое
        total = self._driver.find_element(
            By.CSS_SELECTOR, "div.summary_total_label").text

        # Выводим итоговую сумму в консоль (для отладки или логирования)
        print(total)

        # Возвращаем итоговую сумму, чтобы можно было использовать её в тестах
        # или других методах
        return total

    @allure.step("Закрытие браузера")
    def close_browser(self) -> None:
        """Закрытие браузера."""
        # Завершаем работу драйвера и закрываем все окна браузера
        self._driver.quit()
