import requests
import pytest
import allure
import pytest_check as check


@allure.title('Апи тесты')
@allure.feature('Проверка апи главной страницы')
@allure.description("Тут мы проверяем, что главная страницы доступна и отдает статус код 200")
@allure.tag("API", "Positive")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Vadzim Parkhimovich")
@allure.link("https://onliner.by", name="Website")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
@pytest.mark.parametrize('url', ["впармпрмпаро",
                                 "jhuihuiohoi",
                                 "56678",
                                 "Каталог",
                                 "@@#@$%$%*",
                                 ])
def test_url(url):
  respons = requests.get(f'https://onliner.by/{url}')
  with allure.step(f'Проверка сайта {url} на статус код'):
    check.equal(respons.status_code, 200)

