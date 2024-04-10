from selenium import webdriver
import settings
import pytest

@pytest.fixture(scope='function')
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get(settings.URL)
    return chrome_driver