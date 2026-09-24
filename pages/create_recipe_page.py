import allure
from selenium.webdriver.support import expected_conditions as EC

from locators.create_recipe_page_locators import CreateRecipePageLocators as Locators
from pages.base_page import BasePage
from urls import CREATE_RECIPE_URL


class CreateRecipePage(BasePage):
    @allure.step('Выбрать тег «{tag_name}»')
    def select_tag(self, tag_name):
        buttons = self.wait.until(EC.visibility_of_all_elements_located(Locators.TAG_BUTTONS))
        for button in buttons:
            name = button.find_element(*Locators.TAG_NAME).text
            selected = Locators.TAG_SELECTED_CLASS in button.get_attribute('class')
            if selected != (name == tag_name):
                button.click()

    @allure.step('Выбрать ингредиент из подсказок и добавить количество')
    def add_ingredient(self, name, amount):
        self.fill(Locators.INGREDIENT, name)
        self.click(Locators.ingredient_option(name))
        self.fill(Locators.AMOUNT, amount)
        self.click(Locators.ADD_INGREDIENT)
        self.wait.until(EC.text_to_be_present_in_element(Locators.ADDED_INGREDIENT, name))

    @allure.step('Загрузить изображение из assets')
    def upload_image(self, image_path):
        image_input = self.wait.until(EC.presence_of_element_located(Locators.IMAGE))
        image_input.send_keys(str(image_path.resolve()))
        self.find_visible(Locators.IMAGE_PREVIEW)

    def create_recipe(self, recipe_data):
        self.wait_for_url(CREATE_RECIPE_URL)
        with allure.step('Заполнить название рецепта'):
            self.fill(Locators.NAME, recipe_data['name'])
        self.select_tag(recipe_data['tag'])
        self.add_ingredient(recipe_data['ingredient'], recipe_data['amount'])
        with allure.step('Заполнить время приготовления и описание'):
            self.fill(Locators.COOKING_TIME, recipe_data['cooking_time'])
            self.fill(Locators.DESCRIPTION, recipe_data['description'])
        self.upload_image(recipe_data['image'])
        with allure.step('Нажать «Создать рецепт»'):
            self.click(Locators.SUBMIT_BUTTON)
