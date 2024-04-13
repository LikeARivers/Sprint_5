from conftest import driver
from locators import SBurgersLocators
from data import SBurgersTestData
from settings import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestSBurgersExit:

    def test_authorization_forgot_password(self, driver):
        personal_area_button = driver.find_element(*SBurgersLocators.PERSONAL_ACCOUNT_BUTTON_MAIN).click()
        authorization_input_email = driver.find_element(*SBurgersLocators.AUTHORIZATION_INPUT_EMAIL).send_keys(*SBurgersTestData.AUTHARIZATION_EMAIL)
        authorization_input_password = driver.find_element(*SBurgersLocators.AUTHORIZATION_INPUT_PASSWORD).send_keys(*SBurgersTestData.REGISTRATION_PASSWORD_6_NUMBERS)
        authorization_login_button = driver.find_element(*SBurgersLocators.AUTHORIZATION_LOGIN_BUTTON).click()
        personal_area_button = driver.find_element(*SBurgersLocators.PERSONAL_ACCOUNT_BUTTON_MAIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((SBurgersLocators.EXIT_BUTTON)))
        exit_button = driver.find_element(*SBurgersLocators.EXIT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((SBurgersLocators.ENTER_TEXT)))
        current_url = driver.current_url
        assert current_url == URL_LOGIN
