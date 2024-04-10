from conftest import driver
from locators import SBurgersLocators
from settings import *

class TestSBurgersTransitionConstructor:

    def test_authorization_forgot_password(self, driver):
        personal_area_button = driver.find_element(*SBurgersLocators.PERSONAL_ACCOUNT_BUTTON_MAIN).click()
        constructor_button = driver.find_element(*SBurgersLocators.CONSTRUCTOR_BUTTON).click()
        current_url = driver.current_url
        assert current_url == URL