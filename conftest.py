import os

import allure
import pytest
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.remote.file_detector import LocalFileDetector

from data import CHROME_VERSION
from helpers import clean_test_data, create_user, generate_recipe_data, generate_user_data
from pages.create_recipe_page import CreateRecipePage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.recipe_page import RecipePage
from pages.registration_page import RegistrationPage


def pytest_addoption(parser):
    parser.addoption(
        '--selenoid-uri', default=os.getenv('SELENOID_URI', ''),
        help='Адрес Selenoid; без параметра используется локальный Chrome.',
    )
    parser.addoption('--browser-version', default=CHROME_VERSION)
    parser.addoption('--headless', action='store_true', help='Скрыть окно локального Chrome.')


@pytest.fixture
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument('--window-size=1440,1100')
    options.add_argument('--lang=ru-RU')
    selenoid_uri = request.config.getoption('--selenoid-uri')
    if selenoid_uri:
        options.browser_version = request.config.getoption('--browser-version')
        options.set_capability('selenoid:options', {'name': request.node.name})
        browser = webdriver.Remote(command_executor=selenoid_uri, options=options)
        browser.file_detector = LocalFileDetector()
    else:
        if request.config.getoption('--headless'):
            options.add_argument('--headless=new')
        browser = webdriver.Chrome(options=options)
    try:
        browser.set_page_load_timeout(60)
        browser.set_window_size(1440, 1100)
        yield browser
    finally:
        browser.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    browser = item.funcargs.get('driver')
    if browser is not None and report.when in ('setup', 'call') and report.failed:
        try:
            allure.attach(
                browser.get_screenshot_as_png(), name='Страница при ошибке',
                attachment_type=allure.attachment_type.PNG,
            )
            allure.attach(
                browser.current_url, name='URL при ошибке',
                attachment_type=allure.attachment_type.TEXT,
            )
        except WebDriverException:
            allure.attach(
                'Браузерная сессия недоступна для скриншота.',
                name='Диагностика', attachment_type=allure.attachment_type.TEXT,
            )


@pytest.fixture
def user_data():
    return generate_user_data()


@pytest.fixture
def registration_user(user_data):
    yield user_data
    clean_test_data(user_data, allow_missing=True)


@pytest.fixture
def registered_user(user_data):
    create_user(user_data)
    yield user_data
    clean_test_data(user_data)


@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    page.open()
    return page


@pytest.fixture
def registration_page(driver):
    return RegistrationPage(driver)


@pytest.fixture
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture
def authenticated_main_page(registered_user, login_page, driver):
    login_page.open()
    login_page.login(registered_user)
    page = MainPage(driver)
    page.is_opened()
    page.is_logout_visible()
    return page


@pytest.fixture
def create_recipe_page(driver):
    return CreateRecipePage(driver)


@pytest.fixture
def recipe_page(driver):
    return RecipePage(driver)


@pytest.fixture
def recipe_data():
    return generate_recipe_data()
