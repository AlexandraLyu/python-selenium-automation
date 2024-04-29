from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SignInPage:
    def __init__(self, driver):
        self.driver = driver

    def open_sign_in_page(self):
        # Navigate to target.com
        self.driver.get('https://www.target.com')

        try:
            # Click the sign-in icon in the right navigation
            sign_in_icon = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@aria-label='Account, sign in']")))
            sign_in_icon.click()

            # Wait for the sign-in page to load
            # WebDriverWait(self.driver, 10).until(
            #     EC.visibility_of_element_located((By.XPATH, "//h1[contains(@class, 'styles__AuthHeading')]/span[text()='Sign into your Target account']")))

            # Click on the sign-in link
            sign_in_link = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='accountNav-signIn']")))
            sign_in_link.click()

        except TimeoutException:
            print("TimeoutException occurred. Could not find or interact with the sign-in icon.")

    def get_current_window(self):
        # Return the current window handle
        return self.driver.current_window_handle

    def click_tc_link(self):
        try:
            # Click on the "Target terms and conditions" link
            tc_link = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Target terms and conditions")))
            tc_link.click()

        except TimeoutException:
            print("TimeoutException occurred. Could not find or interact with the terms and conditions link.")

    def switch_to_new_window(self):
        try:
            # Get the handles of all windows
            handles = self.driver.window_handles

            # Switch to the new window
            new_window_handle = [handle for handle in handles if handle != self.original_window][0]
            self.driver.switch_to.window(new_window_handle)
        except Exception as e:
            print("Failed to switch to the newly opened window:", e)

    def verify_tc_opened(self):
        try:
            # Check if the title of the current page contains "Terms & Conditions"
            assert "Terms & Conditions" in self.driver.title, "Terms and Conditions page is not opened"
            print("Terms and Conditions page is opened successfully")
        except AssertionError as e:
            print(e)

    def close_and_return_to_original(self, original_window):
        try:
            # Close the current window
            self.driver.close()
            # Switch back to the original window
            self.driver.switch_to.window(original_window)
            print("Closed new window and switched back to original window successfully")
        except Exception as e:
            print("An error occurred while closing and returning to original window:", e)

