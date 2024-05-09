from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class TargetSignInPage(Page):
    EMAIL_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login")
    ERROR_MESSAGE = (By.XPATH, "//div[contains(text(), 'Sorry, something went wrong. Please try again')]")




    def open_target_sign_in_page(self):
        # Navigate to target.com
        self.driver.get('https://www.target.com')

        try:
            # Click the sign-in icon in the right navigation
            sign_in_icon = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@aria-label='Account, sign in']")))
            sign_in_icon.click()

            # Click on the sign-in link
            sign_in_link = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='accountNav-signIn']")))
            sign_in_link.click()

        except TimeoutException:
            print("TimeoutException occurred. Could not find or interact with the sign-in icon.")

    def enter_credentials(self, email, password):
        self.input_text(email, *self.EMAIL_INPUT)
        self.input_text(password, *self.PASSWORD_INPUT)

    def click_login_button(self):
        login_button = self.find_element(*self.LOGIN_BUTTON)
        login_button.click()

    def is_element_displayed(self, by_locator):
        try:
            element = self.driver.find_element(*by_locator)
            return element.is_displayed()
        except NoSuchElementException:
            return False

    def verify_error_message_displayed(self):
        return self.is_element_displayed(self.ERROR_MESSAGE)