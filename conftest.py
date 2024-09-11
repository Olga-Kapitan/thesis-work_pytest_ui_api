import pytest
from selenium import webdriver


@pytest.fixture()
def chrome_browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(3)
    browser.maximize_window()
    yield browser

    browser.quit()
