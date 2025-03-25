import os

from selenium.webdriver.support.wait import WebDriverWait

from pages.download_page import DownloadPage
from pages.home_page import HomePage


# 1, 2
def test_open_local_versions(driver):
    home_page = HomePage(driver, "https://saby.ru/")
    home_page.open()
    home_page.open_download_local_versions()

    assert "/download" in driver.current_url, f"Unexpected path {driver.current_url}"
    assert "Скачать Saby (СБИС) и дополнительное ПО" in driver.title, f"Unexpected title {driver.title}"


# 3, 4, 5
def test_download_plugin_for_windows(driver):
    download_page = DownloadPage(driver, "https://saby.ru/download")
    download_page.open()

    filename = "sbisplugin-setup-web.exe"
    expected_size = download_page.download_web_installer_for_windows(filename)

    download_path = os.path.join(os.getcwd(), "tests", "downloads")
    file_path = os.path.join(download_path, filename)

    WebDriverWait(driver, 30, poll_frequency=1).until(lambda _: os.path.exists(file_path))
    assert os.path.exists(file_path), f"File {filename} wasn't found in {download_path}"

    actual_size_bytes = os.path.getsize(file_path)
    actual_size_mb = round(actual_size_bytes / (1024 * 1024), 1)
    assert actual_size_mb == expected_size, f"File size {actual_size_mb} MB does not match the expected size {expected_size} "
