from selenium.webdriver.common.by import By
from pages.base_page import Page


class TermsAndConditionsPage(Page):
    TC_LINK = (By.XPATH, "//a[contains(text(), 'Target terms and conditions')]")

    def open_sign_in_page(self):
        sign_in_url = 'https://www.target.com/login?client_id=ecom-web-1.0.0&ui_namespace=ui-default&back_button_action=browser&keep_me_signed_in=true&kmsi_default=false&actions=create_session_signin'
        self.driver.get(sign_in_url)

    def open_terms_and_conditions_page(self):
        self.open('https://www.target.com/c/terms-conditions/-/N-4sr7l')

    def click_tc_link(self):
        self.click(*self.TC_LINK)

    def verify_tc_opened(self):
        self.verify_partial_url('terms-conditions/')
