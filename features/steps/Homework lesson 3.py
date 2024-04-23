from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I am on the target.com website')
def step_impl(context):
    # Initialize Chrome WebDriver
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.target.com")

@when('I click on the Cart icon')
def step_impl(context):
    # Wait for the Cart icon to be clickable
    cart_icon = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#headerPrimary > a.styles__PrimaryHeaderLink-sc-8s5b77-1.styles__CartLink-sc-jff2tp-0.eLNniN.iqZQhg > div > svg"))
    )
    # Click on the Cart icon
    cart_icon.click()

@then('I should see the message "Your cart is empty"')
def step_impl(context):
    # Wait for the "Your cart is empty" message to appear
    empty_cart_message = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#cart-container > div.styles__StyledDiv-sc-fw90uk-0.gYsXNb.h-padding-a-default > div > div > div:nth-child(2)"))
    )
    assert empty_cart_message.text == "Your cart is empty"

    # Close the browser
    context.driver.quit()

