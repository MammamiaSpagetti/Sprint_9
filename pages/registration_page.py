import allure

from locators.registration_page_locators import RegistrationPageLocators
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    def register(self, user_data):
        with allure.step('Заполнить все поля регистрации'):
            self.fill(RegistrationPageLocators.FIRST_NAME, user_data['first_name'])
            self.fill(RegistrationPageLocators.LAST_NAME, user_data['last_name'])
            self.fill(RegistrationPageLocators.USERNAME, user_data['username'])
            self.fill(RegistrationPageLocators.EMAIL, user_data['email'])
            self.fill(RegistrationPageLocators.PASSWORD, user_data['password'])
        with allure.step('Отправить форму регистрации'):
            self.click(RegistrationPageLocators.SUBMIT_BUTTON)
