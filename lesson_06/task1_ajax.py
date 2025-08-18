from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()

# Перейти на сайт
driver.get("http://uitestingplayground.com/ajax")

# Нажимаем на синюю кнопку
blue_button = driver.find_element(By.CSS_SELECTOR, "#ajaxButton")
blue_button.click()

# Ожидаем появление зеленой плашки
WebDriverWait(driver, 20).until(
    ec.visibility_of_element_located((By.CSS_SELECTOR, "p.bg-success"))
)

# Получаем и выводим текст
message = driver.find_element(By.CSS_SELECTOR, "p.bg-success").text
print(message)

driver.quit()
