import re

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.download_page_locators import DownloadPageLocators
from pages.base_page import BasePage


class DownloadPage(BasePage):
    locators = DownloadPageLocators()

    def download_web_installer_for_windows(self, filename):

        plugin_tab = self.element_is_clickable(self.locators.TAB_PLUGIN_BUTTON)
        plugin_tab.click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.url_contains('tab=plugin'))
        download_link_locator = self.locators.get_web_installer_link_locator(filename)
        web_installer_link = self.element_is_clickable(download_link_locator)
        match = re.search(r"(\d+\.\d+) МБ", web_installer_link.text)
        web_installer_link.click()
        file_size = round(float(match.group(1)), 1)
        return file_size

