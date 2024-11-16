import requests
import pytest_check as check


def test_api_users():

    url = "https://reqres.in/api/unknown"

    headers = {}

    response = requests.request('GET', url, headers=headers)
    data = response.json()

    check.equal(data['total_pages'], 2, "total pages is not 2")
    check.equal(response.status_code, 200, f'статус код не равен 200. Статус код равен {response.status_code}')


def test_api_post_users():

    url = "https://reqres.in/api/users"

    headers = {}

    response = requests.request('PUT', url, headers=headers)
    data = response.json()

    assert 'name' in data, "Напиши нет 'name'"
    assert 'job' in data, "Напиши нет 'job'"
    assert 'id' in data, "Напиши нет 'id'"
    check.equal(response.status_code, 201, f'статус код не равен 201. Статус код равен {response.status_code}')
