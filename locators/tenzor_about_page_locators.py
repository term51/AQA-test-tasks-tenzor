from selenium.webdriver.common.by import By


class TenzorAboutPageLocators:
    @staticmethod
    def block_header(title):
        return By.XPATH, f"//h2[contains(@class, 'tensor_ru-About__block-title') and text()='{title}']"

    @staticmethod
    def block_images(title):
        return (
            By.XPATH,
            f"//h2[contains(@class, 'tensor_ru-About__block-title') and text()='{title}']/ancestor::div[contains(@class, 'tensor_ru-About__block3')]//img"
        )
