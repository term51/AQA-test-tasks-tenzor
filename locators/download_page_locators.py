from selenium.webdriver.common.by import By


class DownloadPageLocators:
    TAB_PLUGIN_BUTTON = (By.CSS_SELECTOR, "[data-id='plugin']")

    @staticmethod
    def get_web_installer_link_locator(filename):
        return (
            By.XPATH,
            f'//div[contains(@class, "sbis_ru-DownloadNew-block")][.//h3[text()="Веб-установщик "]]//a[contains(@href, "{filename}")]'
        )
