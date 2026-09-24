from pathlib import Path


APP_DIR = Path(__file__).resolve().parent
RECIPE_IMAGE = APP_DIR / 'assets' / 'recipe.png'
WAIT_TIMEOUT = 20
API_TIMEOUT = 30
CHROME_VERSION = '128.0'

USER_DATA = {
    'first_name': 'Иван',
    'last_name': 'Тестовый',
    'password': 'Sprint9_Test_4826!',
}
USERNAME_PREFIX = 'sprint9_'
EMAIL_DOMAIN = 'example.com'

RECIPE_DATA = {
    'name': 'Картофель для автотеста',
    'ingredient': 'картофель',
    'amount': '200',
    'tag': 'Обед',
    'cooking_time': '20',
    'description': 'Вымыть картофель, отварить до готовности и подать.',
    'image': RECIPE_IMAGE,
}
