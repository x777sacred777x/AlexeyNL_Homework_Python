from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()

# Перейти на сайт
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
           )

# Ожидаем загрузку всех картинок (ждем появления последней картинки)
WebDriverWait(driver, 20).until(
    ec.presence_of_element_located((By.CSS_SELECTOR, "#landscape"))
)

# Получаем 3-ю картинку (индекс 2, так как отсчет с 0)
third_image = driver.find_element(By.CSS_SELECTOR, "#award")
src_value = third_image.get_attribute("src")
print(src_value)

driver.quit()
