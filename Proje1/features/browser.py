from selenium import webdriver


class Browser(object):
    driver = webdriver.Chrome()

    driver.implicitly_wait(10)
    driver.set_page_load_timeout(10)
    driver.maximize_window()

    def close(context):
        context.driver.quit()