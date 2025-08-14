from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox(service=FirefoxService
                           (GeckoDriverManager().install()))

# Открыть страницу
driver.get("http://the-internet.herokuapp.com/inputs")

# Найти поле ввода
input_locator = "input"
search_input = driver.find_element(By.CSS_SELECTOR, input_locator)

# Ввести текст в поле ввода Sky
search_input.send_keys("Sky")
sleep(3)

# Очистить поле
search_input.clear()

# Ввести текст в поле ввода Pro
search_input.send_keys("Pro")
sleep(3)

# Закрыть браузер
driver.quit()
