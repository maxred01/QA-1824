import ssl
import socket
import allure
import pytest_check as check
import requests


@allure.title("Autotest")
@allure.feature("test ssl certificate and status code")
@allure.description("check:ssl certificate and status code 200")
@allure.tag("Autotest", "Positive")
@allure.label("QA", "Artemij Shulga")
@allure.link("https://www.nasa.gov/", name="Website")


def test_ssl_certificate_exists():
    domain = 'www.nasa.gov'
    context = ssl.create_default_context()
    with socket.create_connection((domain, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=domain) as ssock:
            certificate = ssock.getpeercert()
            assert certificate is not None, "SSL certificate does not exist."


def test_status_code_nasa():

    url = 'https://www.nasa.gov/'

    headers = {}

    response = requests.request('GET', url, headers=headers)

    with allure.step("nasa status check code"):
        check.equal(response.status_code, 200,
                    f'status code is not equal to 200.Status code is {response.status_code}')