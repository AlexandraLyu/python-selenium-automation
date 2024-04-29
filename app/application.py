from pages.base_page import Page
from pages.cart_page import CartPage
from pages.header import Header
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.target_app_page import TargetAppPage
from pages.terms_and_conditions_page import TermsAndConditionsPage
from pages.sign_in_page import SignInPage

class Application:
    def __init__(self, driver):
        self.base_page = Page(driver)
        self.cart_page = CartPage(driver)
        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.search_result_page = SearchResultsPage(driver)
        self.target_app_page = TargetAppPage(driver)
        self.terms_and_conditions_page = TermsAndConditionsPage(driver)
        self.sign_in_page = SignInPage(driver)