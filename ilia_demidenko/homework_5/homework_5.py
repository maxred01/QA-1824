import requests
import pytest_check as check


def test_api_post_users():

    url = "https://reqres.in/api/register"

    data = {
        "id": 0,
        "name": "null",
        "year": 0,
        "color": "null",
        "pantone_value": "null"
        }

    r = requests.post(url, data)

    print(r.text)
    print(type(r))
    print(dir(r))
