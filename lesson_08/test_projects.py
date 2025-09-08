# Позитивные тесты — проверяют корректную работу API при правильных данных

def test_create_project(api):
    # Подготавливаем валидные данные для создания проекта
    valid_project_payload = {'title': 'Test Project'}
    # Отправляем запрос на создание проекта
    response = api.create_project(valid_project_payload)
    # Проверяем, что статус ответа — 201 (Created)
    assert response.status_code == 201, f"Expected 201, got {
        response.status_code}"


def test_get_all_projects(api):
    # Отправляем запрос на получение всех проектов
    response = api.get_all_projects()
    # Проверяем, что статус ответа — 200 (OK)
    assert response.status_code == 200, f"Expected 200, got {
        response.status_code}"
    # Проверяем, что список проектов не пустой
    assert len(response.json()) > 0, "No projects found"


def test_get_project_by_id(api):
    # Сначала создаём проект, чтобы получить его ID
    valid_project_payload = {'title': 'Test Project'}
    create_response = api.create_project(valid_project_payload)
    # Извлекаем ID созданного проекта
    project_id = create_response.json().get('id')
    # Отправляем запрос на получение проекта по ID
    response = api.get_project_by_id(project_id)
    # Проверяем, что статус ответа — 200 (OK)
    assert response.status_code == 200, f"Expected 200, got {
        response.status_code}"


def test_update_project(api):
    # Создаём проект, который будем обновлять
    valid_project_payload = {'title': 'Updated Project'}
    create_response = api.create_project(valid_project_payload)
    project_id = create_response.json().get('id')
    # Подготавливаем новые данные для обновления
    updated_payload = {'title': 'Updated Project Name'}
    # Отправляем запрос на обновление проекта
    response = api.update_project(project_id, updated_payload)
    # Проверяем, что статус ответа — 200 (OK)
    assert response.status_code == 200, f"Expected 200, got {
        response.status_code}"


# Негативные тесты — проверяют корректную обработку ошибок при
# некорректных данных

def test_create_project_missing_title(api):
    # Отправляем запрос с пустым телом (нет обязательного поля title)
    invalid_payload = {}
    response = api.create_project(invalid_payload)
    # Ожидаем ошибку 400 (Bad Request)
    assert response.status_code == 400, f"Expected 400, got {
        response.status_code}"


def test_get_project_by_invalid_id(api):
    # Отправляем запрос с несуществующим ID проекта
    response = api.get_project_by_id('invalid-id')
    # Ожидаем ошибку 404 (Not Found)
    assert response.status_code == 404, f"Expected 404, got {
        response.status_code}"


def test_update_project_with_invalid_id(api):
    # Пытаемся обновить проект с несуществующим ID
    invalid_project_id = 'nonexistent-id'
    updated_payload = {'title': 'Updated Title'}
    response = api.update_project(invalid_project_id, updated_payload)
    # Ожидаем ошибку 404 (Not Found)
    assert response.status_code == 404, f"Expected 404, got {
        response.status_code}"


def test_create_project_invalid_title(api):
    # Отправляем запрос с некорректным типом данных для title (число вместо
    # строки)
    invalid_payload = {'title': 12345}
    response = api.create_project(invalid_payload)
    # Ожидаем ошибку 400 (Bad Request)
    assert response.status_code == 400, f"Expected 400, got {
        response.status_code}"
