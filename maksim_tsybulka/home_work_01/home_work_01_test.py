"""Мой импорт"""
import requests  # pylint: disable=E0401

URL = "https://hoster.by/ajax/basket.php"

PAYLAUD = "mode=CLOUD_HOSTING&name=24CPU%2C+RAM%3A+64%D0%93%D0%B1%2C+SSD%3A+" \
          "1000%D0%93%D0%B1%2C+Linux&json_config=%7B%22os%22%3A%22Linux%22%" \
          "2C%22cpu%22%3A%2224%22%2C%22ram%22%3A%2264%22%2C%22hdd%22%3A%5B%" \
          "7B%22size%22%3A%221000%22%2C%22type%22%3A%22SSD%22%7D%5D%2C%22pa" \
          "th%22%3A%22%2Fservice%2Fcloud%2Fhosting%2F%22%7D&price=1.9&alte" \
          "r_section_name=%0A++++++++++++++++++++++++++++%D0%9E%D0%B1%D0%B" \
          "B%D0%B0%D1%87%D0%BD%D1%8B%D0%B9+%D1%81%D0%B5%D1%80%D0%B2%D0%B5%" \
          "D1%80++++++++++++++++++++++++&action=add2basket&list_name=cloud" \
          "-host-calculator&highTrial=1"
HEADERS = {
  'accept': '*/*',
  'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
  'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'cookie': 'hg-client-security=2nnmTb4E9oTCzgRQfvQtiHSH'
            'Po0; BITRIX_SM_SALE_UID=94565450; BITRIX_CO'
            'NVERSION_CONTEXT_s1=%7B%22ID%22%3A2%2C%22EX'
            'PIRE%22%3A1729630740%2C%22UNIQUE%22%3A%5B%'
            '22conversion_visit_day%22%5D%7D; BX_USER_ID'
            '=9f0f0d7801395f8001be7e7d97e35c44; no_show_m'
            'e=1; _gcl_gs=2.1.k1$i1729619226$u193947188; '
            '_gcl_au=1.1.839792687.1729619227; tmr_lvid=aa2'
            '482047427904930bbdafe6d146103; tmr_lvidTS=17296'
            '19227176; _ga=GA1.1.1169101049.1729619227; _fbp='
            'fb.1.1729619227471.686470846207408706; domain_si'
            'd=rx0sh3ZSkUWa-eO5idlpJ%3A1729619227483; '
            '=1729619228481326784; _ym_d=1729619228; _ymab_param='
            'XD-hsAjBGyIa2fYSyivBaH9UTev52-nH0l3SqBHIxPeGQDvUwXp_O'
            'gznJntY6C0ocCWgr4Wxxu4w117ugcdKtj23aaE; _ym_isad=2; '
            '=w; mindboxDeviceUUID=ea555af1-3b63-486e-af60-0cc11'
            '03ae891; directCrm-session=%7B%22deviceGuid%22%3A%'
            '22ea555af1-3b63-486e-af60-0cc1103ae891%22%7D; popme',
  'origin': 'https://hoster.by',
  'priority': 'u=0, i',
  'referer': 'https://hoster.by/service/cloud/hosting/',
  'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x6'
                '4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
  'x-requested-with': 'XMLHttpRequest'
}

response = requests.request("POST", URL, headers=HEADERS, data=PAYLAUD)

print(response.text)
print(response.json())
print(response.status_code)
