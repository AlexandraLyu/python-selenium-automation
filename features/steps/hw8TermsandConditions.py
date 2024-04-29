from behave import given, when, then

@given('Open sign in page')
def open_sign_in_page(context):
    context.app.sign_in_page.open_sign_in_page()


@when('Store original window')
def store_original_window(context):
    context.original_window = context.app.sign_in_page.get_current_window()


@when('Click on Target terms and conditions link')
def click_tc_link(context):
    context.app.sign_in_page.click_tc_link()

@when('Switch to the newly opened window')
def switch_window(context):
    context.app.sign_in_page.switch_to_new_window()

@then('Verify Terms and Conditions page is opened')
def verify_tc_opened(context):
    context.app.sign_in_page.verify_tc_opened()

@then('User can close new window and switch back to original')
def close_and_return(context):
    context.app.sign_in_page.close_and_return_to_original(context.original_window)
