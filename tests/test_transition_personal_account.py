from conftest import driver
from locators import SBurgersLocators
import time

class TestSBurgersTransitionPersonalAccount:

    def test_authorization_forgot_password(self, driver):
        personal_area_button = driver.find_element(*SBurgersLocators.PERSONAL_ACCOUNT_BUTTON_MAIN).click()
        time.sleep(1)
        current_url = driver.current_url
        assert current_url == 'https://stellarburgers.nomoreparties.site/login'
        driver.quit()