from behave import given, then, when
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from support.page_objects import LandingPage, EstimationPage
from selenium.common.exceptions import NoAlertPresentException

MAX_WAIT_TIME = 10

@given('the user is on the landing page')
def step_given_user_on_login_page(context):
    context.driver = webdriver.Chrome()
    context.landing_page = LandingPage(context.driver)
    context.landing_page.open()
    context.initial_url = context.driver.current_url

@when('the user clicks main cta')
def step_when_user_clicks_main_cta(context):
    context.landing_page.clicks_main_cta()

@then('the user should be redirected to the subscription page')
def step_then_user_redirected_to_subscription_page(context):
    subscription_path = '/souscription'
    wait = WebDriverWait(context.driver, MAX_WAIT_TIME)
    wait.until(EC.url_contains(subscription_path))
    context.new_url = context.driver.current_url
    assert subscription_path in context.new_url, "Redirection didn't occur as expected."

@given('the user is on the landing page with a pending estimation')
def step_given_user_on_login_page_with_pending_estimation(context):
    context.driver = webdriver.Chrome()
    context.landing_page = LandingPage(context.driver)
    context.landing_page.open()
    context.initial_url = context.driver.current_url
    context.landing_page.clicks_main_cta()
    context.estimation_page = EstimationPage(context.driver)
    context.estimation_page.clicks_yes_to_first_question()
    context.estimation_page.checks_for_email_input()
    context.driver.back()
    try:
        context.driver.switch_to.alert.accept()
    except NoAlertPresentException:
        print('No alert present')

@when('the user clicks secondary cta')
def step_when_user_clicks_secondary_cta(context):
    context.landing_page.clicks_secondary_cta()

@then('the user should catch up the estimation')
def step_then_user_catch_up_estimation(context):
    wait = WebDriverWait(context.driver, MAX_WAIT_TIME)
    wait.until(EC.url_contains(context.initial_url))
    context.new_url = context.driver.current_url
    assert context.initial_url in context.new_url, "Redirection didn't occur as expected."
    context.estimation_page = EstimationPage(context.driver)
    context.estimation_page.checks_for_search_by_plate()

@when('the user scrolls down to see "Rubrique des guides"')
def step_when_user_scrolls_to_rubrique_des_guides(context):
    target_element = context.driver.find_element(By.XPATH, "//h2[contains(text(), 'Rubrique des guides')]")
    context.driver.execute_script("arguments[0].scrollIntoView();", target_element)


@then('the user should see "Rubrique des guides" on the page')
def step_then_user_should_see_rubrique_des_guides(context):
    target_text = "Rubrique des guides"
    visible_text = context.driver.find_element(By.XPATH, f"//*[contains(text(), '{target_text}')]")
    assert visible_text.is_displayed(), f'"{target_text}" text is not visible on the page.'
