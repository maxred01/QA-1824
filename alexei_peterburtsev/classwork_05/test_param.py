import requests
import allure
import pytest
import pytest_check as check

@allure.feature('Api tests')
@allure.description('Test')
@allure.tag('Api', 'Positive')
@allure.severity(allure.severity_level.CRITICAL)
@allure.label('owner', 'Alexei Peterburtsev')
@allure.link('https://www.onliner.by/', name='Website')
@allure.issue('AUTH-123')
@allure.testcase('TMS-456')
@pytest.mark.parametrize('url', [
                                '2024/11/14/posledstviya-diabeta',
                                '2024/11/14/muzhchina-delal-remont-2',
                                '2024/11/14/belorusskaya-issledovatelnica-god-provela-v-izolyacii-radi-nauki',
                                '2024/11/14/belorusskaya-issledovatelnica-god-provela-v-izolyacii-radi-nauki111',
                                'KJDFKSDFGD',
                                '*&^*&#^*^$%)*&%T',
                                 ]
                         )
def test_url(url):
  respons = requests.get(f'https://people.onliner.by/{url}')

  with allure.step(f'Test site {url} on status code'):
    check.equal(respons.status_code, 200)









# url = "https://www.onliner.by/sdapi/catalog.api/search/schemas?query=sdajhkfdjghsxcvnvbn"
#
#     payload = {}
#     headers = {
#       'Accept': 'application/json, text/javascript, */*; q=0.01',
#       'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
#       'Connection': 'keep-alive',
#       'Cookie': 'ouid=snyBDmc2MLsr/uT0A/zbAg==; occ=rfam%3A241114; stid=280ead3acf1d3ec1c974e4b7194e28ee0541f86acab8b0cbab86f864c96fd397; _ga=GA1.1.1154319807.1731604672; _ga_KPSB9MHYED=GS1.1.1731604672.1.0.1731604672.60.0.0; _ym_uid=1731604673336099289; _ym_d=1731604673; _ym_isad=2; _ga_NG54S9EFTD=GS1.1.1731604672.1.0.1731604677.55.0.0',
#       'Referer': 'https://www.onliner.by/sdapi/catalog/search/iframe?referrer=https://www.onliner.by/',
#       'Sec-Fetch-Dest': 'empty',
#       'Sec-Fetch-Mode': 'cors',
#       'Sec-Fetch-Site': 'same-origin',
#       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
#       'X-Requested-With': 'XMLHttpRequest',
#       'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
#       'sec-ch-ua-mobile': '?0',
#       'sec-ch-ua-platform': '"Windows"'
#     }
#
#     response = requests.request("GET", url, headers=headers, data=payload)
#
#     print(response.text)
