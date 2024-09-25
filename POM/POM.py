# 1.Page Classes: For each web page in the application, there is a corresponding page class. This class contains the locators for the web elements on that page and methods to interact with them.
# 2.Separation of Concerns: The test logic is separated from the page-specific code, making the tests more readable and maintainable.
# 3.Reusability: Page methods can be reused across multiple test cases, reducing redundancy.

import unittest
from selenium import webdriver
from login_page import LoginPage

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://example.com/login")
        self.login_page = LoginPage(self.driver)

    def test_login(self):
        self.login_page.enter_username("user")
        self.login_page.enter_password("password")
        self.login_page.click_login()
        # Add assertions to verify successful login

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()