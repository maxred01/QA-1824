import pytest_check as check
import requests


def test_api_register_successful():
    url = "https://reqres.in/api/register"

    id = "1"
    name = "cerulean"
    year = "2000"
    color = "#98B2D1"
    pantone_value = "15-4020"
    headers = {}
    email = "test1111@gmail.com"
    password = "1234561111"

    data = {
        "id": id,
        "name": name,
        "year": year,
        "color": color,
        "pantone_value": pantone_value,
        "email": email,
        "password": password
    }

    response = requests.request('POST', url, data=data, headers=headers)
    data_response = response.json()
    print(data_response)

    check.equal(data_response["id"], id)
    check.equal(data_response["name"], name)
    check.equal(data_response['year'], year)
    check.equal(data_response['color'], color)
    check.equal(data_response['pantone_value'], pantone_value)
    check.equal(data_response['total pages'], 2)
    check.equal(data_response['total'], 12)
    check.equal(data_response['per_page'], 6)
    check.equal(response.status_code, 400)
