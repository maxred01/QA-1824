"""test total pages"""
import requests  # pylint: disable=E0401
import pytest_check as check  # pylint: disable=E0401


def test_api_users():
    """functions Check total pages"""
    url = "https://reqres.in/api/unknown"

    headers = {}

    response = requests.request('GET', url, headers=headers)

    find_json = response.json()

    test_json_pages = find_json['total_pages']

    print(response.status_code)

    check.equal(test_json_pages, 2, "total pages is not 2")

    check.equal(response.status_code, 200, f'status code is NOT 200, status code is,'
                                           f'{response.status_code}')


def test_api_post_users():
    url = "https://reqres.in/api/users"

    headers = {}
    data = {
        "name": "Nikita",
        "job": "president"
    }

    response = requests.request("POST", url, headers=headers, data=data)

    find_json = response.json()

    test_json_name = find_json["name"]

    check.equal(response.status_code, 201, f'стастус код не равен 201. Статус код равен {response.status_code}')

    check.equal(test_json_name, "Nikita", "total pages is not Nikita")


