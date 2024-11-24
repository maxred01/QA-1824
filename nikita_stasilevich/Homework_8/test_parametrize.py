import requests
import pytest
import allure
import pytest_check as check


@allure.title('Проверка параметрайз')
@allure.feature('Проверка апи страницы "Помощь"')
@allure.description("Тут мы проверяем замену номера телефона на странице 'Помощь'")
@allure.tag("API", "Positive")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Nikita Stasilevich")
@allure.link("https://hoster.by/ajax/ajax.php", name="Website")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
@pytest.mark.parametrize('phone', [
                                '375296961077'])



def test_parametrize(phone):

    url = "https://hoster.by/ajax/ajax.php"

    payload = ('action=sendAjax&phone=%2B375%20(29)%20697-10-77&form_name=%D0%9E%D1%81%D1%82%D0%B0%D0%BB%D0%B8%D1%81%D1'
               '%8C%20%D0%B2%D0%BE%D0%BF%D1%80%D0%BE%D1%81%D1%8B%3F&email=stasilevichnik1996%40gmail.com&name=%D0%9D%D0'
               '%B8%D0%BA%D0%B8%D1%82%D0%B0&message=test&email'
               'Temlate=HOSTER_FEEDBACK_FORM_CONTACTS&session_id=828517621.1732273783')
    headers = {
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'bx-ajax': 'true',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': '_ym_uid=1713717215907008145; hg-client-security=2o9xQ0sq1BBqRU9vFmuT2Bl5DPg;'
                  ' BITRIX_SM_SALE_UID=95076993; BX_USER_ID=8802636797e54084f358104b3935a7b4; no_show_me=1; '
                  'cookie_technical=y; cookie_targeting=y;'
                  ' _gcl_au=1.1.1490582911.1732273783; _ga=GA1.1.828517621.1732273783; '
                  'tmr_lvid=7beb4ff144b4073fea92befa4dc5e2f9; tmr_lvidTS=1732273783201;'
                  ' _tt_enable_cookie=1; _ttp=IW79l-7ERVU8UNpHZrTQVWD6mGn.tt.1; '
                  'mindboxDeviceUUID=c4e4a6cd-7755-4dc2-81be-6fa1011ad774; '
                  'directCrm-session=%7B%22deviceGuid%22%3A%22c4e4a6cd-7755-4dc2-81be-6fa1011ad774%22%7D;'
                  ' _fbp=fb.1.1732273783790.830736852504240606; '
                  'popmechanic_sbjs_migrations='
                  'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1;'
                  ' _ym_d=1732273787;'
                  ' _ymab_param=OQfqJeqeAwlzlR1jAidJN8'
                  '-NL7znBtoknYgpvwyx9o7mtcAf8Awk0FDpyHRDw1cORV3GYdWbh9Ym6U8LIh_vqRZBVrQ; '
                  'PHPSESSID=17U3vyT2AodV3Topy5PPPCcdXt3e9WZd; '
                  'BITRIX_CONVERSION_CONTEXT_s1=%7B%22ID%22%3A3%2C%22EXPIRE%22%3A1732481940%2C%22UNIQUE%22%3A%5B%22'
                  'conversion_visit_day%22%5D%7D; _ga_261820121=GS1.1.1732464893.4.0.1732464893.0.0.1954656879;'
                  ' domain_sid=htsMTmdfoF_Bup6GY3A7E%3A1732464893278; tmr_detect=0%7C1732464894319; _ym_isad=2;'
                  ' _ym_visorc=w; _ga_9JLLFGM9W7=GS1.1.1732464949.5.0.1732465027.60.0.0; '
                  'PHPSESSID=2Ce2W2akydjV7AY1Jva0VtWr84N4E5hI',
        'origin': 'https://hoster.by',
        'priority': 'u=1, i',
        'referer': 'https://hoster.by/',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/131.0.0.0 Safari/537.36'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


    with allure.step(f'Test Phone: {phone}'):
        check.equal(response.status_code, 200)