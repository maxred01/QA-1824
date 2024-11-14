''' test api allure '''


import requests  # pylint: disable=E0401
import pytest_check as check  # pylint: disable=E0401
import pytest  # pylint: disable=E0401
import allure  # pylint: disable=E0401


@allure.feature('Проверка главной страницы')
@allure.description("Тут мы проверяем, что главная страница доступна и запускается ")
@allure.tag("API", "Positive")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("QA", "Artemij Shulga")
@allure.link("https://gta5rp.com/api/V2/news", name="Website")

def test_api_users():
    """ testing """
    url = "https://gta5rp.com/api/V2/news"

    payload = {}
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,'
                  'image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'cookie': '_ym_uid=1731436466773950270; _ym_d=1731436466; _ym_isad=2; _gcl_au=1.1.1611923229.1731436466;'
                  ' _ym_visorc=b; _ga=GA1.1.1105133477.1731436466; _ga_EWSTLBC5EN=GS1.1.1731436466.1.1.'
                  '1731436848.37.0.0;'
                  ' _ga_2K3801VYMN=GS1.1.1731436466.1.1.1731436848.37.0.0',
        'priority': 'u=0, i',
        'referer': 'https://www.google.com/',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    with allure.step('Проверка статус кода'):
        check.equal(response.status_code, 200, f'статус код не равен 200. Статус код равен {response.status_code}')




