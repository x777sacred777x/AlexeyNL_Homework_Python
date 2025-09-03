import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
# Если работает, то оставляем строку активной.
# from webdriver_manager.microsoft import EdgeChromiumDriverManager


# Фикстура pytest — запускает браузер Edge перед тестом и закрывает его после
@pytest.fixture
def driver():

    # Если работает, то оставляем строку активной.
    # driver = webdriver.Edge(service=EdgeService
    # (EdgeChromiumDriverManager().install()))
    # Если не работает, то обновляем EDGE до актуальной версии,
    # переходим на https://developer.microsoft.com/en-us/
    # microsoft-edge/tools/webdriver/?form=MA13LH#downloads
    # скачиваем Stable Channel для вашей версии EDGE и
    # архитектуры системы х64 или х86, распаковываем в любое удобное место,
    # в папке, куда вы сохранили драйвер, в адресной строке
    # копируем адрес через ПКМ . Затем переходим в код .
    # Удаляем строку driver = webdriver.Edge(service=EdgeService
    # (EdgeChromiumDriverManager().install())),
    # здесь система пытается установить драйвер из сети
    # по адресу который недоступен,или, не проверял, закрыт для РФ.
    # Вместо нее вставляем следующие строки:
    # edge_driver_path = r"C:\Users\Professional\Desktop\
    # AlexeyNL_Homework_Python_1\AlexeyNL_Homework_Python\msedgedriver.exe"
    # тут мы после кавычек вставили путь который ранее скопировали
    # в папке и после добавили слеш и написали имя файла,
    # это мы создали переменную которая говорит коду, где взять драйвер.
    # И вторая строка: driver = webdriver.Edge
    # (service=EdgeService(edge_driver_path))
    # говорим драйверу что вэбдрайвер эдже равен переменной которой мы
    # присвоили путь к драйверу.

    # Указываем путь к скачанному msedgedriver.exe
    edge_driver_path = r"C:\Users\Professional\Desktop\AlexeyNL_Homework_Python_1\AlexeyNL_Homework_Python\msedgedriver.exe"

    # Инициализируем драйвер Edge
    driver = webdriver.Edge(service=EdgeService(edge_driver_path))

    # Открываем страницу с формой
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Возвращаем драйвер в тест
    yield driver

    # Закрываем браузер после завершения теста
    driver.quit()


# Основной тест — проверяет валидацию формы
def test_form_validation(driver):
    # Данные для заполнения формы
    input_data = {
        "First name": "Иван",
        "Last name": "Петров",
        "Address": "Ленина, 55-3",
        "E-mail": "test@skypro.com",
        "Phone number": "+7985899998787",
        "Zip code": "",  # Оставляем пустым — должно вызвать ошибку
        "City": "Москва",
        "Country": "Россия",
        "Job position": "QA",
        "Company": "SkyPro"
    }

    # Ждём, пока все поля формы появятся на странице
    WebDriverWait(driver, 15).until(
        ec.presence_of_all_elements_located((By.CSS_SELECTOR, ".form-label"))
    )

    # Получаем все элементы с метками формы
    labels = driver.find_elements(By.CSS_SELECTOR, ".form-label")

    # Заполняем поля формы
    for label in labels:
        # Некоторые метки содержат несколько названий (например, "Zip
        # code\nN/A")
        field_names = label.text.split('\n')
        for field_name in field_names:
            field_name = field_name.strip()
            if field_name in input_data:
                # Находим input внутри метки и заполняем его
                input_element = label.find_element(By.TAG_NAME, "input")
                input_element.clear()
                input_element.send_keys(input_data[field_name])

    # Находим и нажимаем кнопку Submit
    submit_button = driver.find_element(
        By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

    # Ждём повторного появления меток после отправки формы
    WebDriverWait(driver, 15).until(
        ec.presence_of_all_elements_located((By.CSS_SELECTOR, ".form-label"))
    )

    # Выводим результаты валидации в консоль
    print("\n📋 Результаты валидации:\n" + "-" * 40)
    for label in driver.find_elements(By.CSS_SELECTOR, ".form-label"):
        field_names = label.text.split('\n')

        # Получаем класс div, который показывает статус валидации (success или
        # danger)
        alert_class = label.find_element(
            By.TAG_NAME, "div").get_attribute("class")

        for field_name in field_names:
            field_name = field_name.strip()

            # Проверка для поля Zip code — должно быть с ошибкой (danger)
            if field_name == "Zip code":
                print(f"🔴 {field_name}: ожидается 'danger'")
                assert "danger" in alert_class, (f"Ожидался класс"
                                                 f" 'danger' для "
                                                 f"поля '{field_name}'")

            # Проверка для поля N/A — тоже должно быть с ошибкой (danger)
            elif field_name == "N/A":
                print(f"🔴 {field_name}: ожидается 'danger'")
                assert "danger" in alert_class, (f"Ожидался класс"
                                                 f" 'danger' для "
                                                 f"поля '{field_name}'")

            # Все остальные поля должны быть успешными (success)
            else:
                print(f"🟢 {field_name}: ожидается 'success'")
                assert "success" in alert_class, (f"Ожидался класс"
                                                  f" 'success' для "
                                                  f"поля '{field_name}'")

    # Завершаем вывод
    print("-" * 40 + "\n✅ Тест завершён успешно.")
