import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function')
def driver():
    download_path = os.path.join(os.getcwd(), "tests", "downloads")
    prefs = {
        "download.default_directory": download_path,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    }
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("prefs", prefs)

    service = Service(executable_path=ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()
