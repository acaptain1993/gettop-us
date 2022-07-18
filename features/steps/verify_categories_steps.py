from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.common.keys import Keys

BROWSE_CATEGORIES_HEADER = "//span[contains(text(), 'Browse')]"
ACCESSORIES_HEADER = "//h5[contains(text(), 'Accessories')]"
IPAD_HEADER = "//h5[contains(text(), 'iPad')]"
IPHONE_HEADER = "//h5[contains(text(), 'iPhone')]"
MACBOOK_HEADER = "//h5[contains(text(), 'MacBook')]"
HOME_LINK = "//a[contains(text(), 'Home')]"
CURRENT_LOCATION = "nav.breadcrumbs"


@when('Browse Our Categories Text is Verified')
def verify_our_categories_text(context):

    categories_as_text = context.driver.find_element(By.XPATH, BROWSE_CATEGORIES_HEADER).text
    expected_text = 'BROWSE OUR CATEGORIES'
    assert expected_text == categories_as_text, f"{expected_text}is the expected, instead the text is {categories_as_text}"


@when('Verify 4 Correct Categories are Shown')
def verify_each_category(context):
    accessories_text = context.driver.find_element(By.XPATH, ACCESSORIES_HEADER).text
    ipad_text = context.driver.find_element(By.XPATH, IPAD_HEADER).text
    iphone_text = context.driver.find_element(By.XPATH, IPHONE_HEADER).text
    macbook_text = context.driver.find_element(By.XPATH, MACBOOK_HEADER).text
    expected_list = ['ACCESSORIES', 'IPAD', 'IPHONE', 'MACBOOK']
    result_list = [accessories_text, ipad_text, iphone_text, macbook_text]
    assert expected_list == result_list, f"Expected list is {expected_list} but instead the list is {result_list}"


@then('Click Each Category and Verify the Correct Page Opened')
def click_and_verify_category(context):
    clickable_accessories = context.driver.find_element(By.XPATH, ACCESSORIES_HEADER)
    clickable_ipad = context.driver.find_element(By.XPATH, IPAD_HEADER)
    clickable_iphone = context.driver.find_element(By.XPATH, IPHONE_HEADER)
    clickable_macbook = context.driver.find_element(By.XPATH, MACBOOK_HEADER)
    expected_current_location_accessories = 'HOME / ACCESSORIES'
    expected_current_location_ipad = 'HOME / IPAD'
    expected_current_location_iphone = 'HOME / IPHONE'
    expected_current_location_macbook = 'HOME / MACBOOK'

    clickable_accessories.click()
    sleep(2)
    current_location = context.driver.find_element(By.CSS_SELECTOR, CURRENT_LOCATION).text
    assert current_location == expected_current_location_accessories, f"Location is {current_location}, should be {expected_current_location_accessories}"
    click_home = context.driver.find_element(By.XPATH, HOME_LINK)
    click_home.click()

    clickable_ipad.click()
    sleep(2)
    current_location = context.driver.find_element(By.CSS_SELECTOR, CURRENT_LOCATION).text
    assert current_location == expected_current_location_ipad, f"Location is {current_location}, should be {expected_current_location_accessories}"
    click_home = context.driver.find_element(By.XPATH, HOME_LINK)
    click_home.click()

    clickable_iphone.click()
    sleep(2)
    current_location = context.driver.find_element(By.CSS_SELECTOR, CURRENT_LOCATION).text
    assert current_location == expected_current_location_iphone, f"Location is {current_location}, should be {expected_current_location_accessories}"
    click_home = context.driver.find_element(By.XPATH, HOME_LINK)
    click_home.click()

    clickable_macbook.click()
    sleep(2)
    current_location = context.driver.find_element(By.CSS_SELECTOR, CURRENT_LOCATION).text
    assert current_location == expected_current_location_macbook, f"Location is {current_location}, should be {expected_current_location_accessories}"
    click_home = context.driver.find_element(By.XPATH, HOME_LINK)
    click_home.click()
