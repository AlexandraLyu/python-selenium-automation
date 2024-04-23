from behave import given, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

@given('Open Target Circle page')
def open_target_circle_page(context):
    context.driver.get('https://www.target.com/circle')


@then('Verify there are 6 benefit boxes')
def verify_benefit_boxes_count(context):
    # Find all benefit boxes on the page using the provided selectors
    benefit_box_selectors = [
        "#__next > div.max-width-slingshot-container > div > div > div.styles__StyledGrid-sc-8k32oi-0.styles__GridStyledForSlotRenderer-sc-1weaxkp-0.yMGkH.bevkHo > div:nth-child(7) > div > div > div:nth-child(1) > div:nth-child(1) > a > div > div.styles__CellItemCopy-sc-3f68hg-7.dAbAee",
        "#__next > div.max-width-slingshot-container > div > div > div.styles__StyledGrid-sc-8k32oi-0.styles__GridStyledForSlotRenderer-sc-1weaxkp-0.yMGkH.bevkHo > div:nth-child(7) > div > div > div:nth-child(1) > div:nth-child(2) > a > div > div.styles__CellItemCopy-sc-3f68hg-7.dAbAee",
        "#__next > div.max-width-slingshot-container > div > div > div.styles__StyledGrid-sc-8k32oi-0.styles__GridStyledForSlotRenderer-sc-1weaxkp-0.yMGkH.bevkHo > div:nth-child(7) > div > div > div:nth-child(1) > div:nth-child(3) > a > div > div.styles__CellItemCopy-sc-3f68hg-7.dAbAee",
        "#__next > div.max-width-slingshot-container > div > div > div.styles__StyledGrid-sc-8k32oi-0.styles__GridStyledForSlotRenderer-sc-1weaxkp-0.yMGkH.bevkHo > div:nth-child(7) > div > div > div:nth-child(2) > div:nth-child(1) > a > div > div.styles__CellItemCopy-sc-3f68hg-7.dAbAee",
        "#__next > div.max-width-slingshot-container > div > div > div.styles__StyledGrid-sc-8k32oi-0.styles__GridStyledForSlotRenderer-sc-1weaxkp-0.yMGkH.bevkHo > div:nth-child(7) > div > div > div:nth-child(2) > div:nth-child(2) > a > div > div.styles__CellItemCopy-sc-3f68hg-7.dAbAee",
        "#__next > div.max-width-slingshot-container > div > div > div.styles__StyledGrid-sc-8k32oi-0.styles__GridStyledForSlotRenderer-sc-1weaxkp-0.yMGkH.bevkHo > div:nth-child(7) > div > div > div:nth-child(2) > div:nth-child(3) > a > div > div.styles__CellItemCopy-sc-3f68hg-7.dAbAee"
    ]

    # Wait for the benefit boxes to be present
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, benefit_box_selectors[0]))
    )

    # Check if there are exactly 6 benefit boxes present on the page
    for selector in benefit_box_selectors:
        try:
            benefit_box = context.driver.find_element(By.CSS_SELECTOR, selector)
        except NoSuchElementException:
            assert False, f"Expected to find 6 benefit boxes, but couldn't find one with selector: {selector}"
