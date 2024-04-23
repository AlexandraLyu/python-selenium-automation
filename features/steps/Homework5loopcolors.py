from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('I navigate to "{url}"')
def navigate_to_url(context, url):
    context.driver.get(url)


from behave import when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@when('Loop through colors and verify selection')
def loop_through_colors(context):
    colors = {
        'Light Gray': (By.XPATH, '//img[@alt="Light Gray"]'),
        'Aqua': (By.XPATH, '//img[@alt="Aqua"]'),
        'Gold': (By.XPATH, '//img[@alt="Gold"]'),
        'White': (By.XPATH, '//img[@alt="White"]'),
        'Washed Black': (By.XPATH, '//img[@alt="Washed Black"]')
    }

    display_locators = {
        'Light Gray': (By.XPATH, '//div[contains(text(), "Color") and contains(text(), "Light Gray")]'),
        'Aqua': (By.XPATH, '//div[contains(text(), "Color") and contains(text(), "Aqua")]'),
        'Gold': (By.XPATH, '//div[contains(text(), "Color") and contains(text(), "Gold")]'),
        'White': (By.XPATH, '//div[contains(text(), "Color") and contains(text(), "White")]'),
        'Washed Black': (By.XPATH, '//div[contains(text(), "Color") and contains(text(), "Washed Black")]')
    }

    for color, locator in colors.items():
        select_color(context, locator)
        verify_color_display(context, display_locators[color])


def select_color(context, locator):
    wait = WebDriverWait(context.driver, 20)

    try:
        # Switch to the iframe
        iframe = wait.until(
            EC.frame_to_be_available_and_switch_to_it((By.ID, 'google_ads_iframe_/7079046/tgt/5xtvd/5xtvc/5xtv9_0')))

        # Locate the color element inside the iframe
        color_element = wait.until(EC.element_to_be_clickable(locator))
        print(f"Located the color element: {color_element.get_attribute('alt')}")

        # Click on the color element
        color_element.click()
        print(f"Clicked on the color element: {color_element.get_attribute('alt')}")

        # Switch back to the main content
        context.driver.switch_to.default_content()

        # Wait for the selected color element
        wait.until(EC.visibility_of_element_located(locator))
        print(f"Waiting for the selected color element: {color_element.get_attribute('alt')}")

    except Exception as e:
        print(f"Error occurred while selecting {locator[1]}: {e}")


def verify_color_display(context, locator):
    wait = WebDriverWait(context.driver, 20)

    try:
        display_element = wait.until(EC.visibility_of_element_located(locator))
        print(f"Verified that the color is displayed: {display_element.text}")

    except Exception as e:
        print(f"Error occurred while verifying the display of {locator[1]}: {e}")




from behave import then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from behave import then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@then('Verify when clicking on the color selection the correct color image is displayed')
def step_impl(context):
    colors = ["Light Gray", "Aqua", "Gold", "White", "Washed Black"]

    for color in colors:
        # Click on color
        try:
            color_element = WebDriverWait(context.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f'//img[@alt="{color}"]'))
            )
            color_element.click()
        except Exception as e:
            print(f"Error clicking {color} color: {e}")

        # Verify color image
        try:
            color_image_element = WebDriverWait(context.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f'//img[@alt="{color}"]'))
            )
            assert color_image_element.is_displayed(), f"{color} image is not displayed"
        except Exception as e:
            print(f"Error verifying display of {color} image: {e}")