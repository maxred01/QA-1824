import requests
import pytest_check as check


def test_api_users():
    url = "https://reqres.in/api/users?page=2"

    headers = {}

    response = requests.request('GET', url, headers=headers)
    data = response.json()

    print(data['page'])
    check.equal(data['page'], 4)

    print(response.status_code)

    # assert response.status_code == 200

    check.equal(response.status_code, 202, f'статус код не равен 200. Статус код равен {response.status_code}')
    print(response)
