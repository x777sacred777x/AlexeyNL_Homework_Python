# Импортируем класс By, который используется для указания типа локатора
# (например, поиск по CSS-селектору, XPATH, ID и т.д.)
from selenium.webdriver.common.by import By

# Импортируем allure для создания отчетов
import allure


class YouCart:
    """Класс для работы с корзиной покупок."""

    def __init__(self, driver):
        """
        Инициализация корзины.

        Args:
            driver: WebDriver для управления браузером
        """
        # Сохраняем переданный драйвер в атрибуте объекта для дальнейшего
        # использования
        self._driver = driver

    @allure.step("Переход к оформлению заказа")
    def checkout(self) -> None:
        """Переход к оформлению заказа."""
        # Находим кнопку "Checkout" по CSS-селектору "#checkout" и кликаем по
        # ней
        self._driver.find_element(By.CSS_SELECTOR, "#checkout").click()
