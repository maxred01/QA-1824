import requests
import pytest_check as check
import pytest
import allure


@allure.feature('Проверка апи')
def test_api_users():
    url = "https://reqres.in/api/users/2"

    headers = {}

    response = requests.request('GET', url, headers=headers)
    data = response.json()

    with allure.step('Проверка статус кода'):
        check.equal(response.status_code, 200, f'статус код не равен 200. Статус код равен {response.status_code}')

    with allure.step('Проверка фамилии'):
        check.equal(data['data']['last_name'], 'We2121aver',
                    f'Фамилия не равна "Weaver". Фамилия равна {data["data"]["last_name"]}')


def test_api_post_users():
    url = "https://reqres.in/api/users"

    name = "max"
    job = "teacher"

    data = {
        "name": name,
        "job": job
    }

    headers = {}

    response = requests.request('POST', url, headers=headers, data=data)
    data_respons = response.json()
    respons_id = data_respons['id']

    check.equal(response.status_code, 201)

    check.equal(data_respons['name'], name)
    check.equal(data_respons['job'], job)
    check.greater(int(respons_id), 620)
    check.is_not_none(data_respons['createdAt'])
