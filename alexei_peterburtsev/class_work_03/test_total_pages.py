'''Alexei Peterburtsev test'''
import requests  # pylint: disable=E0401
import pytest_check as check  # pylint: disable=E0401


def test_api_users():
    '''func test total_pages'''
    url = 'https://reqres.in/api/unknown'

    header = {}

    response = requests.request('GET', url, headers=header)
    find_total_pages = response.json()

    test_total_pages = find_total_pages['total_pages']

    check.equal(response.status_code, 200, f'status code is NOT 200, status code is,'
                                           f'{response.status_code}')

    check.equal(test_total_pages, 2, f'total_pages is NOT 2, total_pages is,'
                                     f'{test_total_pages}')


def test_api_users_new():
    '''func test new_user'''

    url = 'https://reqres.in/api/users'

    user_name = "Alexei"
    user_job = "Student"

    header = {}
    new_users = {
        "name": user_name,
        "job": user_job
    }

    response = requests.request('POST', url, headers=header, data=new_users)

    check.equal(response.status_code, 201, f'status code is NOT 201, status code is,'
                                           f'{response.status_code}')

    user_data = response.json()

    check.not_equal(user_data['name'], user_data['job'], 'FAIL. "Name" = "Job".')
    check.is_not_none(user_data['createdAt'], 'FAIL. "createdAt" is EMPTY')
