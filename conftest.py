import pytest
from pathlib import Path
from selenium import webdriver

BASE_DIR = Path("__file__").resolve().parent
CHROME_PATH = str(BASE_DIR.joinpath("resource")) + "\chromedriver.exe"


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(executable_path=CHROME_PATH)
    driver.implicitly_wait(15)
    driver.maximize_window()
    yield driver
    driver.quit()
