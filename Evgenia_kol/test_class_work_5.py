import requests
import pytest
import allure
import pytest_check as check


@allure.title('Апи тесты')
@allure.feature('Проверка апи главной страницы')
@allure.description("Тут мы проверяем, что главная страницы доступна и отдает статус код 200")
@allure.tag("API", "Positive")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Maksim Tsybulka")
@allure.link("https://google.com", name="Website")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
@pytest.mark.parametrize('url', ["fftyfyt1",
                                 "2$^",
                                 "3       ",
                                 "456",
                                 "5",
                                 ])
def test_url(url):
  respons = requests.get(f'https://onliner.by/{url}')

  with allure.step(f'Проверка сайта {url} на статус код'):
    check.equal(respons.status_code, 200)









#
#
# @allure.title('Апи тесты второй вариант')
# @allure.feature('Проверка апи главной страницы второй вариант')
# @allure.description("Тут мы проверяем, что главная страницы доступна и отдает статус код 200 второй вариант")
# @allure.tag("API", "Positive")
# @allure.severity(allure.severity_level.CRITICAL)
# @allure.label("owner", "Maksim Tsybulka второй вариант")
# @allure.link("https://google.com", name="Website")
# @allure.issue("AUTH-123")
# @allure.testcase("TMS-456")
# @pytest.mark.parametrize('a', 'b', 'expected', [
#   (1,2,3),
#   (2,3,4),
#   (2,2,6)
#
# ])
#
# def test_addition(a,b, expected):
#     assert a + b == expected