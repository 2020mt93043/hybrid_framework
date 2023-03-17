import time

import pytest

from page.login_page import LoginPage
from page.dashboard_page import DashboardPage
from utilities.base.webdriver_listerner import WebDriverWrapper
from assertpy import assert_that
from selenium.webdriver.common.by import By
from utilities import data_source


class TestLogin(WebDriverWrapper):

    def test_valid_login(self):
        # using page object model we are optimising the code

        # self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        # self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")

        login_page = LoginPage(self.driver)
        login_page.enter_username("Admin")
        login_page.enter_password("admin123")
        login_page.click_on_login()

        # self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        # dashboard_header = self.driver.find_element(By.XPATH, "//h6[normalize-space()='Dashboard']").text

        dashboard_page = DashboardPage(self.driver)
        assert_that("Dashboard").is_equal_to(dashboard_page.get_dashboard_header)

    def test_header_dashboard(self):
        dashboard_header = self.driver.find_element(By.XPATH, "//h6[normalize-space()='Dashboard']").text
        assert_that("Dashboard").is_equal_to(dashboard_header)

    @pytest.mark.parametrize("username, password, expected_error", data_source.test_invalid_login_data)
    def test_invalid_login(self, username, password, expected_error):
        # using page object model we are optimising the code

        # self.driver.find_element(By.NAME, "username").send_keys(username)
        # self.driver.find_element(By.NAME, "password").send_keys(password)
        # self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        login_page = LoginPage(self.driver)
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_on_login()

        # actual_error = self.driver.find_element(By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']").text
        assert_that(expected_error).is_equal_to(login_page.invalid_error_message)

class TestLoginUI(WebDriverWrapper):

    def test_title(self):
        actual_title = self.driver.title
        # assert actual_title == "OrangeHRM"
        # use assertpy to validate the title
        assert_that("OrangeHRM").is_equal_to(actual_title)

    def test_header(self):
        actual_header = self.driver.find_element(By.XPATH, "//h5[normalize-space()='Login']").text
        assert_that("Login").is_equal_to(actual_header)

    def test_login_placeholder(self):
        # updating the code using POM

        login_page = LoginPage(self.driver)

        # actual_username_placeholder = self.driver.find_element(By.NAME, "username").get_attribute("placeholder")
        # actual_password_placeholder = self.driver.find_element(By.NAME, "password").get_attribute("placeholder")

        assert_that("username").is_equal_to(login_page.get_username_placeholder())
        assert_that("password").is_equal_to(login_page.get_password_placeholder())