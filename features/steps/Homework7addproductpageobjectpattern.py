from behave import given, when, then
from selenium import webdriver
from pages.MainPage import MainPage
from pages.ProductPage import ProductPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException


@given('Navigate to Target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')
    context.app.main_page = MainPage(context.driver)
    context.app.main_page.open_main()


@when('Search for Tazo green tea')
def search_product(context):
    context.app.main_page.search_product('green tea Tazo')


@then('Click on green tea Tazo label')
def click_tazo_green_tea_label(context):
    context.app.product_page = ProductPage(context.driver)
    context.app.product_page.click_tazo_green_tea_label()


@then('Click on the name Tazo Green Tea')
def click_tazo_green_tea_matcha_latte(context):
    context.app.product_page.click_product('Tazo Green Tea Matcha Latte')


@then('Click on Add to Cart button')
def click_add_to_cart_button(context):
    context.app.product_page.click_add_to_cart()


@then('Click X button')
def click_x_button(context):
    context.app.product_page.close_modal()


# @then('Click on the cart button')
def click_cart_button(context):
    context.app.main_page.click_cart()


@then('Click on the cart button from main page')
def click_cart_button_from_main_page(context):
    locator = (By.CSS_SELECTOR, 'a[data-test="@web/CartLink"]')

    try:
        cart_button = WebDriverWait(context.driver, 20).until(
            EC.element_to_be_clickable(locator)
        )
        cart_button.click()

    except TimeoutException:
        print("Timed out waiting for the cart button to be clickable. The button might not be present or interactable.")
        raise


@then("Verify subtotal {amount}")
def verify_subtotal(context, amount):
    locator = (By.XPATH, '//span[contains(@class, "styles__CartSummarySpan-sc-odscpb-3 jaXVgU")]')

    try:
        # Wait for the subtotal element to be visible
        subtotal_element = WebDriverWait(context.driver, 40).until(
            EC.visibility_of_element_located(locator)
        )

        # Get the text of the subtotal element
        subtotal_text = subtotal_element.text

        # Assert that the subtotal is $3.99
        assert str(amount) in subtotal_text, f"Expected subtotal $3.99, but found {subtotal_text}"

    except TimeoutException:
        print("Timed out waiting for the subtotal element to be visible or it might not be present on the page.")
        raise
    except NoSuchElementException:
        print("The subtotal element was not found on the page.")
        raise
    except Exception as e:
        print(f"An error occurred: {e}")
        raise
