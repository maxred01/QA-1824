'''test api rev 1.2'''

import requests # pylint: disable=E0401
import pytest_check as check # pylint: disable=E0401

def test_api_users():
    '''func test total_pages'''
    url = 'https://reqres.in/api/unknown'

    header = {}

    response = requests.request('GET', url, headers = header)
    find_total_pages = response.json()

    test_total_pages = find_total_pages['total_pages']

    check.equal(response.status_code, 200, f'status code is NOT 200, status code is,'
                                           f'{response.status_code}')

    check.equal(test_total_pages, 2,  f'total_pages is NOT 2, total_pages is,'
                                           f'{test_total_pages}')

def test_api_users_new():
    '''func test new_user'''

    url = 'https://reqres.in/api/users'

    header = {}
    new_users = {
        "name": "Alexei",
        "job": "student"
    }

    response = requests.request('POST', url, headers=header, data=new_users)

    check.equal(response.status_code, 201, f'status code is NOT 201, status code is,'
                                           f'{response.status_code}')

    find_job_and_name = response.json()
    test_job = find_job_and_name['job']
    test_name = find_job_and_name['name']
    check.equal(test_job, 'student', 'job is NOT "student"')
    check.equal(test_name, 'Alexei', 'name is NOT "Alexei"')

    check.is_in("jkhklexei", test_name)