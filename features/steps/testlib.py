from behave import given, when, then
import requests
import json
from jsonschema import validate
from features.steps.utils import get_json_data


@given(u'the endpoint {endpoint}')
def step_impl(context, endpoint):
    context.url = context.url + endpoint


@given(u'param {parameter}')
def step_impl(context, parameter):
    if parameter == 'default':
        context.url = context.url + '?session_id=' + context.sessionId


@when(u'method get')
def step_impl(context):
    context.response = requests.get(context.url, headers=context.shared_header)
    print(context.url)
    print(context.response)


@then(u'the response status is {response_status}')
def step_impl(context, response_status):
    assert int(context.response.status_code) == int(response_status)


@then(u'the response matches {response_schema} schema')
def step_impl(context, response_schema):
    expected_response = get_json_data("../schemas/", response_schema)
    response_content = json.loads(context.response.content)
    validate(instance=response_content, schema=expected_response)

