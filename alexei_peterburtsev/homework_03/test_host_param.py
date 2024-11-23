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
                                '123@tut.by',
                                '<tag>',
                                 ]
                         )
def test_url(email):

    url = "https://hoster.by/ajax/ajax.php"

    payload = (f'action=registration_lk&reg_client_type=2&isBasketPage='
               f'&2_resident=1&2_country=RU&2_email={email}&2_password='
               f'QWERTYqwerty123456!&2_name=%D0%91%D0%B0%D1%80%D0%B0%D0%BA%20%D0'
               f'%9E%D0%B1%D0%B0%D0%BC%D0%B0&2_entity_phone=%2B375291324345&1_res'
               f'ident=1&1_country=RU&1_email=&1_password=&1_unp=&1_name=&1_entity_p'
               f'hone=&1_2faReg=1&gov_email=&gov_password=&gov_unp=&gov_name=&gov_entit'
               f'y_phone=&gov_2faReg=1&3_resident=1&3_country=RU&3_email=&3_password=&3'
               f'_unp=&3_name=&3_entity_phone=&3_2faReg=1')
    headers = {
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'bx-ajax': 'true',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'hg-client-security=2p6wCu6bhHNtlnWRkLq3Yiyc0RF; BITRIX_SM_SALE_UID=9'
                  '6507511; BX_USER_ID=998365259c4ede785013edde61a986cb; cookie_techni'
                  'cal=y; cookie_targeting=y; _gcl_au=1.1.1910626659.1732099801; tmr_lvi'
                  'd=7eb8fd9a9e86a61d13ec93f5d04a28e4; tmr_lvidTS=1732099801262; _ga=GA'
                  '1.1.1365919737.1732099801; _fbp=fb.1.1732099801415.103414015379665977;'
                  ' _tt_enable_cookie=1; _ttp=ZpJ4tntFc4sZeDEpHN0tGYSO0Vm.tt.1; _ym_uid=17'
                  '32099803638822632; _ym_d=1732099803; _ymab_param=WVfuXFuX7UsdhW_AgEppjX8U'
                  'vUWlk0VA46PBvPHw2NHdKXxLbCH3octEX4zrqLdgvlw5k5KBlsUAVQxWLMbPkBc8wEo; min'
                  'dboxDeviceUUID=08cb1f4c-a42a-4930-bab4-b6e78e3ee43f; directCrm-session=%'
                  '7B%22deviceGuid%22%3A%2208cb1f4c-a42a-4930-bab4-b6e78e3ee43f%22%7D; popme'
                  'chanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C147151975260'
                  '0%3D1%7C%7C%7C1471519752605%3D1; BITRIX_CONVERSION_CONTEXT_s1=%7B%22ID%2'
                  '2%3A2%2C%22EXPIRE%22%3A1732395540%2C%22UNIQUE%22%3A%5B%22conversion_visit'
                  '_day%22%5D%7D; _ym_isad=2; domain_sid=7pCv1nNBOKigEpstsq7pi%3A17323644603'
                  '05; _ym_visorc=w; _gcl_gs=2.1.k1$i1732366955$u193947188; _ga_261820121=GS'
                  '1.1.1732364460.4.1.1732366957.0.0.1832658421; _gcl_aw=GCL.1732366958.CjwK'
                  'CAiAl4a6BhBqEiwAqvrqup_NkxO2Q0aT3g6vSK7zf5xXWuYItm0InEBZh1u6w-3S6a59SN7uC'
                  'BoCb7EQAvD_BwE; tmr_detect=0%7C1732366960048; PHPSESSID=53IZ8BzKQkeyx4XdnL'
                  '4WgY8Lpk1LN65v; _ga_9JLLFGM9W7=GS1.1.1732364462.4.1.1732367032.60.0.0',
        'origin': 'https://hoster.by',
        'priority': 'u=0, i',
        'referer': 'https://hoster.by/?utm_source=google&utm_medium=cpc&utm_campaign=search|'
                   '{Brend}|google-search|keyword&utm_content=adaptiv&utm_term=hoster%20by-ma'
                   'in-page&gad_source=1&gclid=CjwKCAiAl4a6BhBqEiwAqvrqup_NkxO2Q0aT3g6vSK7zf5x'
                   'XWuYItm0InEBZh1u6w-3S6a59SN7uCBoCb7EQAvD_BwE',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                      ' (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    with allure.step(f'Test Email: {email}'):
        check.equal(response.status_code, 200)
