from selenium.webdriver.common.by import By


class RecipePageLocators:
    CARD = (By.XPATH, '//div[img[contains(@class,"single-card__image")]]')
    TITLE = (By.CSS_SELECTOR, 'h1')
    IMAGE = (By.CSS_SELECTOR, 'img[class*="single-card__image"]')
