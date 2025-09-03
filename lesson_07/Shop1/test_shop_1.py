# Импортируем необходимые модули для работы с Selenium и Chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Импортируем наши классы-страницы (Page Object)
from mane_page import MainPage  # Класс для главной страницы (авторизация)
from products_page import ProductsPage  # Класс для страницы с товарами
from you_cart_page import YouCart  # Класс для страницы корзины
from information_page import Information  # Класс для страницы с формой данных
from price_total import PriceTotal  # Класс для страницы с итоговой суммой


def test_shop():
    # Создаём объект настроек для Chrome
    options = webdriver.ChromeOptions()

    # Отключаем встроенный менеджер паролей Chrome, чтобы он не мешал тесту
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })

    # Запускаем браузер Chrome с автоматической установкой драйвера
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=options
    )

    # Создаём объект главной страницы и открываем сайт
    main_page = MainPage(browser)
    main_page.get()

    # Авторизуемся на сайте
    main_page.authorization("standard_user", "secret_sauce")

    # Создаём объект страницы с товарами и добавляем товары в корзину
    product = ProductsPage(browser)
    product.add_to_cart()

    # Создаём объект страницы корзины и переходим к оформлению заказа
    cart = YouCart(browser)
    cart.checkout()

    # Создаём объект страницы с формой и заполняем данные покупателя
    information = Information(browser)
    information.fill_out_the_forms("Alex", "Nekrasov", "654002")

    # Создаём объект страницы с итоговой суммой
    total_price = PriceTotal(browser)

    # Получаем итоговую сумму заказа
    total = total_price.checkout_price()

    # Проверяем, что итоговая сумма соответствует ожидаемой
    assert total == "Total: $58.29", "Итоговая сумма не равна $58.29"

    # Закрываем браузер
    total_price.close_browser()
