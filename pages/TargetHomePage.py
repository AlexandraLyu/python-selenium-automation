from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TargetHomePage:
    SIGN_IN_TOP_NAV = (By.XPATH, "//button[text()='Sign In']")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://www.target.com/")

    def click_sign_in_top_nav(self):
        sign_in_top_nav = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SIGN_IN_TOP_NAV)
        )
        sign_in_top_nav.click()
