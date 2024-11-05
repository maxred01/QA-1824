import requests
import pytest_check as check
import pytest


def test_api_users():
    url = "https://reqres.in/api/users/2"

    headers = {}

    response = requests.request('GET', url, headers=headers)
    data = response.json()

    check.equal(response.status_code, 200, f'статус код не равен 200. Статус код равен {response.status_code}')
    check.equal(data['data']['last_name'], 'We2121aver',
                f'Фамилия не равна "Weaver". Фамилия равна {data["data"]["last_name"]}')


def test_api_post_users():
    url = "https://reqres.in/api/users"

    headers = {}
    data = {
        "name": "max",
        "job": "teacher"
    }

    response = requests.request('POST', url, headers=headers, data=data)

    (print(response.status_code))
    (print(response.json()))
