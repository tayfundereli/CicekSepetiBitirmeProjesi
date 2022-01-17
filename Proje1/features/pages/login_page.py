from selenium.webdriver.common.by import By
from features.browser import Browser


class LoginPageLocator(object):
    # Login Page Locators
    USERNAME = (By.ID, "EmailLogin")
    PASSWORD = (By.ID, "Password")
    SUBMIT_BUTTON = (By.CLASS_NAME, "login__btn")


class LoginPage(Browser):
    # Login Page Actions

    def fill(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def click_element(self, *locator):
        self.driver.find_element(*locator).click()

    def get_text(self, *locator):
        return self.driver.find_element(*locator).text

    def navigate(self, address):
        self.driver.get(address)

    def fill_email(self, email):
        self.fill(email, *LoginPageLocator.USERNAME)

    def fill_password(self, password):
        self.fill(password, *LoginPageLocator.PASSWORD)

    def click_submit(self):
        self.click_element(*LoginPageLocator.SUBMIT_BUTTON)