import os

from maksim_tsybulka.example_diplom.page.base_page import WebPage
from maksim_tsybulka.example_diplom.page.elements import WebElement
from maksim_tsybulka.example_diplom.page.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://hoster.by'

        super().__init__(web_driver, url)

    btn_headers_domain = WebElement(xpath='//div[@id="menu-item"]//span[contains(text(),"Домены")]')
    btn_headers_hosting = WebElement(xpath='//div[@id="menu-item"]//span[contains(text(),"Хостинг")]')
    btn_headers_cloud = WebElement(xpath='//div[@id="menu-item"]//span[contains(text(),"Облако")]')
    btn_headers_mail = WebElement(xpath='//div[@id="menu-item"]//span[contains(text(),"Почта")]')
    btn_pip_up_сookie = WebElement(id="accept")
    block_main = WebElement(xpath='//div[@class="m-section main-intro"]')
    txt_main_h1 = WebElement(xpath='//h1[@class="intro-title m-font-hl1"]')
    input_main_wrapper = WebElement(xpath='//input[@class="m-input m-b1"]')
    btn_search_domain = WebElement(xpath='//button[@class="m-button red"]')
    text_results_search_domain = WebElement(xpath='//div[@class="group-valid group-domain"]//div[@class="name tCell middle"]')
    text_by_zone = WebElement(xpath='(//span[@class="domain-name m-font-l2"])[1]')
    group_valid_domain = WebElement(xpath='//div[@class="tabCont"]')
    btn_domain_link = WebElement(xpath='//*[contains(text(), "Подобрать домен")]')
    btn_count_box = ManyWebElements(xpath='//div[contains(@class, "category-item m-font-l2")]')
    count_box = ManyWebElements(xpath='//a[@class="solutions-item"]')
