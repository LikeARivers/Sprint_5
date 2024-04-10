from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from conftest import driver
from locators import SBurgersLocators
from data import SBurgersTestData


class TestSBurgersRegistration:

    def test_registration(self, driver):
        personal_area_button = driver.find_element(*SBurgersLocators.PERSONAL_ACCOUNT_BUTTON_MAIN).click()
        registration_button = driver.find_element(*SBurgersLocators.REGISTRATION_BUTTON).click()
        registration_input_name = driver.find_element(*SBurgersLocators.REGISTRATION_INPUT_NAME).send_keys(*SBurgersTestData.REGISTRATION_NAME)
        registration_input_email = driver.find_element(*SBurgersLocators.REGISTRATION_INPUT_EMAIL).send_keys(*SBurgersTestData.REGISTRATION_EMAIL)
        registration_input_password = driver.find_element(*SBurgersLocators.REGISTRATION_INPUT_PASSWORD).send_keys(*SBurgersTestData.REGISTRATION_PASSWORD_6_NUMBERS)
        registration_finish_button = driver.find_element(*SBurgersLocators.REGISTRATION_FINISH_BUTTON).click()
        WebDriverWait(driver, 6).until(expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/login"))
        current_url = driver.current_url
        assert current_url == "https://stellarburgers.nomoreparties.site/login"
        driver.quit()