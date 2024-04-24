from pages.Basepage import Page
from pages.Header import Header
from pages.MainPage import MainPage
from pages.SearchResultsPage import SearchResultsPage


class Application:

    def __init__(self, driver):
        self.base_page = Page(driver)
        self.main_page = MainPage(driver)
        self.header = Header(driver)
        self.search_result_page = SearchResultsPage(driver)