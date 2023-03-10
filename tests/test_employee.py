import time
import pytest
from assertpy import assert_that
from selenium.webdriver.common.by import By
from utilities.base.webdriver_listerner import WebDriverWrapper
from utilities import data_source


class TestAddEmployee(WebDriverWrapper):

    @pytest.mark.parametrize(
        "username, password, file_path", data_source.test_invalid_profile_upload)
    def test_invalid_profile_upload(self, username, password, file_path):
        self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys(username)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        self.driver.find_element(By.XPATH, "//span[normalize-space()='PIM']").click()
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Add Employee']").click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, "//input[@type='file']").send_keys(file_path)
        actual_error = self.driver.find_element(By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message']").text
        assert_that(actual_error).contains("not allowed")

    @pytest.mark.parametrize(
        "username, password, firstname, middlename, lastname, emp_id, expected_profile_header, expected_profile_firstname",
        data_source.test_add_valid_employee)
    def test_add_valid_employee(self, username, password, firstname, middlename, lastname, emp_id,
                                expected_profile_header, expected_profile_firstname):
        self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys(username)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        self.driver.find_element(By.XPATH, "//span[normalize-space()='PIM']").click()
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Add Employee']").click()
        self.driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys(firstname)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Middle Name']").send_keys(middlename)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys(lastname)
        # self.driver.find_element(By.XPATH,
        #                          "//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']").clear()
        # self.driver.find_element(By.XPATH,
        #                          "//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']").click()
        self.driver.find_element(By.XPATH,
                                 "//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']").send_keys(
            emp_id)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
        time.sleep(8)
        actual_profile_header = self.driver.find_element(By.XPATH,
                                                         f"//h6[contains(normalize-space(),'{firstname}')]").text
        actual_first_name = self.driver.find_element(By.XPATH, "//input[@placeholder='First Name']").get_attribute("value")
        assert_that(actual_profile_header).is_equal_to(expected_profile_header)
        assert_that(actual_first_name).is_equal_to(expected_profile_firstname)
