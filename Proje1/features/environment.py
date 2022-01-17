from features.browser import Browser
from features.pages.category_page import CategoryPage
from features.pages.home_page import HomePage
from features.pages.login_page import LoginPage


def before_all(context):
    context.browser = Browser()
    context.home_page = HomePage()
    context.category_page = CategoryPage()
    context.login_page = LoginPage()


def after_all(context):
    context.browser.close()
