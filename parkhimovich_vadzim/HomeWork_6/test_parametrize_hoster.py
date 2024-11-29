import pytest
import pytest_check as check

@allure.feature('Api tests')
@allure.description('Test')
@allure.tag('Api', 'Positive')
@allure.feature("Api tests")
@allure.description("Test")
@allure.tag("Api", "Positive")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label('owner', 'Vadzim Parkhimovich')
@allure.link('https://www.hoster.by/', name='Website')
@allure.issue('AUTH-123')
@allure.testcase('TMS-456')
@pytest.mark.parametrize('url',[

])
