''' test api - status_code/total_pages '''


import requests  # pylint: disable=E0401
import pytest_check as check  # pylint: disable=E0401


def test_api_users():
    """ testing """

    url = "https://reqres.in/api/unknown"

    headers = {}

    response = requests.request('GET', url, headers=headers)

    result = response.json()

    print(response.status_code)

    print(result['total_pages'])

    check.equal(result['total_pages'], 2)

    check.equal(response.status_code, 200,
                f'статус код не равен 200. Статус код равен {response.status_code}')


def test_api_post_users():
    """ testing """

    url = "https://reqres.in/api/users"

    headers = {}

    info = {
    "name": "artemij",
    "job": "prime leader"
    }

    response = requests.request('POST', url, headers=headers, data=info)

    print(response.status_code)
    print(response.json())



def test_api_post_one_users():
    """ testing """

    url = "https://reqres.in/api/users"

    headers = {}

    info = {
    "name": "artemij",
    "job": "prime leader"
    }

    response = requests.request('POST', url, headers=headers, data=info)

    test_name = response.json()

    test_job = response.json()

    print(test_name['name'])
    print(test_job['job'])
    print(response.status_code)

    check.equal(test_name['name'], "artemij",
                f'Имя не равен "artemij". Имя равен artemij {test_name["name"]}')
    check.equal(test_job['job'], "prime leader",
                f'Рабона не равна "prime leader". Имя равна prime leader {test_job["job"]}')
    check.equal(response.status_code, 201,
                f'статус код не равен 200. Статус код равен {response.status_code}')
