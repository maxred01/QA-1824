import requests
import pytest_check as check


def test_api_users():
    url = 'https://reqres.in/api/users?page=2`'
    headers = {}
    response = requests.request('GET', url, headers=headers)

    print(response.status_code)

    assert response.status_code == 200
    check.equal(response.status_code, 200)
