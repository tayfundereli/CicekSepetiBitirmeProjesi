from selenium.webdriver.common.by import By
from nose.tools import assert_equal, assert_true
from features.browser import Browser


class HomePageLocator(object):
    # Home Page Locators
    POPUP = (By.CLASS_NAME, "js-subheader-close")
    CONTROL_LOGIN = (By.XPATH, "//span[text()='My Account']")
    SUB_MENU_LINKS = (By.CSS_SELECTOR, ".main-submenu__item > a")


class HomePage(Browser):
    # Home Page Actions
    subMenuHrefList = []

    def fill(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def click_element(self, *locator):
        self.driver.find_element(*locator).click()

    def get_text(self, *locator):
        return self.driver.find_element(*locator).text

    def navigate(self, address):
        self.driver.get(address)

    def close_popup(self):
        self.click_element(*HomePageLocator.POPUP)

    def control_login(self):
        actual = self.get_text(*HomePageLocator.CONTROL_LOGIN)
        expected = "My Account"

        assert_equal(actual, expected)

    def count_links(self):
        subMenuList = self.driver.find_elements(*HomePageLocator.SUB_MENU_LINKS)

        for subMenuLink in subMenuList:
            self.subMenuHrefList.append(subMenuLink.get_attribute("href"))

    def control_links(self):
        brokenLinks = []

        for href in self.subMenuHrefList:
            self.driver.get(href)

            if self.driver.title == "Page Not Found!":
                brokenLinks.append(href)
            else:
                assert_true(True)

        print(brokenLinks)

        assert_equal([], brokenLinks)
