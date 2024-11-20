import requests
import pytest_check as check
import allure
import pytest


@allure.title("Api test")
@allure.description("find test")
@allure.tag("API", "Positive")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Nikita Stasilevich")
@allure.link("https://catalog.onliner.by/", name="Website")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
@pytest.mark.parametrize("url",["/notebook",
                                "/display",
                                "/ssd",
                                "/fail",
                                "/mistake",
                                "/alert"
                                ])
def test_url(url):
    response = requests.get(f"https://catalog.onliner.by/{url}")

    with allure.step(f"Проверка сайта {url} на статус код"):
        check.equal(response.status_code, 200)
