import ssl
import socket
import requests
import pytest_check as check
import allure

@allure.feature('Site test')
@allure.description('Check status code, certificate SSL')
@allure.label('owner', 'Alexei Peterburtsev')
@allure.link('https://www.hoverstat.es/', name='Website')
@allure.issue('AUTH-123')
@allure.testcase('TMS-456')

def test_status_code():
    respons = requests.get('https://www.hoverstat.es/')

    with allure.step('Check status code'):
        check.equal(respons.status_code, 200,'status code is not 200')

def test_ssl_certificate_exists():
    domain = 'https://www.hoverstat.es/'
    context = ssl.create_default_context()

    with socket.create_connection((domain, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=domain) as ssock:
            certificate = ssock.getpeercert()
            assert certificate is not None, "SSL certificate does not exist."
