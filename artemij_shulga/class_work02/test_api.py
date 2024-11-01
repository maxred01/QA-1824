''' test_api '''

import requests
import pytest
import pytest_check as check


def test_api_users():
    url = "https://reqres.in/api/users?page=2"

    headers = {}

    response = requests.request('GET', url, headers=headers)

    print(response.status_code)

    check.equal(response.status_code, 201, f'статус код не равен 200. Статус код равен {response.status_code}')