from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    FIRST_NAME = (By.NAME, 'first_name')
    LAST_NAME = (By.NAME, 'last_name')
    USERNAME = (By.NAME, 'username')
    EMAIL = (By.NAME, 'email')
    PASSWORD = (By.NAME, 'password')
    SUBMIT_BUTTON = (By.XPATH, '//form//button[normalize-space()="Создать аккаунт"]')
