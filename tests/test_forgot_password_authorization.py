from conftest import driver
from locators import SBurgersLocators
from data import SBurgersTestData
import time

class TestSBurgersAuthorizationForgotPassword:

    def test_authorization_forgot_password(self, driver):
        personal_area_button = driver.find_element(*SBurgersLocators.PERSONAL_ACCOUNT_BUTTON_MAIN).click()
        restore_password_button = driver.find_element(*SBurgersLocators.RESTORE_PASSWORD_BUTTON).click()
        authorization_button_restore_password = driver.find_element(*SBurgersLocators.AUTHORIZATION_BUTTON_RESTORE_PASSWORD).click()
        authorization_input_email = driver.find_element(*SBurgersLocators.AUTHORIZATION_INPUT_EMAIL).send_keys(*SBurgersTestData.REGISTRATION_EMAIL)
        authorization_input_password = driver.find_element(*SBurgersLocators.AUTHORIZATION_INPUT_PASSWORD).send_keys(*SBurgersTestData.REGISTRATION_PASSWORD_6_NUMBERS)
        authorization_login_button = driver.find_element(*SBurgersLocators.AUTHORIZATION_LOGIN_BUTTON).click()
        time.sleep(1)
        current_url = driver.current_url
        assert current_url == 'https://stellarburgers.nomoreparties.site/'
        driver.quit()