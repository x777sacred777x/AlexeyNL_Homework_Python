# Импортируем класс By, который используется для указания типа локатора
# (например, поиск по CSS-селектору, XPATH, ID и т.д.)
from selenium.webdriver.common.by import By

# Импортируем allure для создания отчетов
import allure


class ProductsPage:
    """Класс для работы со страницей товаров."""

    def __init__(self, driver):
        """
        Инициализация страницы товаров.

        Args:
            driver: WebDriver для управления браузером
        """
        # Сохраняем переданный драйвер в атрибуте объекта для дальнейшего
        # использования
        self._driver = driver

    @allure.step("Добавление товаров в корзину")
    def add_to_cart(self) -> None:
        """Добавление товаров в корзину и переход в неё."""
        # Находим кнопку "Add to cart" для товара "Sauce Labs Backpack" и
        # кликаем по ней
        self._driver.find_element(By.CSS_SELECTOR,
                                  "#add-to-cart-sauce-labs-backpack").click()

        # Находим кнопку "Add to cart" для товара "Sauce Labs Bolt T-Shirt" и
        # кликаем по ней
        self._driver.find_element(
            By.CSS_SELECTOR,
            "#add-to-cart-sauce-labs-bolt-t-shirt").click()

        # Находим кнопку "Add to cart" для товара "Sauce Labs Onesie" и кликаем
        # по ней
        self._driver.find_element(
            By.CSS_SELECTOR,
            "#add-to-cart-sauce-labs-onesie").click()

        # Находим иконку корзины (ссылка с классом shopping_cart_link) и
        # переходим в корзину
        self._driver.find_element(
            By.CSS_SELECTOR,
            "a.shopping_cart_link").click()
