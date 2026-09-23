import os


BASE_URL = os.getenv(
    'BASE_URL',
    'https://foodgram-frontend-1.foodgram.education-services.ru',
).rstrip('/')
API_URL = os.getenv(
    'API_URL',
    'https://foodgram-backend-1.foodgram.education-services.ru/api',
).rstrip('/')

MAIN_URL = f'{BASE_URL}/recipes'
LOGIN_URL = f'{BASE_URL}/signin'
REGISTRATION_URL = f'{BASE_URL}/signup'
CREATE_RECIPE_URL = f'{BASE_URL}/recipes/create'

USERS_URL = f'{API_URL}/users/'
CURRENT_USER_URL = f'{USERS_URL}me/'
LOGIN_API_URL = f'{API_URL}/auth/token/login/'
LOGOUT_API_URL = f'{API_URL}/auth/token/logout/'
RECIPES_API_URL = f'{API_URL}/recipes/'
