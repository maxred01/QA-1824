'''testing hoster'''

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
@pytest.mark.parametrize('url', [
                                'service/solutions/ssl/',
                                'service/solutions/ssl/not_exist',
                                 ]
                         )
def test_url(url):
    '''test func'''
    respons = requests.get(f'https://www.hoster.by/{url}')

    with allure.step(f'Test site {url} ON_ status code'):
        check.equal(respons.status_code, 200)
