from selenium.webdriver.common.by import By
from conftest import driver
from locators import SBurgersLocators
import time

class TestSBurgersGoToSections:

    def test_go_to_sections(self, driver):
        stuffing_button = driver.find_element(*SBurgersLocators.STUFFING_BUTTON).click()
        time.sleep(1)
        assert driver.find_element(By.XPATH, "//h2[text() = 'Начинки']").is_displayed()
        sauces_button = driver.find_element(*SBurgersLocators.SAUCES_BUTTON).click()
        time.sleep(1)
        assert driver.find_element(By.XPATH, "//h2[text() = 'Соусы']").is_displayed()
        buns_button = driver.find_element(*SBurgersLocators.BUNS_BUTTON).click()
        time.sleep(1)
        assert driver.find_element(By.XPATH, "//h2[text() = 'Булки']").is_displayed()



