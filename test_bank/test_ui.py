import time

import allure
import pytest
from selene import browser

from methods_page_objects.methods import main_page, credit_page
from test_bank.conftest import local_test

"""Test #1"""


@pytest.mark.usefixtures('local_test')
class TestProductBannerAndFormCredit:

    @allure.epic("Кредитные продукты")
    @allure.feature("Заявка на получение кредитной карты")
    @allure.story("Заполнение формы для получения карты")
    @allure.tag('ui', 'credit', 'positive', 'regress')
    def test_take_card(self):
        main_page.click_on_product()
        credit_page.check_header()
        credit_page.registration_credit_form()


"""Test #2"""


@pytest.mark.usefixtures('local_test')
class TestProductBar:

    @allure.epic("Welcome Page Банка")
    @allure.feature("Главный Баннер")
    @allure.story("Проверка активности главноего баннера")
    @allure.tag('ui', 'mainPage', 'positive', 'regress')
    def test_bar(self):
        main_page.switch_product_on_main_page_right()
        main_page.switch_product_on_main_page_right()
        main_page.switch_product_on_main_page_left()


"""Test #2"""


@pytest.mark.usefixtures('local_test')
class TestMainMenu:

    @allure.epic("Welcome Page Банка")
    @allure.feature("Боковое Меню")
    @allure.story("Проверка открытия меню")
    @allure.tag('ui', 'menu', 'positive', 'regress')
    def test_bar(self):
        main_page.open_menu()
        browser.all('._2xtPnv').second.click()
        browser.all('._2xtPnv').first.click()
        time.sleep(5)
