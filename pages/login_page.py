import allure

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
from urls import LOGIN_URL


class LoginPage(BasePage):
    @allure.step('Открыть страницу авторизации')
    def open(self):
        self.open_url(LOGIN_URL)

    def login(self, user_data):
        with allure.step('Заполнить форму авторизации и нажать «Войти»'):
            self.fill(LoginPageLocators.EMAIL, user_data['email'])
            self.fill(LoginPageLocators.PASSWORD, user_data['password'])
            self.click(LoginPageLocators.SUBMIT_BUTTON)

    @allure.step('Проверить переход на страницу авторизации')
    def is_opened(self):
        return self.wait_for_url(LOGIN_URL)

    @allure.step('Проверить отображение формы авторизации')
    def is_form_visible(self):
        return self.find_visible(LoginPageLocators.FORM).is_displayed()
