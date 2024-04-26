from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, NoSuchElementException

class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_overlay_to_disappear(self):
        # Implement the wait logic for overlay if necessary
        pass

    def click_tazo_green_tea_label(self):
        try:
            # Wait for any overlay to disappear
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.CSS_SELECTOR, '.styles__PubAdWrapper-sc-1ro03th-0.fHrqLw'))
            )

            # Scroll down to the Tazo green tea label
            tazo_green_tea_label = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-test="product-title"]'))
            )
            tazo_green_tea_label.click()

        except (TimeoutException, ElementClickInterceptedException, NoSuchElementException) as e:
            print(f"Error clicking on the Tazo green tea label: {e}")

    def click_product(self, product_name):
        try:
            # Refresh the element locator to handle stale element reference
            product_link = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, f"//a[contains(text(), '{product_name}')]"))
            )
            product_link.click()

        except (TimeoutException, ElementClickInterceptedException, NoSuchElementException) as e:
            print(f"Error clicking on the product {product_name}: {e}")

    def click_add_to_cart(self):
        try:
            add_to_cart_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '//button[@data-test="orderPickupButton"]'))
            )
            add_to_cart_button.click()

        except (TimeoutException, ElementClickInterceptedException, NoSuchElementException) as e:
            print(f"Error clicking on the Add to Cart button: {e}")

    def close_modal(self):
        try:
            close_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "styles__StyledButton-sc-18jd2v4-0 hevCoJ styles__StyledBaseIconButton-sc-136p0tp-0 gqNUiT")]'))
            )
            close_button.click()

        except (TimeoutException, ElementClickInterceptedException, NoSuchElementException) as e:
            print(f"Error clicking on the close button: {e}")

    def get_subtotal(self):
        try:
            subtotal_element = WebDriverWait(self.driver, 40).until(
                EC.visibility_of_element_located((By.XPATH, '//span[@data-test="subtotal"]'))
            )

            return subtotal_element.text

        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error getting the subtotal: {e}")
