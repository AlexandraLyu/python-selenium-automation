from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SignInPageLocators:
    SIGN_IN_RIGHT_NAV = (By.CSS_SELECTOR, "[data-test='accountNav-signIn']")
    SIGN_IN_FORM = (
    By.XPATH, "//h1[contains(@class, 'styles__AuthHeading')]/span[text()='Sign into your Target account']")


class SignInPage:
    def __init__(self, driver):
        self.driver = driver

    def click_sign_in_right_nav(self):
        sign_in_right_nav = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(SignInPageLocators.SIGN_IN_RIGHT_NAV)
        )
        sign_in_right_nav.click()

    def verify_sign_in_form_opened(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(SignInPageLocators.SIGN_IN_FORM)
        )

    def open(self):
        try:
            self.click_sign_in_right_nav()
            self.verify_sign_in_form_opened()
        except TimeoutException:
            print("Sign-in link is not clickable within the timeout period.")
