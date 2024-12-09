from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def navigate(self, url):
        self.driver.get(url)

    def click(self, locator):
        WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(locator)).click()

    def send_keys(self, locator, value):
        WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator)).send_keys(value)

    def get_text(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator)).text
