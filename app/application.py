from pages.Basepage import Page
from pages.Header import Header
from pages.MainPage import MainPage
from pages.ProductPage import ProductPage
from pages.SearchResultsPage import SearchResultsPage
from pages.sign_in_page import SignInPage
from pages.TargetHomePage import TargetHomePage


class Application:

    def __init__(self, driver):
        self.base_page = Page(driver)
        self.main_page = MainPage(driver)
        self.header = Header(driver)
        self.search_result_page = SearchResultsPage(driver)
        self.product_page = ProductPage(driver)
        self.sign_in_page = SignInPage(driver)
        self.home_page = TargetHomePage(driver)


