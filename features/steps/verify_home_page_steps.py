from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.common.keys import Keys


MAC_NAV_LINK = "#menu-item-468"
HOME_LINK = "//a[contains(text(), 'Home')]"


@given('Gettop Home Page')
def gettop_home(context):
    context.driver.get('https://gettop.us/')


@when('Mac Link is Clicked')
def mac_link_clicked(context):
    clickable_mac_link = context.driver.find_element(By.CSS_SELECTOR, MAC_NAV_LINK)
    clickable_mac_link.click()
    sleep(2)


@when('Mac Page is Verify')
def mac_page_verified(context):
    mac_page_verification = context.driver.find_element(By.CSS_SELECTOR, "nav[class]").text
    correct_text = 'HOME / MACBOOK'
    assert mac_page_verification == correct_text, f"This {mac_page_verification} is not the correct page. The correct page is {correct_text}"


@then('Home Button is Clicked')
def home_button_clicked(context):
    clickable_home_link = context.driver.find_element(By.XPATH, HOME_LINK)
    clickable_home_link.click()


@then('Home Page is Verified')
def home_page_verified(context):
    home_page_verification = "span[class = 'section-title-main']"

    home_page_elements = len(context.driver.find_elements(By.CSS_SELECTOR, home_page_verification))

    correct_number_of_elements = int(2)

    assert correct_number_of_elements == home_page_elements, f"{home_page_elements} should be {correct_number_of_elements}"
    sleep(2)
    context.driver.close()
