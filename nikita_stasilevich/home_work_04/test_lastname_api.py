"""test_lastname_api"""

import requests # pylint: disable=E0401
import pytest_check as check # pylint: disable=E0401


def test_api_users():
    """functions Check last name"""
    url = "https://reqres.in/api/users/2"

    headers = {}

    response = requests.request('GET', url, headers=headers)

    find_json=response.json()
    test_json_lastname=find_json['data']['last_name']

    print(response.status_code)

    check.equal(test_json_lastname,'Weaver',"Last name is Weaver")

    check.equal(response.status_code, 200, f'status code is NOT 200, status code is,'
                                           f'{response.status_code}')
