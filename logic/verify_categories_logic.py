from selenium import webdriver
from selenium.webdriver.common.by import By

from time import sleep

# driver initiated
driver = webdriver.Chrome('C:/Users/aaron/Documents/PythonProjects/gettop-us/chromedriver.exe')

# open home page of gettop.us
driver.get('https://gettop.us/')


# verify the browse categories
BROWSE_CATEGORIES_HEADER = "//span[contains(text(), 'Browse')]"
categories_as_text = driver.find_element(By.XPATH, BROWSE_CATEGORIES_HEADER).text
expected_text = 'BROWSE OUR CATEGORIES'
assert expected_text == categories_as_text, f"{expected_text}is the expected, instead the text is {categories_as_text}"

# verify four categories names
ACCESSORIES_HEADER = "//h5[contains(text(), 'Accessories')]"
accessories_text = driver.find_element(By.XPATH, ACCESSORIES_HEADER).text
expected_list = ['ACCESSORIES', 'IPAD', 'IPHONE', 'MACBOOK']
FOUR_CATEGORIES = "//h5[contains(text(), '')]"
selected_categories = driver.find_elements(By.XPATH, FOUR_CATEGORIES)
HOME_LINK = "//a[contains(text(), 'Home')]"
result_category_names = []
print(selected_categories)
for category in selected_categories:
    category.click()
    current_page_name = driver.find_element(By.CSS_SELECTOR, "nav[class]").text
    #result_category_names += [current_page_name]
    clickable_home_link = driver.find_element(By.XPATH, HOME_LINK)
    clickable_home_link.click()

print(result_category_names)


driver.close()
