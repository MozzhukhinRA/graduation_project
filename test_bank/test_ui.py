import time

import allure
import pytest
from methods_page_objects.methods import main_page, credit_page, menu_page, middel_page, cart_page, acquiring_page, \
    footer_page

"""Test #1"""


@pytest.mark.usefixtures('local')
class TestProductBannerAndFormCredit:

    @allure.epic("Кредитные продукты")
    @allure.feature("Заявка на получение кредитной карты")
    @allure.story("Заполнение формы для получения карты")
    @allure.tag('ui', 'credit_page', 'positive', 'regress')
    @allure.severity(allure.severity_level.BLOCKER)
    def test_assert_take_card(self):
        with allure.step('Выбираем продукт на баннере'):
            main_page.click_on_product()
        with allure.step('Проверяем текст заголовка'):
            credit_page.check_header()
        with allure.step('Заполняем форму регитсрации'):
            credit_page.registration_credit_form()


"""Test #2"""


@pytest.mark.usefixtures('local')
class TestProductBar:

    @allure.epic("Welcome Page Банка")
    @allure.feature("Главный Баннер")
    @allure.story("Проверка активности главноего баннера")
    @allure.tag('ui', 'mainPage', 'positive', 'regress')
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_assert_bar(self):
        with allure.step('Производим нажатие на правую стрелку'):
            main_page.switch_product_on_main_page_right()
        with allure.step('Производим нажатие на правую стрелку'):
            main_page.switch_product_on_main_page_right()
        with allure.step('Производим нажатие на лквую стрелку'):
            main_page.switch_product_on_main_page_left()


"""Test #3"""


@pytest.mark.usefixtures('local')
class TestMainMenu:

    @allure.epic("Welcome Page Банка")
    @allure.feature("Боковое Меню")
    @allure.story("Проверка открытия меню")
    @allure.tag('ui', 'menu', 'positive', 'regress')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_assert_open_menu_and_button(self):
        with allure.step('Открываем меню'):
            main_page.open_menu()
        with allure.step('Проверяем доступные услуги'):
            menu_page.size_element_in_menu()
        with allure.step('Проверяем текст - "Банкоматы и офисы" и нажимаем'):
            menu_page.assert_text_and_click()
        with allure.step('Возвращаемся на главную через логотип'):
            main_page.comeback()


"""Test #4"""


@pytest.mark.usefixtures('local')
class TestBestProduct:

    @allure.epic("Выбирайте из лучших продуктов")
    @allure.feature("Банковские карты")
    @allure.story("Проверка отображения")
    @allure.tag('ui', 'cards', 'positive', 'regress')
    @allure.severity(allure.severity_level.BLOCKER)
    def test_assert_product_card(self):
        with allure.step('Нажимаем на кнопку "Для Бизнеса"'):
            middel_page.type_business()
        with allure.step('Проверяем все доступные карты "Для Бизнеса"'):
            middel_page.card_list_bussines()
        with allure.step('Нажимаем на кнопку "Для всех"'):
            middel_page.type_all()
        with allure.step('Проверяем все доступные карты "Для всех"'):
            middel_page.cards_list_all()


"""Test #5"""


@pytest.mark.usefixtures('local')
class TestAllCreditCard:

    @allure.epic("Кредит наличными")
    @allure.feature("Банковские карты")
    @allure.story("Проверка отображения")
    @allure.tag('ui', 'cards', 'positive', 'regress')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_assert_page_credit_card(self):
        with allure.step(
                'Проверяем что страница форма - "Кредит наличными", заполняем номер телефона и проверяем что кнопка доступна'):
            cart_page.check_card()


"""Test #6"""


@pytest.mark.usefixtures('local')
class TestBusinessCreditCard:
    @allure.epic("Эквайринг для бизнеса")
    @allure.feature("Продукты для бизнеса")
    @allure.story("Проверка отображения и формы")
    @allure.tag('ui', 'business', 'positive', 'regress')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_assert_acquiring_product(self):
        with allure.step('Проверка открытия страницы эквайринга'):
            middel_page.type_business()
        with allure.step('Проверка отображение продукта "Торговый эквайринг"'):
            acquiring_page.acquiring_page()


"""Test #7"""


@pytest.mark.usefixtures('local')
class TestPayment:
    @allure.epic("Платежи и переводы")
    @allure.feature("Открытие страницы платежей")
    @allure.story("Проверка успешного открытия")
    @allure.tag('ui', 'payment', 'positive', 'regress')
    @allure.severity(allure.severity_level.BLOCKER)
    def test_open_payment_page(self):
        with allure.step('Проверяем баннер'):
            footer_page.assert_info_banner()
        with allure.step('Проверяем заголовок искомой страницы - "Всё самое нужное под рукой"'):
            footer_page.assert_header()
        with allure.step('Нажимаем "Платежи и переводы"'):
            footer_page.open_payment()
        with allure.step('Проверяем что попали на страницу "Платежи"'):
            footer_page.assert_header_page_payment()
