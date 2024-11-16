''' test api - lastname'''
import requests  # pylint: disable=E0401
import pytest_check as check  # pylint: disable=E0401


def test_api_users():
    """ testing """

    url = "https://reqres.in/api/users/2"

    headers = {}

    response = requests.request("GET", url, headers=headers)
    jsondata = response.json()

    print(jsondata['data']['last_name'])

    check.equal(jsondata['data']['last_name'], 'Weaver')
