import requests
import pytest
import allure
import pytest_check as check


@allure.feature('Мой первый тест')
def test_url():
    response = requests.get(f'https://hoster.by/')

    with allure.step(f'Проверка статус кода страницы'):
        check.equal(response.status_code, 200, f'статаус код не равен 200. Статус код равен {response.status_code}')
