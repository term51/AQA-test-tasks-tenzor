from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage


class HomePage(BasePage):
    locators = HomePageLocators()

    def open_contacts(self):
        self.element_is_clickable(self.locators.HEADER_MENU_CONTACTS_LINK).click()
        self.element_is_clickable(self.locators.MORE_OFFICES_LINK).click()

    def open_download_local_versions(self):
        self.element_is_clickable(self.locators.DOWNLOAD_LOCAL_VERSIONS_LINK).click()
