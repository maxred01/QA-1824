''' test api '''
import requests # pylint: disable=E0401
import pytest_check as check # pylint: disable=E0401


def test_api_users():
    """Function work"""
    url = 'https://reqres.in/api/users?page=2'

    header = {}

    response = requests.request('GET', url, headers = header)

    print(response.status_code)

    check.equal(response.status_code, 201, f'status code is NOT 200, status code is,'
                                           f'{response.status_code}')
