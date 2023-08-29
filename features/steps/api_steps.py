import requests
from behave import then, when

DUMMY_API_BASE_URL = "https://dummyjson.com"

@when('I make a GET request to "{endpoint}"')
def step_when_get_request(context, endpoint):
    context.response = requests.get(f"{DUMMY_API_BASE_URL}{endpoint}")
    
@then('the response status code should be {status_code:d}')
def step_then_status_code(context, status_code):
    assert context.response.status_code == status_code, f"Expected status code {status_code}, but got {context.response.status_code}"
    
@then('the response body should contain "{text}"')
def step_then_response_body(context, text):
    assert text in context.response.text, f"Expected '{text}' to be in the response body"

@when('I make a POST request to "/todos/add" with the following JSON payload')
def step_when_post_request_add(context):
    payload = context.text
    headers = {'Content-Type': 'application/json'}
    context.response = requests.post(f"{DUMMY_API_BASE_URL}/todos/add", data=payload, headers=headers)
