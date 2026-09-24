import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from urls import MAIN_URL


class MainPage(BasePage):
    @allure.step('Открыть главную страницу')
    def open(self):
        self.open_url(MAIN_URL)

    @allure.step('Нажать «Создать аккаунт»')
    def open_registration(self):
        self.click(MainPageLocators.CREATE_ACCOUNT_LINK)

    @allure.step('Нажать «Войти»')
    def open_login(self):
        self.click(MainPageLocators.LOGIN_LINK)

    @allure.step('Перейти на вкладку «Создать рецепт»')
    def open_recipe_creation(self):
        self.click(MainPageLocators.CREATE_RECIPE_LINK)

    @allure.step('Проверить переход на главную страницу')
    def is_opened(self):
        return self.wait_for_url(MAIN_URL)

    @allure.step('Проверить отображение кнопки «Выход»')
    def is_logout_visible(self):
        return self.find_visible(MainPageLocators.LOGOUT_LINK).is_displayed()
