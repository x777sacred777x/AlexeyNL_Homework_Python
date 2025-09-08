# Импортируем класс By, который используется для указания типа локатора
# (например, поиск по CSS-селектору, XPATH, ID и т.д.)
from selenium.webdriver.common.by import By


class YouCart:
    # Конструктор класса — принимает драйвер браузера (webdriver)
    def __init__(self, driver):
        # Сохраняем переданный драйвер в атрибуте объекта для дальнейшего
        # использования
        self._driver = driver

    # Метод для перехода к оформлению заказа
    def checkout(self):
        # Находим кнопку "Checkout" по CSS-селектору "#checkout" и кликаем по
        # ней
        self._driver.find_element(By.CSS_SELECTOR, "#checkout").click()
