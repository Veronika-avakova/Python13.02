import os
import requests
from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env
load_dotenv()

# Получаем ключ из окружения. Если его нет, будет пустая строка.
API_KEY = os.getenv('YOUGILE_API_KEY', '')
BASE_URL = 'https://ru.yougile.com'


def get_headers():
    """Функция для генерации заголовков с авторизацией."""
    headers = {'Content-Type': 'application/json'}
    if API_KEY:
        headers['Authorization'] = f'Bearer {API_KEY}'
    return headers


# 1. Создать проект

def test_positive_create_project():
    """Позитивный тест: создание проекта с валидным названием."""
    title = 'Таганрог'
    headers = get_headers()
    body = {"title": title}

    response = requests.post(
        f'{BASE_URL}/api-v2/projects',
        json=body,
        headers=headers
    )
    assert response.status_code == 201


def test_negative_create_project():
    """Негативный тест: создание проекта с пустым названием."""
    headers = get_headers()
    body = {"title": ""}

    response = requests.post(
        f'{BASE_URL}/api-v2/projects',
        json=body,
        headers=headers
    )
    assert response.status_code == 400


# 2. Изменить проект

def test_positive_edit_project():
    """Позитивный тест: изменение названия существующего проекта."""
    title = 'Москва'
    new_title = 'Санкт-Петербург'
    headers = get_headers()

    # Создаем проект
    create_resp = requests.post(
        f'{BASE_URL}/api-v2/projects',
        json={"title": title},
        headers=headers
    )
    assert create_resp.status_code == 201

    project_id = create_resp.json()['id']

    # Меняем имя проекта
    edit_resp = requests.put(
        f'{BASE_URL}/api-v2/projects/{project_id}',
        json={"title": new_title},
        headers=headers
    )
    assert edit_resp.status_code == 200

    # Проверяем, что название изменилось
    get_resp = requests.get(
        f'{BASE_URL}/api-v2/projects/{project_id}',
        headers=headers
    )
    assert get_resp.json()['title'] == new_title


def test_negative_edit_project_title():
    """Негативный тест: попытка изменить название на пустую строку."""
    title = 'Москва'
    headers = get_headers()

    # Создаем проект
    create_resp = requests.post(
        f'{BASE_URL}/api-v2/projects',
        json={"title": title},
        headers=headers
    )

    if create_resp.status_code != 201:
        return

    project_id = create_resp.json()['id']

    # Пытаемся изменить название на пустое
    response = requests.put(
        f'{BASE_URL}/api-v2/projects/{project_id}',
        json={"title": ""},
        headers=headers
    )

    assert response.status_code in [400, 422]


# 3. Получить проект по ID

def test_positive_get_project_by_id():
    """Позитивный тест: получение проекта по существующему ID."""
    title = 'Таганрог'
    headers = get_headers()

    # Создаем проект, чтобы получить его ID
    create_resp = requests.post(
        f'{BASE_URL}/api-v2/projects',
        json={"title": title},
        headers=headers
    )

    assert create_resp.status_code == 201, "Проект не был создан"

    project_id = create_resp.json()['id']

    # Получаем проект по ID
    response = requests.get(
        f'{BASE_URL}/api-v2/projects/{project_id}',
        headers=headers
    )

    assert response.status_code == 200, "Не удалось получить проект по ID"


def test_negative_get_project_by_nonexistent_id():
    """Негативный тест: получение проекта по несуществующему ID."""
    nonexistent_id = "00000000-0000-0000-0000-000000000000"
    headers = get_headers()

    response = requests.get(
        f'{BASE_URL}/api-v2/projects/{nonexistent_id}',
        headers=headers
    )

    assert response.status_code == 404, (
        f"Ожидался статус 404, получен {response.status_code}"
    )
