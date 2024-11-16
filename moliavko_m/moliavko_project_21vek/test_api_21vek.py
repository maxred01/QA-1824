import pytest
import requests
import pytest_check as check
import allure


@allure.title('Апи тест')
@allure.feature('проверка апи кнопки "все акции" ')
@allure.description("проверяем, что кнопка работает, отдает статус код 200,"
                    " sentry_key, sentry_version, sentry_client и cookies не пусты")
@allure.tag("API", "Positive")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("owner", "Mishael")
@allure.link("https://www.21vek.by/special_offers/promo.html", name="Website")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
@pytest.mark.parametrize('url', ["https://www.21vek.by/special_offers/promo.html",
                                 "https://www.21vek.by/special_offers/promo.html",
                                 "https://www.21vek.by/special_offers/promo.html",
                                 "https://www.21vek.by/special_offers/promo.html",
                                 "https://www.21vek.by/special_offers/promo.html",
                                 ])
def test_api_button(url):
    response = requests.get(f'{url}')

    with allure.step(f'проверка кнопки {url} на статус код'):
        check.equal(response.status_code, 200)

    with allure.step(f'sentry_key {url} не пуст'):
        check.is_not_none("sentry_key")

    with allure.step(f'sentry_version {url} не пуст'):
        check.is_not_none("sentry_version")

    with allure.step(f'sentry_client {url} не пуст'):
        check.is_not_none("sentry_client")

    with allure.step(f'cookies {url} не пуст'):
        check.is_not_none("cookies")