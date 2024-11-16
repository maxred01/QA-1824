import requests
import pytest_check as check


def test_api_test():
    url = 'https://reqres.in/api/unknown'
    headers = {}
    response = requests.request('GET', url, headers=headers)
    data = response.json()
    print(data['total_pages'])

    check.equal(data['total_pages'], 2, f'total pages not = 2, it"s = {(data["total_pages"])}')


def test_api_post_users():
    url = 'https://reqres.in/api/users'

    headers = {}
    data = {
        "name": "morpheus",
        "job": "leader"
    }

    response = requests.request('POST', url, headers=headers, data=data)

    (print(response.status_code))
    (print(response.json))


def test_api_post_users1():
    url = 'https://reqres.in/api/users'

    headers = {}

    data = {
        "name": "morpheus",
        "job": "leader"
    }

    response = requests.request('POST', url, headers={}, data={})

    check.equal(data['name']['job'], ['name']['job'], f'значение name job не равно morpheus leader, а равно = {(data[data])}')

    (print(response.status_code))
    (print(response.json))
