import requests
import pytest
import allure
import pytest_check as check


@allure.title("API tests")
@allure.feature("Test search")
@allure.description("check: hoster status and name")
@allure.tag("API", "Positive")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("QA", "Artemij Shulga")
@allure.link("https://hoster.by/", name="Website")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
@pytest.mark.parametrize("status_code, name", [
    (200, "testekor"),
    (230, "hello world"),
    (200, ";%%№"),
    (200, "test"),
    (200, "кураqwery"),

])
def test_parametrize(status_code, name):

    url = "https://hoster.by/ajax/ajax.php"

    payload_one = f'action=sendAjax&phone=test&form_name=' \
                  f'%D0%9E%D1%81%D1%82%D0%B0%D0%BB%D0%B8%D1%81%D1%8C%20%D0%B2%D0%BE%D0%BF%D1%80%D0%BE%D1%81%D1%8B%3F' \
                  f'&email=tester%40tester.com&name={name}' \
                  f'&message=test&emailTemlate=HOSTER_FEEDBACK_FORM_CONTACTS&session_id=19089221.1729842365'

    headers = {
       'accept': '*/*',
       'accept-language': 'en-US,en;q=0.9,ru;q=0.8,uk;q=0.7',
       'bx-ajax': 'true',
       'content-type': 'application/x-www-form-urlencoded',
       'cookie': 'hg-client-security=2ce7oDMxJtdcFHek4RLyRZv5Esi;'
                 ' _ym_uid=1721596623301869217; _ym_d=1721596623;'
                 ' _ymab_param=OfOSkmqJwamkY4b51WndKxrzBm9iRH7GzXi5puA1dDTc0alJW8G0e6IeOmE31345Qqotfk9gLzFuK'
                 '-nI0uO5NoOmOWk; BITRIX_SM_SALE_UID=94736060; BX_USER_ID=5edaed9194ea32ebcd7065c62a384c57;'
                 ' no_show_me=1; _gcl_au=1.1.2124724873.1729842365; _ga=GA1.1.19089221.1729842365;'
                 ' tmr_lvid=555cdaf11f9b06edcc7862c3ba4f5282; tmr_lvidTS=1729842365147;'
                 ' _fbp=fb.1.1729842365377.453126830333787344; mindboxDeviceUUID=381dd29f-6548-4198-b326-90dc25bbb603;'
                 ' directCrm-session=%7B%22deviceGuid%22%3A%22381dd29f-6548-4198-b326-90dc25bbb603%22%7D;'
                 ' popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%'
                 '3D1%7C%7C%7C1471519752605%3D1; cookie_technical=y; cookie_targeting=y; _tt_enable_cookie=1;'
                 ' _ttp=wEE3QQ0bk9nZFyWP3dFT09s9sc2.tt.1; BITRIX_CONVERSION_CONTEXT_s1=%7B%22ID%22%3A3%2C%22EXPIRE'
                 '%22%3A1732049940%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D;'
                 ' domain_sid=vZ4luSRdfngM6BNKHCHfi%3A1732003784182; _ym_isad=2; _ym_visorc=w;'
                 ' b24_sitebutton_hello=y; PHPSESSID=ywJx68if8ro8mMo7hiOixzx37ygDHorJ;'
                 ' _ga_261820121=GS1.1.1732003780.7.1.1732004919.0.0.27449920;'
                 ' tmr_detect=0%7C1732004921103; _ga_9JLLFGM9W7=GS1.1.1732003788.7.1.1732004986.60.0.0;'
                 ' PHPSESSID=qDW0ifa0dXy4TPtusiFFPCKyKan4PeTh; hg-client-security=2p3orATBxeCpCed9iVLJletIEMP',
       'origin': 'https://hoster.by',
       'priority': 'u=1, i',
       'referer': 'https://hoster.by/',
       'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
       'sec-ch-ua-mobile': '?0',
       'sec-ch-ua-platform': '"Windows"',
       'sec-fetch-dest': 'empty',
       'sec-fetch-mode': 'cors',
       'sec-fetch-site': 'same-origin',
       'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                     ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    }

    response_one = requests.request("POST", url, headers=headers, data=payload_one)

    with allure.step(f"Проверка поля name с символами {name}"):
        check.equal(response_one.status_code, 200)

    with allure.step(f"Проверка на статус код {status_code}"):
        assert status_code == 200





