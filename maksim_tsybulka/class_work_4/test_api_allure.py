import requests
import pytest_check as check
import allure


@allure.title('Апи тесты')
@allure.feature('Проверка апи главной страницы')
@allure.description("Тут мы проверяем, что главная страницы доступна и отдает статус код 200")
@allure.tag("API", "Positive")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Maksim Tsybulka")
@allure.link("https://google.com", name="Website")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
def test_api_main_page():
    url = "https://maxkorzh.live/"

    headers = {}

    response = requests.request('GET', url, headers=headers)

    with allure.step('Проверка статус кода 1'):
        check.equal(response.status_code, 202, f'статус код не равен 200. Статус код равен {response.status_code}')

    with allure.step('Проверка статус кода 2'):
        check.equal(response.status_code, 200, f'статус код не равен 200. Статус код равен {response.status_code}')

    with allure.step('Проверка статус кода 3'):
        assert response.status_code == 300
        check.equal(response.status_code, 200, f'статус код не равен 200. Статус код равен {response.status_code}')

    with allure.step('Проверка статус кода 4'):
        check.equal(response.status_code, 200, f'статус код не равен 200. Статус код равен {response.status_code}')

    with allure.step('Проверка статус кода 4'):
        check.equal(response.status_code, 200, f'статус код не равен 200. Статус код равен {response.status_code}')

    with allure.step('Проверка статус кода 5'):
        check.equal(response.status_code, 200, f'статус код не равен 200. Статус код равен {response.status_code}')

    with allure.step('Проверка статус кода 6'):
        check.equal(response.status_code, 200, f'статус код не равен 200. Статус код равен {response.status_code}')


@allure.title('Апи тесты')
@allure.feature('Проверка апи страницы музыки')
@allure.description("Тут мы проверяем, что главная страницы доступна и отдает статус код 200")
@allure.tag("API", "Positive")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Maksim Tsybulka")
@allure.link("https://google.com", name="Website")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
def test_api_muzyika_page():
    url = "https://maxkorzh.live/muzyika/"

    headers = {}

    response = requests.request('GET', url, headers=headers)

    with allure.step('Проверка статус кода'):
        check.equal(response.status_code, 200, f'статус код не равен 200. Статус код равен {response.status_code}')
