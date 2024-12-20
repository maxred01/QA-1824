import requests
import allure
import pytest
import pytest_check as check

@allure.feature("Api tests")
@allure.description("Test")
@allure.tag("Api", "Positive")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Alexei Peterburtsev")
@allure.link("https://www.onliner.by/", name="Website")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
@pytest.mark.parametrize("url", [
                                "2024/11/14/posledstviya-diabeta",
                                "2024/11/14/muzhchina-delal-remont-2",
                                "2024/11/14/belorusskaya-issledovatelnica-god-provela-v-izolyacii-radi-nauki",
                                "2024/11/14/belorusskaya-issledovatelnica-god-provela-v-izolyacii-radi-nauki111",
                                "KJDFKSDFGD",
                                "*&^*&#^*^$%)*&%T",
                                 ]
                         )
def test_url(url):
    respons = requests.get(f"https://people.onliner.by/{url}")

    with allure.step(f"Test site {url} status code"):
        check.equal(respons.status_code, 200)