"""test api"""

import requests #pylint: disable=E0401
import pytest_check as check #pylint: disable=E0401

def test_api_users():
    """Function"""
    url = "https://reqres.in/api/users/2"

    headers = {}

    response = requests.request("GET", url, headers=headers)

    print(response.status_code)

    check.equal(response.status_code, 200, f'стастус код не равен 200. Статус код равен,'
                                           f' {response.status_code}')
