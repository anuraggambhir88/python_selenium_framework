from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePageFactory


class LogoutPage(BasePageFactory):
    __page_url = "https://practicetestautomation.com/logged-in-successfully/"
    __page_title = (By.CLASS_NAME, "post-title")
    __congrats_text = (By.XPATH, "//p/strong")
    __logout_button = (By.XPATH, "//a[contains(@href,'/practice-test-login/')]")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def expected_url(self) -> str:
        return self.__page_url

    def get_header_text(self) -> str:
        return super()._get_text(self.__congrats_text)

    def is_logout_button_displayed(self) -> bool:
        return super()._is_displayed(self.__logout_button)

