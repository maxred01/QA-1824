import requests
import pytest_check as check


def test_api_users():
    url = "https://reqres.in/api/unknown"
    headers = {}
    response = requests.request('GET', url, headers=headers)
    data = response.json()
    print(data)
    check.equal(data['total_pages'], 2)
    check.equal(response.status_code, 200)


def test_api_post_users():
    url = "https://reqres.in/api/users"
    headers = {}
    result = requests.get('https://reqres.in/api/users')
    data = {
        "name": "morpheus",
        "job": "hero",
        "id": "611"
          }
    response = requests.request('POST', url, headers=headers, data=data)
    print(response.status_code)
    print(response.json())
    print(result.text)