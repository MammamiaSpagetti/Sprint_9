import re

import allure
from selenium.webdriver.support import expected_conditions as EC

from locators.recipe_page_locators import RecipePageLocators
from pages.base_page import BasePage
from urls import MAIN_URL


class RecipePage(BasePage):
    @allure.step('Проверить отображение карточки созданного рецепта')
    def is_card_visible(self):
        self.wait.until(EC.url_matches(rf'^{re.escape(MAIN_URL)}/\d+/?$'))
        self.find_visible(RecipePageLocators.CARD)
        self.find_visible(RecipePageLocators.IMAGE)
        self.wait.until(lambda driver: driver.find_element(*RecipePageLocators.TITLE).text)
        return True

    @allure.step('Получить название созданного рецепта')
    def get_name(self):
        return self.find_visible(RecipePageLocators.TITLE).text
