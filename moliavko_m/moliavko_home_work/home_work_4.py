import requests
import pytest_check as check


def test_api_users():

    url = "https://reqres.in/api/user/2"
    headers = {}
    response = requests.request('GET', url, headers=headers)
    print(response.status_code)
    check.equal(response.status_code, 200, f'статус код не равен 200, статуст код равен{response.status_code}')
