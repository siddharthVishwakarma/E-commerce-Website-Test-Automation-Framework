import pytest
import json
from utils.browser_manager import get_browser

@pytest.fixture(scope="function")
def browser():
    # Load config
    with open("config/config.json") as config_file:
        config = json.load(config_file)

    driver = get_browser(config["browser"])
    driver.get(config["base_url"])
    yield driver
    driver.quit()
