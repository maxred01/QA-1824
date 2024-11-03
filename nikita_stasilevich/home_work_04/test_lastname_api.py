"""test last name"""

import requests # pylint: disable=E0401
import pytest_check as check # pylint: disable=E0401

def test_api_users():
    """functions Check last name"""
    url = "https://reqres.in/api/user/2"

    headers = {}

    response = requests.request('GET', url, headers=headers)
    jsondata=response.json()

    print(response.status_code)

    check.equal(jsondata['data']['last_name'],'Weaver')
