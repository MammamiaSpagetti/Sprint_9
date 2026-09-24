from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from data import WAIT_TIMEOUT


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, WAIT_TIMEOUT)

    def open_url(self, url):
        self.driver.get(url)

    def wait_for_url(self, url):
        return self.wait.until(EC.url_to_be(url))

    def find_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def fill(self, locator, value):
        element = self.find_visible(locator)
        element.clear()
        element.send_keys(value)
