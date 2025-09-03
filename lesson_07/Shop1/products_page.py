# Импортируем класс By, который используется для указания типа локатора
# (например, поиск по CSS-селектору, XPATH, ID и т.д.)
from selenium.webdriver.common.by import By


class ProductsPage:
    # Конструктор класса — принимает драйвер браузера (webdriver)
    def __init__(self, driver):
        # Сохраняем переданный драйвер в атрибуте объекта для дальнейшего
        # использования
        self._driver = driver

    # Метод для добавления товаров в корзину
    def add_to_cart(self):
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
