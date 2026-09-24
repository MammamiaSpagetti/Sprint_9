from selenium.webdriver.common.by import By


class CreateRecipePageLocators:
    NAME = (By.XPATH, '//label[div[normalize-space()="Название рецепта"]]/input')
    INGREDIENT = (By.XPATH, '//label[div[normalize-space()="Ингредиенты"]]/input')
    INGREDIENT_OPTION = '//div[contains(@class,"ingredientsInputs")]//div[text()="{}"]'
    AMOUNT = (By.CSS_SELECTOR, 'input[class*="ingredientsAmountValue"]')
    ADD_INGREDIENT = (By.XPATH, '//div[normalize-space()="Добавить ингредиент"]')
    ADDED_INGREDIENT = (By.CSS_SELECTOR, 'span[class*="ingredientsAddedItemTitle"]')
    TAG_BUTTONS = (By.CSS_SELECTOR, 'button[class*="checkboxGroupItem"]')
    TAG_NAME = (By.XPATH, './following-sibling::span')
    TAG_SELECTED_CLASS = 'checkbox_active'
    COOKING_TIME = (By.XPATH, '//label[div[normalize-space()="Время приготовления"]]/input')
    DESCRIPTION = (By.CSS_SELECTOR, 'textarea')
    IMAGE = (By.CSS_SELECTOR, 'input[type="file"]')
    IMAGE_PREVIEW = (By.CSS_SELECTOR, 'div[style*="data:image/"]')
    SUBMIT_BUTTON = (By.XPATH, '//form//button[normalize-space()="Создать рецепт"]')

    @classmethod
    def ingredient_option(cls, name):
        return By.XPATH, cls.INGREDIENT_OPTION.format(name)
