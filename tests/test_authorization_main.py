from conftest import driver
from locators import SBurgersLocators
from data import SBurgersTestData
from settings import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestSBurgersAuthorizationMain:

    def test_authorization_main(self, driver):
        button_authorization_main = driver.find_element(*SBurgersLocators.BUTTON_AUTHORIZATION_MAIN).click()
        authorization_input_email = driver.find_element(*SBurgersLocators.AUTHORIZATION_INPUT_EMAIL).send_keys(*SBurgersTestData.AUTHARIZATION_EMAIL)
        authorization_input_password = driver.find_element(*SBurgersLocators.AUTHORIZATION_INPUT_PASSWORD).send_keys(*SBurgersTestData.REGISTRATION_PASSWORD_6_NUMBERS)
        authorization_login_button = driver.find_element(*SBurgersLocators.AUTHORIZATION_LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((SBurgersLocators.MAKE_BURGER_TEXT)))
        current_url = driver.current_url
        assert current_url == URL