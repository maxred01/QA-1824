import requests
import pytest_check as check

def test_api_users():
    url = "https://reqres.in/api/users/2"
    headers = {}
    response= requests.request('GET', url, headers=headers)
    data = response.json()

    check.equal(data['data']['last_name'],'Weaver',
    f'фамилия не равна "Weaver", фамилия равна{data['data']['last_name']}')

    check.equal(response.status_code, 200,
    f'статус код не равен 200, статус код равен {response.status_code}')
