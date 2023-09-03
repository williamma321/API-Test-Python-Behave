import os
from behave import fixture, use_fixture
import requests
import base64
from dotenv import load_dotenv

load_dotenv()

get_session_url = os.getenv("S_ID_URL")
get_call_url = os.getenv("LIB_BASE_URL")
myUserName = os.getenv("LIB_USER_NAME")
myPwd = os.getenv("LIB_PWD")

auth_str = '%s:%s' % (myUserName, myPwd)
byte_str = auth_str.encode('ascii')
b64_auth_str = base64.b64encode(byte_str)
base64_message = b64_auth_str.decode('ascii')


@fixture
def before_all(context):
    headers = {'Authorization': 'Basic %s' % base64_message, 'Accept': 'application/json'}
    content_res = requests.get(get_session_url, headers=headers)
    t_response = content_res.json()
    context.sessionId = t_response
    context.url = get_call_url
    context.shared_header = headers
