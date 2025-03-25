from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators.tenzor_page_locators import TenzorPageLocators
from pages.base_page import BasePage


class TenzorPage(BasePage):
    locators = TenzorPageLocators()

    def get_title_of_block_strength_in_people(self):
        return self.element_is_visible(self.locators.STRENGTH_IN_PEOPLE_BLOCK_TITLE).text

    def open_about_page(self):
        self.element_is_clickable(self.locators.STRENGTH_IN_PEOPLE_BLOCK_LINK).click()
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("/about")
        )
