from conftest import driver
from locators import SBurgersLocators


class TestSBurgersGoToSectionStuffing:
    def test_go_to_sections_stuffing(self, driver):
        stuffing_button = driver.find_element(*SBurgersLocators.STUFFING_BUTTON).click()
        stuffing_button_activ = driver.find_element(*SBurgersLocators.STUFFING_BUTTON_ACTIV)
        assert 'current' in stuffing_button_activ.get_attribute('class')


class TestSBurgersGoToSectionSauces:
    def test_go_to_sections_sauces(self, driver):
        sauces_button = driver.find_element(*SBurgersLocators.SAUCES_BUTTON).click()
        sauces_button_activ = driver.find_element(*SBurgersLocators.SAUCES_BUTTON_ACTIV)
        assert 'current' in sauces_button_activ.get_attribute('class')


class TestSBurgersGoToSectionBuns:
    def test_go_to_sections_buns(self, driver):
        sauces_button = driver.find_element(*SBurgersLocators.SAUCES_BUTTON).click()
        buns_button = driver.find_element(*SBurgersLocators.BUNS_BUTTON).click()
        buns_button_activ = driver.find_element(*SBurgersLocators.BUNS_BUTTON_ACTIV)
        assert 'current' in buns_button_activ.get_attribute('class')
