# Импортируем класс By, который используется для указания типа локатора
# (например, поиск по CSS-селектору, XPATH, ID и т.д.)
from selenium.webdriver.common.by import By


class PriceTotal:
    # Конструктор класса — принимает драйвер браузера (webdriver)
    def __init__(self, driver):
        # Сохраняем переданный драйвер в атрибуте объекта для дальнейшего
        # использования
        self._driver = driver

    # Метод для получения итоговой суммы заказа
    def checkout_price(self):
        # Находим элемент с итоговой суммой по CSS-селектору "div.summary_total_label"
        # и получаем его текстовое содержимое
        total = self._driver.find_element(
            By.CSS_SELECTOR, "div.summary_total_label").text

        # Выводим итоговую сумму в консоль (для отладки или логирования)
        print(total)

        # Возвращаем итоговую сумму, чтобы можно было использовать её в тестах
        # или других методах
        return total

    # Метод для закрытия браузера
    def close_browser(self):
        # Завершаем работу драйвера и закрываем все окна браузера
        self._driver.quit()
