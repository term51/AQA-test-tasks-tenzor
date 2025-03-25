from selenium.webdriver.common.by import By


class ContactsPageLocators:
    TENZOR_BANNER = (By.CSS_SELECTOR, "#contacts_clients a[title='tensor.ru']")
    CURRENT_REGION = (By.XPATH, "(//span[contains(@class, 'sbis_ru-Region-Chooser__text')])[1]")
    PARTNER_ITEMS = (By.CSS_SELECTOR, "#contacts_list [data-qa='item']")

    @staticmethod
    def get_region_locator(region):
        return (
            By.XPATH,
            f"//li[contains(@class,'sbis_ru-Region-Panel__item')]//span[text()='{region}']"
        )
