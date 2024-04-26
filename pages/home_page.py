from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get('https://www.target.com/')  # Logic to open the Target home page

    def click_sign_in_top_nav(self):
        sign_in_button = self.driver.find_element(By.CSS_SELECTOR, "span.styles__LinkText-sc-1e1g60c-3")
        sign_in_button.click()
