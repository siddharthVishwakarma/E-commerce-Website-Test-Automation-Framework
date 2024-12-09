from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    LOGIN_INPUT = (By.ID, "login")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def navigate_to_login(self):
        self.navigate("https://example-ecommerce.com/login")

    def login(self, username, password):
        self.send_keys(self.LOGIN_INPUT, username)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def is_logged_in(self):
        # Assuming a successful login redirects to a dashboard
        return "dashboard" in self.driver.current_url
