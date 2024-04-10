from conftest import driver
from locators import SBurgersLocators
from data import SBurgersTestData


class TestSBurgersRegistration:

    def test_registration(self, driver):
        personal_area_button = driver.find_element(*SBurgersLocators.PERSONAL_ACCOUNT_BUTTON_MAIN).click()
        registration_button = driver.find_element(*SBurgersLocators.REGISTRATION_BUTTON).click()
        registration_input_name = driver.find_element(*SBurgersLocators.REGISTRATION_INPUT_NAME).send_keys(*SBurgersTestData.REGISTRATION_NAME)
        registration_input_email = driver.find_element(*SBurgersLocators.REGISTRATION_INPUT_EMAIL).send_keys(*SBurgersTestData.REGISTRATION_EMAIL)
        registration_input_password = driver.find_element(*SBurgersLocators.REGISTRATION_INPUT_PASSWORD).send_keys(*SBurgersTestData.REGISTRATION_PASSWORD_5_NUMBERS)
        registration_finish_button = driver.find_element(*SBurgersLocators.REGISTRATION_FINISH_BUTTON).click()
        assert driver.find_element(*SBurgersLocators.INCORRECT_PASSWORD_ELEMENT).text == 'Некорректный пароль'
