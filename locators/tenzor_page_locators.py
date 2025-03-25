from selenium.webdriver.common.by import By


class TenzorPageLocators:
    STRENGTH_IN_PEOPLE_BLOCK_TITLE = (
        By.XPATH, "//p[contains(@class, 'tensor_ru-Index__card-title') and text()='Сила в людях']")
    STRENGTH_IN_PEOPLE_BLOCK_LINK = (
        By.XPATH,
        "//p[contains(@class, 'tensor_ru-Index__card-title') and text()='Сила в людях'] /following-sibling::p//a[@href='/about']"
    )
