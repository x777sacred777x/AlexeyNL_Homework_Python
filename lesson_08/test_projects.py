# ✅ Позитивные тесты — проверяют корректную работу API при валидных данных

def test_create_project(api):
    """
    Проверяет успешное создание проекта.
    Ожидается статус 201 и наличие ID в теле ответа.
    """
    payload = {'title': 'Test Project'}  # Данные нового проекта
    response = api.create_project(payload)  # Отправляем запрос на создание
    assert response.status_code == 201, f"Expected 201, got {response.status_code}"  # Проверяем статус
    data = response.json()  # Получаем тело ответа в формате JSON
    # В зависимости от структуры API, проект может быть в разных ключах
    project = data.get('content') or data.get('data') or data
    assert 'id' in project, "Response missing 'id'"  # Проверяем наличие ID
    # Проверяем совпадение названия, если оно возвращается
    if 'title' in project:
        assert project['title'] == payload['title'], "Title mismatch"

def test_get_all_projects(api):
    """
    Проверяет получение списка всех проектов.
    Ожидается статус 200 и непустой список в ключе 'content'.
    """
    response = api.get_all_projects()  # Запрашиваем все проекты
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"  # Проверяем статус
    data = response.json()
    projects = data.get('content')  # Получаем список проектов
    assert isinstance(projects, list), f"Expected list in 'content', got {type(projects)}"  # Проверяем тип
    assert len(projects) > 0, "No projects found"  # Убеждаемся, что список не пуст
    for project in projects:
        # Проверяем, что каждый проект содержит обязательные поля
        assert 'id' in project and 'title' in project, "Project missing required fields"

def test_get_project_by_id(api):
    """
    Проверяет получение проекта по ID.
    Сначала создаётся проект, затем запрашивается по ID.
    """
    payload = {'title': 'Test Project'}
    create_response = api.create_project(payload)  # Создаём проект
    project_id = create_response.json().get('id')  # Получаем его ID
    response = api.get_project_by_id(project_id)  # Запрашиваем по ID
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"  # Проверяем статус
    data = response.json()
    assert data['id'] == project_id, "ID mismatch"  # Проверяем ID
    assert data['title'] == payload['title'], "Title mismatch"  # Проверяем название

def test_update_project(api):
    """
    Проверяет обновление проекта.
    Ожидается статус 200 и наличие ID в теле ответа.
    """
    payload = {'title': 'Initial Title'}
    create_response = api.create_project(payload)  # Создаём проект
    project_id = create_response.json().get('id')  # Получаем его ID
    updated_payload = {'title': 'Updated Title'}  # Новые данные
    response = api.update_project(project_id, updated_payload)  # Обновляем проект
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"  # Проверяем статус
    data = response.json()
    # В зависимости от структуры API, проект может быть в разных ключах
    project = data.get('content') or data.get('data') or data
    assert 'id' in project, "Response missing 'id'"  # Проверяем наличие ID
    assert project['id'] == project_id, "ID mismatch after update"  # Проверяем ID
    # Проверяем, что название обновилось
    if 'title' in project:
        assert project['title'] == updated_payload['title'], "Title not updated"

# ❌ Негативные тесты — проверяют корректную обработку ошибок при невалидных данных

def test_create_project_missing_title(api):
    """
    Проверяет создание проекта без обязательного поля title.
    Ожидается ошибка 400 и сообщение об ошибке в теле.
    """
    response = api.create_project({})  # Пустой payload
    assert response.status_code == 400, f"Expected 400, got {response.status_code}"  # Проверяем статус
    error = response.json()
    # Проверяем наличие сообщения об ошибке
    assert 'error' in error or 'message' in error, "No error message in response"

def test_get_project_by_invalid_id(api):
    """
    Проверяет запрос проекта по несуществующему ID.
    Ожидается ошибка 404 и сообщение об ошибке.
    """
    response = api.get_project_by_id('invalid-id')  # Некорректный ID
    assert response.status_code == 404, f"Expected 404, got {response.status_code}"  # Проверяем статус
    error = response.json()
    assert 'error' in error or 'message' in error, "No error message in response"  # Проверяем сообщение

def test_update_project_with_invalid_id(api):
    """
    Проверяет обновление проекта с несуществующим ID.
    Ожидается ошибка 404 и сообщение об ошибке.
    """
    response = api.update_project('nonexistent-id', {'title': 'Updated Title'})  # Некорректный ID
    assert response.status_code == 404, f"Expected 404, got {response.status_code}"  # Проверяем статус
    error = response.json()
    assert 'error' in error or 'message' in error, "No error message in response"  # Проверяем сообщение

def test_create_project_invalid_title(api):
    """
    Проверяет создание проекта с некорректным типом title (число вместо строки).
    Ожидается ошибка 400 и сообщение об ошибке.
    """
    response = api.create_project({'title': 12345})  # Некорректный тип данных
    assert response.status_code == 400, f"Expected 400, got {response.status_code}"  # Проверяем статус
    error = response.json()
    assert 'error' in error or 'message' in error, "No error message in response"  # Проверяем сообщение
