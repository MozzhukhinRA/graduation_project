import time
import allure
import pytest
from methods_page_objects.methods import main_page, credit_page, menu_page, middel_page

"""Test #1"""


@pytest.mark.usefixtures('local')
class TestProductBannerAndFormCredit:

    @allure.epic("Кредитные продукты")
    @allure.feature("Заявка на получение кредитной карты")
    @allure.story("Заполнение формы для получения карты")
    @allure.tag('ui', 'credit', 'positive', 'regress')
    def test_assert_take_card(self):
        main_page.click_on_product()
        credit_page.check_header()
        credit_page.registration_credit_form()


"""Test #2"""


@pytest.mark.usefixtures('local')
class TestProductBar:

    @allure.epic("Welcome Page Банка")
    @allure.feature("Главный Баннер")
    @allure.story("Проверка активности главноего баннера")
    @allure.tag('ui', 'mainPage', 'positive', 'regress')
    def test_assert_bar(self):
        main_page.switch_product_on_main_page_right()
        main_page.switch_product_on_main_page_right()
        main_page.switch_product_on_main_page_left()


"""Test #3"""


@pytest.mark.usefixtures('local')
class TestMainMenu:

    @allure.epic("Welcome Page Банка")
    @allure.feature("Боковое Меню")
    @allure.story("Проверка открытия меню")
    @allure.tag('ui', 'menu', 'positive', 'regress')
    def test_assert_open_menu_and_button(self):
        main_page.open_menu()
        menu_page.size_element_in_menu()
        menu_page.assert_text_and_click()
        main_page.comeback()


"""Test #4"""


@pytest.mark.usefixtures('local')
class TestBestProduct:

    @allure.epic("Выбирайте из лучших продуктов")
    @allure.feature("Банковские карты")
    @allure.story("Проверка отображения")
    @allure.tag('ui', 'cards', 'positive', 'regress')
    def test_assert_product_card(self):
        middel_page.type_business()
        middel_page.card_list_bussines()
        middel_page.type_all()
        middel_page.cards_list_all()


"""Test #5"""

#@pytest.mark.usefixtures('local')
#class Test: