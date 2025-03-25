from pages.contacts_page import ContactsPage
from pages.home_page import HomePage
from utils.transliteration import transliterate_to_slug


# 1
def test_contacts(driver):
    home_page = HomePage(driver, "https://saby.ru/")
    home_page.open()
    home_page.open_contacts()

    assert "/contacts" in driver.current_url, f"Unexpected path {driver.current_url}"
    assert "Контакты" in driver.title, f"Unexpected title {driver.title}"


# 2
def test_current_region(driver):
    contacts_page = ContactsPage(driver, "https://saby.ru/contacts/")
    contacts_page.open()
    assert "г. Москва" in driver.title, f"Unexpected title {driver.title}"
    current_region = contacts_page.get_current_region()
    assert current_region == "г. Москва", f"Unexpected region {current_region}"

    partner_list = contacts_page.get_title_of_partners()
    assert len(partner_list) > 1, f"List of partners are empty"


# 3, 4
def test_region_changing(driver):
    contacts_page = ContactsPage(driver, "https://saby.ru/contacts/")
    contacts_page.open()
    old_partner_list = contacts_page.get_title_of_partners()

    new_region = '41 Камчатский край'
    new_region_slug = transliterate_to_slug(new_region)

    contacts_page.change_region_to(new_region)
    current_region = contacts_page.get_current_region()
    assert current_region == "Камчатский край", f"Unexpected region {current_region}"
    assert "Камчатский край" in driver.title, f"Unexpected title {driver.title}"
    assert new_region_slug in driver.current_url, f"Unexpected URL {driver.current_url}"

    new_partner_list = contacts_page.get_title_of_partners()
    assert set(old_partner_list) != set(new_partner_list), "Partners haven't changed"
