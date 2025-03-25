from pages.contacts_page import ContactsPage
from pages.home_page import HomePage
from pages.tenzor_about_page import TenzorAboutPage
from pages.tenzor_page import TenzorPage


# 1
def test_contacts(driver):
    home_page = HomePage(driver, "https://saby.ru/")
    home_page.open()
    home_page.open_contacts()

    assert "/contacts" in driver.current_url, f"Unexpected path {driver.current_url}"
    assert "Контакты" in driver.title, f"Unexpected title {driver.title}"


# 2
def test_tenzor_banner(driver):
    contacts_page = ContactsPage(driver, "https://saby.ru/contacts/")
    contacts_page.open()
    contacts_page.click_tenzor_banner()

    assert driver.current_url == "https://tensor.ru/", f"Unexpected URL {driver.current_url}"


# 3, 4, 5
def test_block_strength_in_people(driver):
    tenzor_page = TenzorPage(driver, "https://tensor.ru/")
    tenzor_page.open()
    block_title = tenzor_page.get_title_of_block_strength_in_people()
    assert block_title == "Сила в людях", f"Unexpected title {block_title}"

    tenzor_page.open_about_page()
    assert driver.current_url == "https://tensor.ru/about", f"Unexpected URL {driver.current_url}"


# 6
def test_height_width_of_pictures(driver):
    tenzor_about_page = TenzorAboutPage(driver, "https://tensor.ru/about")
    tenzor_about_page.open()
    title = 'Работаем'
    is_title_exist = tenzor_about_page.is_block_title_exists(title)
    assert is_title_exist, f"Title {title} isn't exist"

    image_sizes = tenzor_about_page.get_block_images(title)
    are_widths_equal = tenzor_about_page.are_widths_equal(image_sizes)
    are_heights_equal = tenzor_about_page.are_heights_equal(image_sizes)

    assert are_widths_equal, f"Widths aren't equal"
    assert are_heights_equal, f"Heights aren't equal"
