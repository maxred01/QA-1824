import requests
import pytest
import allure
import pytest_check as check


@allure.title('Апи тесты')
@allure.feature('Проверка апи главно_й страницы')
@allure.description("Тут мы проверяем, что главная страницы доступна и отдает статус код 200")
@allure.tag("API", "Positive")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Mishael")
@allure.link("https://www.onliner.by/", name="Website")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
@pytest.mark.parametrize('url', ["https://www.onliner.by/",
                                 "https://forum.onliner.by/",
                                 "https://baraholka.onliner.by/",
                                 "https://s.onliner.by/tasks",
                                 "https://catalog.onliner.by/",
                                 ])
def test_01(url):
    respons = requests.get(f'{url}')

    with allure.step(f'Проверка сайта {url} на статус код'):
        check.equal(respons.status_code, 200)
