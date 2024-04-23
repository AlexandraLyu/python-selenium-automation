from behave import given, when, then
from time import sleep
from selenium.webdriver.common.by import By

SEARCH_INPUT = (By.ID, 'search')


@given('I open Target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when('I search for green tea')
def search_product(context):
    context.driver.find_element(*SEARCH_INPUT).send_keys('green tea')
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(6)


@then( 'I verify search results are shown for green tea')
def verify_search_results(context):
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert 'green tea' in actual_text, f'Error! text green tea not in {actual_text}'
