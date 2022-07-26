import allure
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
# from app.application import Application


# Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
bs_user = 'aaroncaptain_7Hv5Vj'
bs_pw = '1pHy8HX5opTQxMduwkVp'

# Allure command:
# behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/product_page.feature


def browser_init(context, test_name):
    """
    :param context: Behave context
    """
    # context.driver = webdriver.Chrome(executable_path='C:/Users/aaron/Documents/PythonProjects/python-selenium-automation/chromedriver.exe')
    # context.browser = webdriver.Safari()
    # context.browser = webdriver.Firefox(executable_path='C:/Users/aaron/Documents/PythonProjects/gettop-us/geckodriver.exe')



# Headless Enabled
    #options = webdriver.ChromeOptions()
    #options.add_argument('headless')
    #context.driver = webdriver.Chrome(chrome_options=options, executable_path='C:/Users/aaron/Documents/PythonProjects/python-selenium-automation/chromedriver.exe')

    ### for browerstack ###
    desired_cap = {
        "browserName": "chrome",
        "browserVersion": "103.0",
        "os": "Windows",
        "osVersion": "10",
        'name': test_name
     }
    url = f'http://{bs_user}:{bs_pw}@hub-cloud.browserstack.com/wd/hub'
    context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, timeout=10)
    #context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
