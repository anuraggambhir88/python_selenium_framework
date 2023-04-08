from selenium import webdriver

from selenium import webdriver
from pathlib import Path

from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

BASE_DIR = Path("__file__").resolve().parent.parent
CHROME_PATH = BASE_DIR.joinpath("resource")


class BasePageFactory:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.browser = "CHROME"
        self.baseURL = "https://automationteststore.com/"

    def get_browser_instance(self):
        if self.browser == "CHROME":
            self.driver = webdriver.Chrome(executable_path=CHROME_PATH)
        else:
            self.driver = webdriver.firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        return self.driver

    def _find(self, locator: tuple) -> WebElement:
        return self.driver.find_element(*locator)

    def _type(self, locator: tuple, text: str, timeout: int = 10):
        self._wait_for_element_visible(locator, timeout)
        self._find(locator).send_keys(text)

    def _wait_for_element_visible(self, locator: tuple, timeout: int = 10):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(ec.visibility_of_element_located(locator))

    def _click(self, locator: tuple, timeout: int = 10):
        self._wait_for_element_visible(locator, timeout)
        self._find(locator).click()

    def _is_displayed(self, locator: tuple) -> bool:
        try:
            return self._find(locator).is_displayed()
        except NoSuchElementException:
            return False

    @property
    def _get_current_url(self) -> str:
        return self.driver.current_url

    def _open_url(self, url: str):
        self.driver.get(url)

    def _get_text(self, locator: tuple, timeout: int = 10) -> str:
        self._wait_for_element_visible(locator, timeout)
        return self._find(locator).text
