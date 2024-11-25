import requests
import pytest_check as check
import allure
import pytest


@allure.title("Allure test")
@allure.description("test allure report ")
@allure.tag("Allure", "Positive")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Nikita Stasilevich")
@allure.link("https://www.21vek.by/", name="Website")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
@pytest.mark.parametrize("url",["/tires/97505/"
                                 ])
def test_url(url):
    response = requests.get(f"https://www.21vek.by/{url}")

    with allure.step(f"Проверка сайта {url} на статус код"):
        check.equal(response.status_code, 200)
