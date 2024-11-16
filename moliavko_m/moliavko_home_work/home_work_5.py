import pytest_check as check
import requests


def test_api_register_successful():
    url = "https://reqres.in/api/register"

    id_data = "1"
    name_data = "cerulean"
    year_data = "2000"
    color_data = "#98B2D1"
    pantone_value_data = "15-4020"
    headers = {}
    email_data = "test1111@gmail.com"
    password_data = "1234561111"

    data = {
        "id": id_data,
        "name": name_data,
        "year": year_data,
        "color": color_data,
        "pantone_value": pantone_value_data,
        "email": email_data,
        "password": password_data
    }

    response = requests.request('POST', url, data=data, headers=headers)
    data_response = response.json()
    print(data_response)

    check.equal(data_response["id"], id)
    check.equal(data_response["name"], name_data)
    check.equal(data_response['year'], year_data)
    check.equal(data_response['color'], color_data)
    check.equal(data_response['pantone_value'], pantone_value_data)
    check.equal(data_response['total pages'], 2)
    check.equal(data_response['total'], 12)
    check.equal(data_response['per_page'], 6)
    check.equal(response.status_code, 400)
