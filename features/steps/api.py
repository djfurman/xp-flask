from behave import given, when, then
import requests

BASE_PATH = "http://localhost:5000"


@when(u'a GET request to "{path}"')
def get_request_to_relative_path(context, path):
    context.response = requests.get(f"{BASE_PATH}{path}")


@then(u'the response status code should be "{response_code}"')
def assert_response_code(context, response_code):
    assert context.response.status_code == int(response_code)


@then(u'the response header "{header_key}" should be "{header_value}"')
def assert_header_key_value(context, header_key, header_value):
    assert context.response.headers[header_key.lower()] == header_value.lower()


@then(u'the json response body should show "{key}"')
def assert_json_key_in_response_body(context, key):
    assert key in context.response.json().keys()
