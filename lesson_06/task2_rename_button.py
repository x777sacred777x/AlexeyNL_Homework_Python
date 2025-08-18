from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

# Перейти на сайт
driver.get("http://uitestingplayground.com/textinput")

# Вводим текст в поле
input_field = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
input_field.send_keys("SkyPro")

# Нажимаем на кнопку
blue_button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
blue_button.click()

# Получаем и выводим текст кнопки
button_text = blue_button.text
print(button_text)

driver.quit()
