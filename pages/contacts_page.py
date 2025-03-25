from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

from locators.contacts_page_locators import ContactsPageLocators
from pages.base_page import BasePage
from utils.transliteration import transliterate_to_slug


class ContactsPage(BasePage):
    locators = ContactsPageLocators()

    def click_tenzor_banner(self):
        banner = self.element_is_clickable(self.locators.TENZOR_BANNER)
        banner.click()
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[1])
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("tensor.ru")
        )

    def get_current_region(self):
        current_region = self.element_is_visible(self.locators.CURRENT_REGION)
        return current_region.text if current_region else None

    def get_title_of_partners(self):
        partners = self.elements_are_visible(self.locators.PARTNER_ITEMS)
        partner_names = []

        for partner in partners:
            try:
                name = partner.find_element(By.CSS_SELECTOR, ".sbisru-Contacts-List__name")
                partner_names.append(name.text)

            except NoSuchElementException:
                continue

        return partner_names

    def change_region_to(self, region):
        self.element_is_clickable(self.locators.CURRENT_REGION).click()
        locator = self.locators.get_region_locator(region)
        wait = WebDriverWait(self.driver, 10)
        found_region = wait.until(EC.element_to_be_clickable(locator))
        ActionChains(self.driver).move_to_element(found_region).pause(2).click().perform()
        wait.until(
            EC.url_contains(transliterate_to_slug(region))
        )
