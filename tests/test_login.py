import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pathlib import Path

from page_objects.login_page import LoginPage
from page_objects.logout_page import LogoutPage


class TestLoginPage:
    @pytest.mark.login
    @pytest.mark.positive
    def test_tc_001_login_success(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.naviagte_to_login_page()
        login_page.login_user(username="student", password='Password123')

        logout_page = LogoutPage(driver)
        from time import sleep
        sleep(5)
        assert logout_page.is_logout_button_displayed(), "Logout button not displayed"
        assert logout_page.expected_url == login_page.current_url, "Actual Url and expected are not same"
        assert logout_page.get_header_text() == "Congratulations student. You successfully logged in!"


