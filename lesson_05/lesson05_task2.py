from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(service=ChromeService
                          (ChromeDriverManager().install()))

# Открыть страницу
driver.get("http://uitestingplayground.com/dynamicid")

# Найти кнопку
serch_button = driver.find_element(
    By.XPATH, "//button[contains(text(), 'Button with Dynamic ID')]")

sleep(3)

# Кликнуть по кнопке
serch_button.click()

sleep(3)
