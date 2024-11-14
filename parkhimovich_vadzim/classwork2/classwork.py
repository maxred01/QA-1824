import requests
import pytest_check as check


def test_api_users():
    url = "https://reqres.in/api/users/2"
    header = {}
    response = requests.request('GET', url, headers=header)

    check.equal(response.status_code, 200)