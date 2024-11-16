'''test api rev 1.1'''
import requests # pylint: disable=E0401
import pytest_check as check # pylint: disable=E0401


def test_api_users():
    '''func test last_name'''
    url = 'https://reqres.in/api/users/2'

    header = {}

    response = requests.request('GET', url, headers = header)
    find_last_name = response.json()

    test_last_name = find_last_name['data']['last_name']

    check.equal(response.status_code, 200, f'status code is NOT 200, status code is,'
                                           f'{response.status_code}')

    check.equal(test_last_name, 'Weaver', 'last_name in not "Weaver"')
