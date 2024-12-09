from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

def get_browser(browser_name):
    if browser_name.lower() == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser_name.lower() == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        raise ValueError(f"Browser {browser_name} is not supported")
    driver.maximize_window()
    return driver
