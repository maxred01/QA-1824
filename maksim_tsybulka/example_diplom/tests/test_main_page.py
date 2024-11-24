import time

import allure
import pytest_check as check
from Maksim_Tsybulka.class_work_9_f.locators.locators_main_page import MainPage


@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки хедара')
def test_headers(web_browser):
    """Этот тест проверяет хедер главной страницы"""

    page = MainPage(web_browser)

    page.btn_pip_up_сookie.click()

    elements_headers = [
        (page.btn_headers_domain, 'Домены'),
        (page.btn_headers_hosting, 'Хостинг'),
        (page.btn_headers_cloud, 'Облако'),
        (page.btn_headers_mail, 'Почта')
    ]

    for elements, elements_text in elements_headers:
        with allure.step(f'Проверка "{elements_text}" на отображение'):
            check.is_true(elements.is_visible())

        with allure.step(f'Проверка "{elements_text}" на кликабельность'):
            check.is_true(elements.is_clickable())

        with allure.step(f'Сверка текста"{elements_text}"'):
            check.equal(elements.get_text(), elements_text)


@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки наличия блоков')
def test_headers(web_browser):
    """Этот тест проверяет блоки главной страницы на его присутсвие"""

    page = MainPage(web_browser)

    page.btn_pip_up_сookie.click()

    elements_headers = [
        (page.block_main, 'Первый блок или главный')
    ]

    for elements, elements_text in elements_headers:
        with allure.step(f'Проверка "{elements_text}" на отображение'):
            check.is_true(elements.is_visible())


@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки текста')
def test_headers(web_browser):
    """Этот тест проверяет текст на наличие и его корректность"""

    page = MainPage(web_browser)

    page.btn_pip_up_сookie.click()

    elements_headers = [
        (page.txt_main_h1, 'Все для онлайн-проектов и их защиты')
    ]

    for elements, elements_text in elements_headers:
        with allure.step(f'Проверка "{elements_text}" на отображение'):
            check.is_true(elements.is_visible())

        with allure.step(f'Сверка текста "{elements_text}"'):
            check.equal(elements.get_text(), elements_text)


@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки работоспособности инпута')
def test_input_main(web_browser):
    """Этот тест проверяет работоспособность инпута"""

    page = MainPage(web_browser)

    page.btn_pip_up_сookie.click()

    with allure.step('Проверка на кликабельность'):
        check.is_true(page.input_main_wrapper.is_visible())

    with allure.step('Проверка на отображение'):
        check.is_true(page.input_main_wrapper.is_clickable())

    with allure.step('Проверка плейсхолдера'):
        check.equal(page.input_main_wrapper.get_attribute('placeholder'), 'Введите домены')

    with allure.step('Проверка на ввод текст и роверка результата'):
        text_by_zone = page.text_by_zone.get_text()
        text_tatimati = 'tatimati'

        page.input_main_wrapper.send_keys(text_tatimati)
        page.btn_search_domain.click(1)

        time.sleep(10)
        print(page.group_valid_domain.get_text())
        check.not_equal(page.group_valid_domain.get_text().find(f'{text_tatimati+text_by_zone}'), -1)


@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки адреса ссылок')
def test_link_main(web_browser):
    """Этот тест проверяет адрес ссылок в кнопках """

    page = MainPage(web_browser)

    page.btn_pip_up_сookie.click()

    with allure.step('Проверка на кликабельность'):
        check.is_true(page.btn_domain_link.is_clickable())
        check.is_true(page.btn_domain_link.is_visible())
        check.equal(page.btn_domain_link.get_attribute('href'), 'https://hoster.by/service/domains/')


@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки колличества плиток в блоке "Подберите свое решение"')
def test_count_box_main(web_browser):
    """Этот тест проверяет количество плиток в блоке "Подберите свое решение" """

    page = MainPage(web_browser)

    page.btn_pip_up_сookie.click()

    with allure.step('Проверка количетва плиток'):
        count = page.btn_count_box
        namber = [(4), (9), (10), (3), (1), (4), (10), (3), (5), (5), (53)]

        for count_elemnts in count:
            count_elemnts.click()
            check.equal(page.count_box.count(), namber)
