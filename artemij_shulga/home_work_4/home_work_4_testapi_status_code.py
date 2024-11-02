''' test api - status_code'''


import requests  # pylint: disable=E0401
import pytest_check as check  # pylint: disable=E0401


def test_api_users():
    """ testing """

    url = "https://reqres.in/api/users/2"

    headers = {}

    response = requests.request('GET', url, headers=headers)

    print(response.status_code)

    check.equal(response.status_code, 200,
                f'статус код не равен 200. Статус код равен {response.status_code}')
