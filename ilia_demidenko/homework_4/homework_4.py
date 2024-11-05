import requests
import pytest_check as check

def test_api_users():
    url = "https://reqres.in/api/users?page=2"
    headers = {}
    response = requests.request('GET', url, headers=headers)
    check.equal(response.status_code,200)


    # json_data = response.json()
    # check.equal(response.json('data'),('last_name'))
    #
    # url = 'https://reqres.in/api/users?page=2'
    # headers = {}
    # response = requests.get(url, headers=headers)
    # check.equal(json_data('data')('last_name'), 'Weaver')
