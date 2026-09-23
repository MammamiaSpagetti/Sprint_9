from selenium.webdriver.common.by import By


class MainPageLocators:
    CREATE_ACCOUNT_LINK = (By.LINK_TEXT, 'Создать аккаунт')
    LOGIN_LINK = (By.LINK_TEXT, 'Войти')
    LOGOUT_LINK = (By.XPATH, '//a[normalize-space()="Выход"]')
    CREATE_RECIPE_LINK = (By.CSS_SELECTOR, 'a[href="/recipes/create"]')
