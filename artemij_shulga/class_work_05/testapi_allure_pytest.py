import requests
import pytest
import allure
import pytest_check as check

@allure.title('API tests')
@allure.feature('Test search')
@allure.description(" check: onliner status ")
@allure.tag("API", "Positive")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("QA", "Artemij Shulga")
@allure.link("https://catalog.onliner.by/", name="Website")
@allure.issue('AUTH-123')
@allure.testcase('TMS-456')
@pytest.mark.parametrize('url', ["heater/royal_thermo/rtc20",
                                 "headphones/xiaomi/xbuds5gltgl",
                                 "ssd/patriot/p320p1tbm28",
                                 "ssd/patriot/p320p1tbm284568",
                                 "%:?№::№№?*(();№",
                                 ])

def test_url(url):
  response = requests.get(f'https://catalog.onliner.by/{url}')

  with allure.step(f'Проверка сайта {url} на статус код'):
    check.equal(response.status_code, 200)

