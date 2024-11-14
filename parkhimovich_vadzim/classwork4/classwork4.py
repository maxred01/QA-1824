import requests
import pytest_check as check


# def test_api_users():
#     url = "https://reqres.in/api/users/2"
#     header = {}
#     response = requests.request('GET', url, headers=header)
#     data = response.json
#
#     print(['data']['last_name'])
#
# check.equal(response.status_code, 200, f'Статус кода не равен 200б Статус кода равен{response.status_code}')
# check.equal(data.['data']['total_page'],"Weaver", f'Фамилия не равна "Weaver". Фамилия равна{data.['data']['total_page']}')


# def test_api_post_users():
#     url = "https://reqres.in/api/users"
#     header = {}
#     data = {
#         "name": "ingi",
#         "job": "brewer"
#     }
#     response = requests.request('POST', url, headers=header, data=data)
#
#     print(response.status_code)
#     print(response.json())


def test_api_post_users():
    url = "https://reqres.in/api/users"
    header = {}
    data = {
        "name": "ingi",
        "job": "brewer"
    }
    response = requests.request('POST', url, headers=header, data=data)

    print(response.json())


check.equal(data.['data']['job'], "taylor", f'Работа не равна "brewer". Работа равна {data.["data"]["job"]}')