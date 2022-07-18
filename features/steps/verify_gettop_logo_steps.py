from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.common.keys import Keys


BROWSE_CATEGORIES_HEADER = "//span[contains(text(), 'Browse')]"
GETTOP_LOGO = "#logo"


@then('Click GetTop Logo')
def click_gettop_logo(context):
    clickable_logo = context.driver.find_element(By.CSS_SELECTOR, GETTOP_LOGO)
    clickable_logo.click()


@then('Verify Browse Our Categories Text')
def verify_browse_categories(context):
    categories_as_text = context.driver.find_element(By.XPATH, BROWSE_CATEGORIES_HEADER).text
    expected_text = 'BROWSE OUR CATEGORIES'
    assert expected_text == categories_as_text, f"{expected_text}is the expected, instead the text is {categories_as_text}"
    sleep(2)
