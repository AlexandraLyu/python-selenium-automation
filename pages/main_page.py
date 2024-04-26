from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class MainPageLocators:
    SEARCH_INPUT = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    HEADER = (By.CSS_SELECTOR, "[class*='UtilityHeaderWrapper']")
    HEADER_LINKS = (By.CSS_SELECTOR, "a[id*='utilityNav']")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
    SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "h4[class*='StyledHeading']")
    SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='orderPickupButton']")


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    def open_main(self):
        self.driver.get('https://www.target.com/')

    def search_product(self, item):
        self.driver.find_element(*MainPageLocators.SEARCH_INPUT).send_keys(item)
        self.driver.find_element(*MainPageLocators.SEARCH_BTN).click()

    def click_cart(self):
        self.driver.find_element(*MainPageLocators.CART_ICON).click()

    def click_add_to_cart(self):
        self.driver.find_element(*MainPageLocators.ADD_TO_CART_BTN).click()

    def get_header_links_count(self):
        return len(self.driver.find_elements(*MainPageLocators.HEADER_LINKS))

    # Add more methods as needed
