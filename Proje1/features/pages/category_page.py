from time import sleep
from selenium.webdriver.common.by import By
from nose.tools import assert_equal
from features.browser import Browser

class CategoryPageLocator(object):
    # Category Page Locator
    PRODUCT_COUNT_SELECTOR = (By.CLASS_NAME, "products__item-inner")


class CategoryPage(Browser):
    # Category Page Actions
    PRODUCT_COUNT_PER_PAGE = 60


    def fill(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def click_element(self, *locator):
        self.driver.find_element(*locator).click()

    def get_text(self, *locator):
        return self.driver.find_element(*locator).text

    def navigate(self, address):
        self.driver.get(address)

    def scrollPageTenTimes(self):
        for pageCount in range(9):
            self.scrollToBottomOfPage(pageCount + 2)

    def scrollToBottomOfPage(self, pageCount):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight+999);")

        sleep(3)

        self.getProductCount(pageCount)

    def getProductCount(self, pageCount):
        productList = self.driver.find_elements(*CategoryPageLocator.PRODUCT_COUNT_SELECTOR)

        assert_equal(len(productList), pageCount * self.PRODUCT_COUNT_PER_PAGE)

    def makeScrollBehaviourSmooth(self):
        self.driver.execute_script("document.querySelector('html').style.scrollBehavior = 'smooth'")