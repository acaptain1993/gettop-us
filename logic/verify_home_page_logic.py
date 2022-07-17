from selenium import webdriver
from selenium.webdriver.common.by import By

from time import sleep

# driver initiated
driver = webdriver.Chrome('C:/Users/aaron/Documents/PythonProjects/gettop-us/chromedriver.exe')

# open home page of gettop.us
driver.get('https://gettop.us/')


# select Mac link in the navigation bar
#MAC_NAV_LINK = "a[class = 'nav-top-link'][href*= 'mac']"
MAC_NAV_LINK = "#menu-item-468"

clickable_mac_link = driver.find_element(By.CSS_SELECTOR, MAC_NAV_LINK)
clickable_mac_link.click()

mac_page_verification = driver.find_element(By.CSS_SELECTOR, "nav[class]").text

correct_text = 'HOME / MACBOOK'

assert mac_page_verification == correct_text, f"This {mac_page_verification} is not the correct page. The correct page is {correct_text}"

HOME_LINK = "//a[contains(text(), 'Home')]"
clickable_home_link = driver.find_element(By.XPATH, HOME_LINK)
clickable_home_link.click()

home_page_verification = "span[class = 'section-title-main']"

home_page_elements = len(driver.find_elements(By.CSS_SELECTOR, home_page_verification))

correct_number_of_elements = int(2)

assert correct_number_of_elements == home_page_elements,f"{home_page_elements} should be {correct_number_of_elements}"
sleep(2)
driver.close()
