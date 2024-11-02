"""test status code"""

import requests # pylint: disable=E0401
import pytest_check as check # pylint: disable=E0401

def test_api_users():
    """Work functions"""
    url = "https://reqres.in/api/user/2"

    headers = {}

    response = requests.request('GET', url, headers=headers)

    print(response.status_code)

    check.equal(response.status_code, 200, f'status code is NOT 200, status code is,'
                                           f'{response.status_code}')
