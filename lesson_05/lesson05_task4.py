from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep

driver = webdriver.Firefox(service=FirefoxService
                           (GeckoDriverManager().install()))

# Открыть страницу
driver.get("http://the-internet.herokuapp.com/login")

# Найти поле username
username_locator = "#username"
search_username = driver.find_element(By.CSS_SELECTOR, username_locator)

# Ввести имя пользователя
search_username.send_keys("tomsmith")
sleep(3)

# Найти поле password
password_locator = "#password"
search_password = driver.find_element(By.CSS_SELECTOR, password_locator)

# Ввести пароль
search_password.send_keys("SuperSecretPassword!")
sleep(3)

# Найти кнопку "Login"
login_locator = "i.fa.fa-2x.fa-sign-in"
search_login = driver.find_element(By.CSS_SELECTOR, login_locator)

# Нажать на кнопку "Login"
search_login.click()
sleep(3)

# Получение текста плашки
flash_message = WebDriverWait(driver, 10).until(
    ec.visibility_of_element_located((By.ID, "flash")))
print("Текст плашки:", flash_message.text.split("×")[0].strip())
sleep(3)

# Закрыть браузер
driver.quit()
