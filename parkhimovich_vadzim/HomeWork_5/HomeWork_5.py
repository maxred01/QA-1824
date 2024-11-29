import requests
import pytest_check as check

def test_api_post_register():
    url = "https://reqres.in/api/register"

    data = {}

    headers = {}

    response = requests.request("POST",url, headers=headers, data=data)
    data_response = response.json()
    response_id = data_response['id']

    check.equal(response.status_code, 200)
    check.greater(int(response_id),)
    check.equal(data_response)
    check.equal(data_response)