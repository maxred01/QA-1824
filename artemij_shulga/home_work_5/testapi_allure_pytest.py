import ssl
import socket
import allure
import pytest
import pytest_check as check

@allure.title("API tests")
@allure.feature("Test search")
@allure.description("check: onliner status")
@allure.tag("API", "Positive")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("QA", "Artemij Shulga")
@allure.link("https://www.nasa.gov/", name="Website")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")

def test_ssl_certificate_exists():
    domain = 'https://www.nasa.gov/'  # Замените на нужный домен
    context = ssl.create_default_context()
    with socket.create_connection(('https://www.nasa.gov/', 443)) as sock:
        with context.wrap_socket(sock, server_hostname=domain) as ssock:
            certificate = ssock.getpeercert()
            assert certificate is not None, "SSL certificate does not exist."

