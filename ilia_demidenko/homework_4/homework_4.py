import requests
import pytest_check as check

def test_api_users():
    url = "https://reqres.in/api/users/2"
    headers = {}
    response = requests.request('GET', url, headers=headers)
    check.equal(response.status_code,200)
    ########################################
    data = response.json()
    print(data['data']['last_name'])
    check.equal(data['data']['last_name'],'We123aver', f'surname is not "Weaver" its {response.status_code}')
