from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import StaleElementReferenceException


SEARCH_INPUT = (By.ID, 'search')
ADD_TO_CART_BUTTON = (By.ID, 'addToCartButtonOrTextIdFor14778867')

@given('Open Target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')

@when('Search for green tea Tazo')
def search_product(context):
    context.driver.find_element(*SEARCH_INPUT).send_keys('green tea Tazo')
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(6)


#@then('Click on Tazo green tea label')
def click_tazo_green_tea_label(context):
    print("Waiting for Tazo green tea label...")
    try:
        # Wait for the overlay to disappear
        WebDriverWait(context.driver, 20).until_not(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.ReactModal__Overlay'))
        )

        print("Overlay disappeared. Waiting for Tazo green tea label...")

        # Wait for the Tazo green tea label to be clickable
        tazo_green_tea_label = WebDriverWait(context.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        '#pageBodyContainer > div > div:nth-child(1) > div > div:nth-child(4) > div > div.styles__ProductListGridFadedLoading-sc-j2atyg-0 > section > div > div:nth-child(1) > div > div > div.styles__ImageAndInfoWrapper-sc-hztu6c-3.jNBVOy > div.styles__StyledProductCardBody-sc-9lksuw-0.igyNQi > div > div > div.styles__ProductCardItemInfoDiv-sc-14ktig2-0.enMoTF > div.h-display-flex.h-flex-justify-space-between > div.styles_truncate__lcCbH.styles__Truncate-sc-1wcknu2-0.dsImrp > a'))
        )

        print("Tazo green tea label is clickable. Clicking...")

        # Click on the Tazo green tea label
        tazo_green_tea_label.click()

    except Exception as e:
        print(f"Error: {e}")
        raise


#@then('Click on the name Tazo Green Tea Matcha Latte')
def click_tazo_green_tea_matcha_latte(context):
    try:
        print("Clicking on Tazo Green Tea Matcha Latte label...")

        # Wait for the element to be clickable
        tazo_green_tea_matcha_latte_label = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, 'a[href="/p/tazo-green-tea-matcha-latte-32-fl-oz/-/A-12954578#lnk=sametab"]'))
        )

        tazo_green_tea_matcha_latte_label.click()

        print("Verifying Add to Cart button or text is present...")

        # Wait for the Add to Cart button or text to be present
        add_to_cart_button_or_text = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'addToCartButtonOrTextIdFor12954578'))
        )

        assert add_to_cart_button_or_text.is_displayed(), "Add to Cart button or text is not present"

    except StaleElementReferenceException:
        print("Element is stale. Retrying...")
        # You can implement a retry mechanism here
        # e.g., by calling the same function again or refreshing the page

    except Exception as e:
        print(f"Error: {e}")
        raise


#@then('Click on Add to Cart button')
def click_add_to_cart_button(context):
    try:
        print("Clicking on Add to Cart button...")

        # Wait for the commercial banner to disappear
        try:
            WebDriverWait(context.driver, 10).until(
                EC.invisibility_of_element_located((By.ID, 'google_ads_iframe_/7079046/tgt/5xt1a/5xt0r/4yi5o_0'))
            )
            print("Commercial banner disappeared.")
        except TimeoutException:
            print("Commercial banner did not disappear. Continuing...")

        # Locate the Add to Cart button
        add_to_cart_button = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'addToCartButtonOrTextIdFor12954578'))
        )

        # Click the Add to Cart button
        add_to_cart_button.click()

    except NoSuchElementException as e:
        print(f"Element not found: {e}")
        raise
    except TimeoutException as e:
        print(f"Timeout waiting for element: {e}")
        raise
    except Exception as e:
        print(f"Error: {e}")
        raise


#@then('Click X button')
def click_x_button(context):
    # Locate the button by aria-label
    close_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="close"]'))
    )
    close_button.click()


#@then('Click on the cart button')
def click_cart_button(context):
    # Define the locator
    locator = (By.CSS_SELECTOR, 'a[data-test="@web/CartLink"]')

    try:
        # Wait for the element to be clickable and click it
        cart_button = WebDriverWait(context.driver, 20).until(
            EC.element_to_be_clickable(locator)
        )
        cart_button.click()

    except TimeoutException:
        # Add a more descriptive error message
        print("Timed out waiting for the cart button to be clickable. The button might not be present or interactable.")
        raise


#@then('Verify subtotal is $5.19')
def verify_subtotal(context):
    locator = (By.CSS_SELECTOR, 'span.styles__CartSummarySpan-sc-odscpb-3.jaXVgU')

    try:
        # Wait for the subtotal element to be visible
        subtotal_element = WebDriverWait(context.driver, 40).until(
            EC.visibility_of_element_located(locator)
        )

        # Get the text of the subtotal element
        subtotal_text = subtotal_element.text

        # Assert that the subtotal is $5.19
        assert "$5.19" in subtotal_text, f"Expected subtotal $5.19, but found {subtotal_text}"

    except TimeoutException:
        print("Timed out waiting for the subtotal element to be visible or it might not be present on the page.")
        raise
    except NoSuchElementException:
        print("The subtotal element was not found on the page.")
        raise
    except Exception as e:
        print(f"An error occurred: {e}")
        raise
