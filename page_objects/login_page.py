from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePageFactory


class LoginPage(BasePageFactory):
    BASE_URL = "https://practicetestautomation.com/"
    __username_field = (By.ID, "username")
    __password_field = (By.ID, "password")
    __submit_button = (By.ID, 'submit')
    __practise_link = (By.XPATH, "//a[contains(@href,'/practice/')]")
    __test_login_page_link = (By.LINK_TEXT, "Test Login Page")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.BASE_URL)

    def login_user(self, username, password):
        super()._wait_for_element_visible(self.__username_field,10)
        super()._type(self.__username_field,username,10)
        super()._type(self.__password_field,password)
        super()._click(self.__submit_button)

    @property
    def current_url(self) ->str:
        return super()._get_current_url


    def naviagte_to_login_page(self):
        super()._click(self.__practise_link)
        super()._click(self.__test_login_page_link)

