import requests

base_url = 'https://ru.yougile.com'
api_key = ""


# 1. Создать проект

def test_positive_create_project():
    """Позитивный тест: создание проекта с валидным названием."""
    title = 'Таганрог'
    my_headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    body = {"title": title}

    project = requests.post(
        url=f'{base_url}/api-v2/projects',
        json=body,
        headers=my_headers
    )
    assert project.status_code == 201


def test_negative_create_project():
    """Негативный тест: создание проекта с пустым названием."""
    title = ''
    my_headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    body = {"title": title}

    project = requests.post(
        url=f'{base_url}/api-v2/projects',
        json=body,
        headers=my_headers
    )
    assert project.status_code == 400


# 2. Изменить проект

def test_positive_edit_project():
    """Позитивный тест: изменение названия существующего проекта."""
    title = 'Москва'
    new_title = 'Санкт-Петербург'
    my_headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }

    # Создаем проект
    body = {"title": title}
    project = requests.post(
        url=f'{base_url}/api-v2/projects',
        json=body,
        headers=my_headers
    )
    assert project.status_code == 201

    project_id = project.json()['id']

    # Меняем имя проекта
    body = {"title": new_title}
    new_project = requests.put(
        url=f'{base_url}/api-v2/projects/{project_id}',
        json=body,
        headers=my_headers
    )
    assert new_project.status_code == 200

    # Проверяем, что название изменилось
    response = requests.get(
        url=f'{base_url}/api-v2/projects/{project_id}',
        headers=my_headers
    )
    assert response.status_code == 200
    assert response.json()['title'] == new_title


def test_negative_edit_project_title():
    """Негативный тест: попытка изменить название на пустую строку."""
    title = 'Москва'
    new_title = ''
    my_headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }

    # Создаем проект
    body = {"title": title}
    project = requests.post(
        url=f'{base_url}/api-v2/projects',
        json=body,
        headers=my_headers
    )
    assert project.status_code == 201

    project_id = project.json()['id']

    # Пытаемся изменить название на пустое
    body = {"title": new_title}
    response = requests.put(
        url=f'{base_url}/api-v2/projects/{project_id}',
        json=body,
        headers=my_headers
    )

    # Ожидаем ошибку валидации
    assert response.status_code in [400, 422]

    # Проверяем, что название НЕ изменилось
    get_response = requests.get(
        url=f'{base_url}/api-v2/projects/{project_id}',
        headers=my_headers
    )
    assert get_response.status_code == 200
    assert get_response.json()['title'] == title


# 3. Получить проект по ID

def test_positive_get_project_by_id():
    """Позитивный тест: получение проекта по существующему ID."""
    title = 'Таганрог'
    my_headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }

    # Создаем проект, чтобы получить его ID
    body = {"title": title}
    project = requests.post(
        url=f'{base_url}/api-v2/projects',
        json=body,
        headers=my_headers
    )

    assert project.status_code == 201, "Проект не был создан"

    project_id = project.json()['id']

    # Получаем проект по ID
    response = requests.get(
        url=f'{base_url}/api-v2/projects/{project_id}',
        headers=my_headers
    )

    # Проверяем результат
    assert response.status_code == 200, "Не удалось получить проект по ID"

    data = response.json()

    assert data['id'] == project_id, "ID полученного проекта не совпадает"
    assert data['title'] == title, "Название проекта не совпадает"


def test_negative_get_project_by_nonexistent_id():
    """Негативный тест: получение проекта по несуществующему ID."""

    nonexistent_id = "00000000-0000-0000-0000-000000000000"

    my_headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }

    response = requests.get(
        url=f'{base_url}/api-v2/projects/{nonexistent_id}',
        headers=my_headers
    )

    assert response.status_code == 404, (f"Ожидался статус 404, "
                                         f"получен {response.status_code}")
