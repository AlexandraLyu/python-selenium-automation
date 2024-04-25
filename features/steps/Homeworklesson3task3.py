from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I am on the website')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.target.com")

@when('I click on the Sign In button')
def step_impl(context):
    # Wait for the Sign In button to be clickable
    sign_in_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#headerPrimary > a.styles__PrimaryHeaderLink-sc-8s5b77-1.styles__StyledLinkNamedIcon-sc-1e1g60c-1.eLNniN.ddVUKA > span"))
    )
    # Click on the Sign In button
    sign_in_button.click()

@when('I click on the Sign In link from the right side navigation menu')
def step_impl(context):
    # Wait for the Sign In link from the right side navigation menu to be clickable
    sign_in_link = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#listaccountNav-signIn > a > span"))
    )
    # Click on the Sign In link from the right side navigation menu
    sign_in_link.click()

@then('I should see the Sign In form opened')
def step_impl(context):
    # Wait for the Sign In form to be visible
    sign_in_form = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#__next > div > div > div > div.styles__ContentWrapper-sc-19gc5cv-1.CpfGf > div > form"))
    )
    assert sign_in_form.is_displayed()



