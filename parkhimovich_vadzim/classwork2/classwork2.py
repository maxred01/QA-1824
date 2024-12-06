import requests
import pytest_check as check

def test_api_users():
    url = "https://reqres.in/api/users?page=2"
    headers = {}
    response = requests.request("GET",url, headers=headers)
    data = response.json()
    print(data['page'])
    check.equal(data['page'],2)