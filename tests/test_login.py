import time
from assertpy import assert_that
from selenium import webdriver


class TestLoginUI:
    def test_title(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(20)
        driver.get("https://opensource-demo.orangehrmlive.com/")
        actual_title = driver.title
        time.sleep(5)
        # assert actual_title == "OrangeHRM"
        # use assertpy to validate the title
        assert_that("OrangeHRM").is_equal_to(actual_title)