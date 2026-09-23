from uuid import uuid4

import allure
import requests

from data import API_TIMEOUT, EMAIL_DOMAIN, RECIPE_DATA, USER_DATA, USERNAME_PREFIX
from urls import CURRENT_USER_URL, LOGIN_API_URL, LOGOUT_API_URL, RECIPES_API_URL, USERS_URL


def generate_user_data():
    username = f'{USERNAME_PREFIX}{uuid4().hex}@{EMAIL_DOMAIN}'
    return {
        **USER_DATA,
        'username': username,
        'email': username,
    }


def generate_recipe_data():
    return {**RECIPE_DATA, 'name': f'{RECIPE_DATA["name"]} {uuid4().hex[:10]}'}


def check_api_response(response, expected_status):
    if response.status_code != expected_status:
        raise AssertionError(
            f'{response.request.method} {response.url}: '
            f'ожидался статус {expected_status}, получен {response.status_code}. '
            f'Ответ: {response.text}'
        )


def create_user(user_data):
    with allure.step('Создать уникального пользователя через API'):
        response = requests.post(USERS_URL, json=user_data, timeout=API_TIMEOUT)
        check_api_response(response, 201)
        return response.json()


def clean_test_data(user_data, allow_missing=False):
    with allure.step('Удалить рецепты тестового пользователя и завершить API-сессию'):
        with requests.Session() as session:
            response = session.post(
                LOGIN_API_URL,
                json={
                    'email': user_data['email'],
                    'password': user_data['password'],
                },
                timeout=API_TIMEOUT,
            )
            if response.status_code == 400 and allow_missing:
                allure.attach(
                    'Вход для очистки отклонён: регистрация могла не завершиться.',
                    name='Очистка тестовых данных',
                    attachment_type=allure.attachment_type.TEXT,
                )
                return
            check_api_response(response, 200)
            session.headers['Authorization'] = f'Token {response.json()["auth_token"]}'
            user_response = session.get(CURRENT_USER_URL, timeout=API_TIMEOUT)
            check_api_response(user_response, 200)
            user_id = user_response.json()['id']
            recipes_response = session.get(
                RECIPES_API_URL,
                params={'author': user_id, 'limit': 100},
                timeout=API_TIMEOUT,
            )
            check_api_response(recipes_response, 200)
            for recipe in recipes_response.json()['results']:
                response = session.delete(
                    f'{RECIPES_API_URL}{recipe["id"]}/', timeout=API_TIMEOUT,
                )
                check_api_response(response, 204)
            response = session.post(LOGOUT_API_URL, timeout=API_TIMEOUT)
            check_api_response(response, 204)
