from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TermsAndConditionsPage:
    def __init__(self, driver):
        self.driver = driver

    def verify_terms_and_conditions_opened(self):
        # Switch to the newly opened window
        new_window = WebDriverWait(self.driver, 10).until(EC.new_window_is_opened)
        self.driver.switch_to.window(new_window)

        # Verify that the terms and conditions page is opened
        assert "Terms and Conditions" in self.driver.title