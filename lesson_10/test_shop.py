# Импортируем необходимые модули для работы с Selenium и Chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Импортируем наши классы-страницы (Page Object)
# Класс для главной страницы (авторизация)
from mane_page import MainPage
# Класс для страницы с товарами
from products_page import ProductsPage
from you_cart_page import YouCart  # Класс для страницы корзины
# Класс для страницы с формой данных
from information_page import Information
# Класс для страницы с итоговой суммой
from price_total import PriceTotal

# Импортируем allure для создания отчетов
import allure

# Импортируем pytest как фреймворк для тестирования
# import pytest


@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тест оформления заказа в интернет-магазине")
@allure.description("""
Полный тест оформления заказа:
1. Авторизация пользователя standard_user
2. Добавление трех товаров в корзину
3. Переход к оформлению заказа
4. Заполнение личных данных
5. Проверка итоговой суммы $58.29
""")
def test_shop():
    """Тест оформления заказа в интернет-магазине."""
    # Создаём объект настроек для Chrome
    options = webdriver.ChromeOptions()

    # Отключаем встроенный менеджер паролей Chrome, чтобы он не мешал тесту
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })

    with allure.step("Запуск браузера Chrome с настройками"):
        # Запускаем браузер Chrome с автоматической установкой драйвера
        browser = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )

    try:
        with allure.step("Открытие главной страницы"):
            # Создаём объект главной страницы и открываем сайт
            main_page = MainPage(browser)
            main_page.get()

        with allure.step("Авторизация пользователя standard_user"):
            # Авторизуемся на сайте
            main_page.authorization("standard_user", "secret_sauce")

        with allure.step("Добавление товаров в корзину"):
            # Создаём объект страницы с товарами и добавляем товары в корзину
            product = ProductsPage(browser)
            product.add_to_cart()

        with allure.step("Переход к оформлению заказа"):
            # Создаём объект страницы корзины и переходим к оформлению заказа
            cart = YouCart(browser)
            cart.checkout()

        with allure.step("Заполнение личных данных"):
            # Создаём объект страницы с формой и заполняем данные покупателя
            information = Information(browser)
            information.fill_out_the_forms("Alex", "Nekrasov", "654002")

        with allure.step("Проверка итоговой суммы"):
            # Создаём объект страницы с итоговой суммой
            total_price = PriceTotal(browser)
            # Получаем итоговую сумму заказа
            total = total_price.checkout_price()
            # Проверяем, что итоговая сумма соответствует ожидаемой
            assert total == "Total: $58.29", "Итоговая сумма не равна $58.29"

    finally:
        with allure.step("Закрытие браузера"):
            # Закрываем браузер
            total_price.close_browser()
