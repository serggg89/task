import requests
from models import InvalidCredentialsResponse
from constants import *


def test_01_authorization_with_wrong_credentials():
    resp = requests.post(url=BASE_URL + AUTH_ENDPOINT, data=INVALID_CREDENTIALS.to_json())
    # first of all we check response status code
    assert resp.status_code == UNAUTHORIZED_STATUS_CODE
    actual_response = InvalidCredentialsResponse(resp.json())
    # check actual and expected response
    assert actual_response == EXPECTED_RESPONSE
