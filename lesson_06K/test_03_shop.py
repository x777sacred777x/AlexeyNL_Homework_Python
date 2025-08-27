import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains


class TestShopPurchase:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 15)
        self.actions = ActionChains(self.driver)
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        yield
        self.driver.quit()

    def _wait_for_element_visible(self, by, value, timeout=15):
        """Ожидание видимости элемента"""
        return self.wait.until(
            ec.visibility_of_element_located((by, value)),
            message=f"Element {by}={value} not visible after {timeout} seconds"
        )

    def _wait_for_element_clickable(self, by, value, timeout=15):
        """Ожидание кликабельности элемента"""
        return self.wait.until(
            ec.element_to_be_clickable((by, value)),
            message=f"Element {by}={value} not clickable"
                    f" after {timeout} seconds"
        )

    def _wait_for_text_present(self, by, value, text, timeout=15):
        """Ожидание появления определенного текста в элементе"""
        return self.wait.until(
            ec.text_to_be_present_in_element((by, value), text),
            message=f"Text '{text}' not found in element {by}={value}"
                    f" after {timeout} seconds"
        )

    def _wait_for_url_contains(self, text, timeout=15):
        """Ожидание изменения URL"""
        return self.wait.until(
            ec.url_contains(text),
            message=f"URL does not contain '{text}' after {timeout} seconds"
        )

    def test_total_amount_should_be_58_29(self):
        # Шаг 1: Авторизация
        print("Шаг 1: Авторизация пользователя")
        username_input = self._wait_for_element_visible(By.ID, "user-name")
        username_input.send_keys("standard_user")

        password_input = self._wait_for_element_visible(By.ID, "password")
        password_input.send_keys("secret_sauce")

        login_button = self._wait_for_element_clickable(By.ID, "login-button")
        login_button.click()

        # Ожидание перехода на страницу товаров
        self._wait_for_url_contains("inventory")
        self._wait_for_element_visible(By.CLASS_NAME, "inventory_list")

        # Шаг 2: Добавление товаров в корзину
        print("Шаг 2: Добавление товаров в корзину")

        # Sauce Labs Backpack
        print("Добавление Sauce Labs Backpack")
        backpack_add_button = self._wait_for_element_clickable(
            By.ID, "add-to-cart-sauce-labs-backpack"
        )
        backpack_add_button.click()

        # Ожидание обновления кнопки (должна стать remove)
        self._wait_for_element_visible(By.ID, "remove-sauce-labs-backpack")

        # Sauce Labs Bolt T-Shirt
        print("Добавление Sauce Labs Bolt T-Shirt")
        tshirt_add_button = self._wait_for_element_clickable(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"
        )
        tshirt_add_button.click()

        # Ожидание обновления кнопки
        self._wait_for_element_visible(By.ID, "remove-sauce-labs-bolt-t-shirt")

        # Sauce Labs Onesie
        print("Добавление Sauce Labs Onesie")
        onesie_add_button = self._wait_for_element_clickable(
            By.ID, "add-to-cart-sauce-labs-onesie"
        )
        onesie_add_button.click()

        # Ожидание обновления кнопки
        self._wait_for_element_visible(By.ID, "remove-sauce-labs-onesie")

        # Шаг 3: Переход в корзину
        print("Шаг 3: Переход в корзину")
        cart_icon = self._wait_for_element_clickable(
            By.CLASS_NAME, "shopping_cart_link")
        cart_icon.click()

        # Ожидание перехода на страницу корзины
        self._wait_for_url_contains("cart")
        self._wait_for_element_visible(By.CLASS_NAME, "cart_list")

        # Шаг 4: Нажатие Checkout
        print("Шаг 4: Нажатие Checkout")
        checkout_button = self._wait_for_element_clickable(By.ID, "checkout")
        checkout_button.click()

        # Ожидание перехода на страницу оформления
        self._wait_for_url_contains("checkout-step-one")
        self._wait_for_element_visible(By.CLASS_NAME, "checkout_info")

        # Шаг 5: Заполнение формы
        print("Шаг 5: Заполнение формы данными")

        # Имя
        first_name_input = self._wait_for_element_visible(By.ID, "first-name")
        first_name_input.send_keys("Алексей")

        # Фамилия
        last_name_input = self._wait_for_element_visible(By.ID, "last-name")
        last_name_input.send_keys("Некрасов")

        # Почтовый индекс
        postal_code_input = self._wait_for_element_visible(
            By.ID, "postal-code")
        postal_code_input.send_keys("654002")

        # Продолжение
        continue_button = self._wait_for_element_clickable(By.ID, "continue")
        continue_button.click()

        # Ожидание перехода на страницу подтверждения
        self._wait_for_url_contains("checkout-step-two")
        self._wait_for_element_visible(By.CLASS_NAME, "summary_info")

        # Шаг 6: Проверка итоговой стоимости
        print("Шаг 6: Проверка итоговой стоимости")
        total_element = self._wait_for_element_visible(
            By.CLASS_NAME, "summary_total_label"
        )

        # Ожидание появления правильной суммы
        self._wait_for_text_present(
            By.CLASS_NAME, "summary_total_label", "$58.29")

        total_text = total_element.text
        print(f"Найдена итоговая сумма: {total_text}")

        total_amount = total_text.split("$")[1]

        # Проверка, что итоговая сумма равна $58.29
        assert total_amount == "58.29", (f"Expected $58.29, "
                                         f"but got ${total_amount}")

        # Вывод результата
        print("\n" + "=" * 50)
        print("РЕЗУЛЬТАТ ТЕСТА:")
        print("=" * 50)
        print(f"✓ Тест успешно пройден!")
        print(f"✓ Итоговая сумма: ${total_amount}")
        print(f"✓ Ожидаемая сумма: $58.29")
        print(f"✓ Статус: СООТВЕТСТВУЕТ ТРЕБОВАНИЯМ")
        print("=" * 50)
