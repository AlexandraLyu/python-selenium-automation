from behave import given, when, then
from selenium.webdriver.common.by import By
from pages.Target_Sign_In_Page import TargetSignInPage



@given('User opens the Target sign in page')
def open_target_sign_in_page(context):
    context.app.target_sign_in_page.open_target_sign_in_page()


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@when('User enters incorrect email and password combination')
def enter_invalid_credentials(context):
    # Wait for the email input field to be clickable
    email_input = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable(TargetSignInPage.EMAIL_INPUT)
    )
    # Once the email input field is clickable, enter the email
    email_input.send_keys("incorrect@example.com")

    # Locate and enter password (assuming it's not required to wait for it to be clickable)
    password_input = context.driver.find_element(*TargetSignInPage.PASSWORD_INPUT)
    password_input.send_keys("Incorrectpassword!")


@when('User clicks the login button')
def click_login_button(context):
    login_button = context.driver.find_element(*TargetSignInPage.LOGIN_BUTTON)
    login_button.click()

@then('Verify that the message "Sorry, something went wrong. Please try again." is shown')
def verify_error_message(context):
    assert context.app.target_sign_in_page.verify_error_message_displayed(), "Error message is not displayed"

#@then('Verify that the message "Sorry, something went wrong. Please try again." is shown')
#def verify_error_message(context):
#    assert context.app.target_sign_in_page.verify_error_message_displayed(), "Error message is not displayed"



