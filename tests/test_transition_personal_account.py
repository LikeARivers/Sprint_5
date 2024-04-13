from conftest import driver
from locators import SBurgersLocators
from settings import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestSBurgersTransitionPersonalAccount:

    def test_authorization_forgot_password(self, driver):
        personal_area_button = driver.find_element(*SBurgersLocators.PERSONAL_ACCOUNT_BUTTON_MAIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((SBurgersLocators.ENTER_TEXT)))
        current_url = driver.current_url
        assert current_url == URL_LOGIN
