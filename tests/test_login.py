from base.webdriver_listerner import WebDriverWrapper
from assertpy import assert_that
from selenium.webdriver.common.by import By


class TestLogin(WebDriverWrapper):
    def test_valid_login(self):
        self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        dashboard_header = self.driver.find_element(By.XPATH, "//h6[normalize-space()='Dashboard']").text
        assert_that("Dashboard").is_equal_to(dashboard_header)

    # def test_header_dashboard(self):
    #     dashboard_header = self.driver.find_element(By.XPATH, "//h6[normalize-space()='Dashboard']").text
    #     assert_that("Dashboard").is_equal_to(dashboard_header)

# class TestLoginUI:
#
#     def test_title(self):
#         actual_title = self.driver.title
#         # assert actual_title == "OrangeHRM"
#         # use assertpy to validate the title
#         assert_that("OrangeHRM").is_equal_to(actual_title)
#
#     def test_header(self):
#         actual_header = self.driver.find_element(By.XPATH, "//h5[normalize-space()='Login']").text
#         assert_that("Login").is_equal_to(actual_header)
