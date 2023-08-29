from behave import fixture, use_fixture
from selenium import webdriver

@fixture
def browser_chrome(context):
    context.driver = webdriver.Chrome()
    yield context.driver
    context.driver.quit()

def before_all(context):
    use_fixture(browser_chrome, context)

def after_scenario(context, scenario):
    context.driver.quit()
