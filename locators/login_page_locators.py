from selenium.webdriver.common.by import By


class LoginPageLocators:
    FORM = (
        By.XPATH,
        '//form[.//input[@name="email"]][.//input[@name="password"]]'
        '[.//button[normalize-space()="Войти"]]',
    )
    EMAIL = (By.NAME, 'email')
    PASSWORD = (By.NAME, 'password')
    SUBMIT_BUTTON = (By.XPATH, '//form//button[normalize-space()="Войти"]')
