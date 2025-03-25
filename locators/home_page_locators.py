from selenium.webdriver.common.by import By


class HomePageLocators:
    HEADER_MENU_CONTACTS_LINK = (By.CSS_SELECTOR, ".sbisru-Header-ContactsMenu")
    MORE_OFFICES_LINK = (By.XPATH, "//div[contains(@class, 'sbisru-Header-ContactsMenu__items')]//a[@href='/contacts']")
    DOWNLOAD_LOCAL_VERSIONS_LINK = (
        By.XPATH, "//a[contains(@class, 'sbisru-Footer__link') and text()='Скачать локальные версии']"
    )
