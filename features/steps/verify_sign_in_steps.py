from behave import given, when, then
from pages.home_page import HomePage
from pages.sign_in_page import SignInPage

@given('the user is on the Target home page')
def open_target(context):
    context.driver.get('https://www.target.com/')
    context.home_page = HomePage(context.driver)  # Instantiate the HomePage object
    context.home_page.open()

@when('the user clicks on Sign In from the top navigation')
def step_impl_when(context):
    context.home_page.click_sign_in_top_nav()

@then('the user clicks on Sign In from the right side navigation')
def step_impl_then(context):
    context.sign_in_page = SignInPage(context.driver)
    context.sign_in_page.click_sign_in_right_nav()

@then('the Sign In form should be opened')
def step_impl_then(context):
    context.sign_in_page = SignInPage(context.driver)  # Instantiate the SignInPage object
    context.sign_in_page.verify_sign_in_form_opened()

