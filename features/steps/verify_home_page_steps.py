from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.common.keys import Keys


MAC_NAV_LINK = "#menu-item-468"
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
    pass


@then('Home Button is Clicked')
def home_button_clicked(context):
    pass


@then('Home Page is Verified')
def home_page_verified(context):
    pass

