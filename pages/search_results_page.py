from selenium.webdriver.common.by import By

class SearchResultsPageLocators:
    SEARCH_RESULT_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")
    LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
    PRODUCT_IMG = (By.CSS_SELECTOR, "[class*='ProductCardImage']")

class SearchResultsPage:

    def __init__(self, driver):
        self.driver = driver

    def verify_search_results(self, expected_item):
        actual_text = self.driver.find_element(*SearchResultsPageLocators.SEARCH_RESULT_HEADER).text
        assert expected_item in actual_text, f'Error! Text {expected_item} not in {actual_text}'

    def verify_products_name_img(self):
        # To see ALL listings (comment out if you only check top ones):
        self.driver.execute_script("window.scrollBy(0,2000)", "")
        sleep(4)
        self.driver.execute_script("window.scrollBy(0,2000)", "")

        all_products = self.driver.find_elements(*SearchResultsPageLocators.LISTINGS)

        for product in all_products:
            title = product.find_element(*SearchResultsPageLocators.PRODUCT_TITLE).text
            assert title, 'Product title not shown'
