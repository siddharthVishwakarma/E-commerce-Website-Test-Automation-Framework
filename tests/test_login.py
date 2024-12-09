import pytest
from pages.login_page import LoginPage

def test_valid_login(browser):
    login_page = LoginPage(browser)
    login_page.navigate_to_login()
    login_page.login("test_user", "password123")
    assert login_page.is_logged_in()
