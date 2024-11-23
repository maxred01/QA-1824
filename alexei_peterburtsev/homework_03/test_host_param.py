import requests
import allure
import pytest
import pytest_check as check

@allure.feature('Api tests')
@allure.description('Test')
@allure.tag('Api', 'Positive')
@allure.severity(allure.severity_level.CRITICAL)
@allure.label('owner', 'Alexei Peterburtsev')
@allure.link('https://www.hoster.by/', name='Website')
@allure.issue('AUTH-123')
@allure.testcase('TMS-456')
@pytest.mark.parametrize('email', [
                                'alex-81@list.ru',
                                '111@@'
                                 ]
                         )

def test_url(email):

    url = "https://hoster.by/ajax/ajax.php"

    payload = (f'action=registration_lk&reg_client_type=2&isBasketPage=&2_resident=1&2_'
               f'country=RU&2_'
               f'email={email}&2_password=Aitin1234567%40&2_name=%D0%98%D0%B2%D0%B0%D0%BD'
               f'%D0%BE%D0%B'
               f'2%20%D0%98%'
               f'D0%B2%D0%B0%D0%BD&2_entity_phone=%2B375296244568&1_resident=1&1_country='
               f'RU&1_email=&1_'
               f'password=&1_'
               f'unp=&1_name=&1_entity_phone=&1_2faReg=1&gov_email=&gov_password=&gov_unp'
               f'=&gov_name=&'
               f'gov_entity_phone='
               f'&gov_2faReg=1&3_resident=1&3_country=RU&3_email=&3_password=&3_unp=&3_name='
               f'&3_entity_phone=&3_2faReg=1')
    headers = {
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'bx-ajax': 'true',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'hg-client-security=2p6wCu6bhHNtlnWRkLq3Yiyc0RF; BITRIX_SM_SALE_UID=96507511;'
                  ' BX_USER_ID=998365259c4ede785013edde61a986cb; cookie_technical=y; '
                  'cookie_targeting=y; _gcl_au=1.1.1910626659.1732099801; '
                  'tmr_lvid=7eb8fd9a9e86a61d13ec93f5d04a28e4; tmr_lvidTS=1732099801262; '
                  '_ga=GA1.1.1365919737.1732099801; _fbp=fb.1.1732099801415.103414015379665977;'
                  ' _tt_enable_cookie=1; _ttp=ZpJ4tntFc4sZeDEpHN0tGYSO0Vm.tt.1;'
                  ' _ym_uid=1732099803638822632; _ym_d=1732099803; _ymab_param=WVfuXFuX7UsdhW_'
                  'AgEppjX8UvUWlk0VA46PBvPHw2NHdKXxLbCH3octEX4zrqLdgvlw5k5KBlsUAVQxWLMbPkBc8wEo; '
                  'mindboxDeviceUUID=08cb1f4c-a42a-4930-bab4-b6e78e3ee43f; '
                  'directCrm-session=%7B%22deviceGuid%22%3A%2208cb1f4c-a42a-4930-bab4-b6e78e3ee'
                  '43f%22%7D; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C'
                  '1471519752600%3D1%7C%7C%7C1471519752605%3D1; domain_sid=7pCv1nNBOKigEpstsq7pi'
                  '%3A1732262900304; BITRIX_CONVERSION_CONTEXT_s1=%7B%22ID%22%3A2%2C%22EXPIRE%22'
                  '%3A1732395540%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D; _ym_isad='
                  '2; _ym_visorc=w; _gcl_gs=2.1.k1$i1732346936$u193947188; _gcl_aw=GCL.173234697'
                  '4.CjwKCAiA9IC6BhA3EiwAsbltOCaNVP1NwD8NcL4StS4MCZcjVB5yQ3hdtKrINOcp7I2sNdT4IW-8'
                  'KBoC45MQAvD_BwE; _ga_261820121=GS1.1.1732345198.3.1.1732347181.0.0.1763845134;'
                  ' tmr_detect=0%7C1732347184162; PHPSESSID=DgcdkBpdMWTr9IN7aSn5OqwOxdJMHDKH; '
                  '_ga_9JLLFGM9W7=GS1.1.1732345198.3.1.1732348066.47.0.0',
        'origin': 'https://hoster.by',
        'priority': 'u=0, i',
        'referer': 'https://hoster.by/',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    with allure.step(f'Test Email: {email}'):
        check.equal(response.status_code, 201)
