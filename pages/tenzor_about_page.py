from locators.tenzor_about_page_locators import TenzorAboutPageLocators
from pages.base_page import BasePage


class TenzorAboutPage(BasePage):
    locators = TenzorAboutPageLocators()

    def is_block_title_exists(self, title) -> bool:
        locator = self.locators.block_header(title)

        return self.element_is_visible(locator).text is not None

    def get_block_images(self, title) -> list:
        locator = self.locators.block_images(title)
        images = self.elements_are_visible(locator)

        return [(img.get_attribute("width"), img.get_attribute("height")) for img in images]

    def are_widths_equal(self, image_sizes) -> bool:
        return all(size[0] == image_sizes[0][0] for size in image_sizes)

    def are_heights_equal(self, image_sizes) -> bool:
        return all(size[1] == image_sizes[0][1] for size in image_sizes)
