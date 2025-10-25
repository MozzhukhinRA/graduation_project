import time

from selene import browser, be, have

from components_page.module_header.credit_card_application.credit_user import user_test_reg
from components_page.module_header.header import selector_found_header
from components_page.module_middel.middel import selector_found_middel
from components_page.module_header.credit_card_application.credit_form import selector_credit_form
from components_page.module_header.main_menu.main_menu import selector_menu


class MainPage:

    def switch_product_on_main_page_left(self):
        browser.element(selector_found_header.selector_left_arrow).should(be.visible).click()

    def switch_product_on_main_page_right(self):
        browser.element(selector_found_header.selector_right_arrow).should(be.visible).click()

    def open_menu(self):
        browser.element(selector_found_header.selector_left_upper_button).should(be.visible).click()

    def open_login_page(self):
        browser.element(selector_found_header.selector_login_button).should(be.visible).click()

    def click_on_product(self):
        browser.element(selector_found_header.selector_middel_button).should(be.visible).click()

    def comeback(self):
        browser.element(selector_found_header.selector_lable_button).click()


class CreditPage:

    def check_header(self):
        browser.element(selector_credit_form.header_name_form).should(have.text('Оформите заявку на кредитную карту'))

    def registration_credit_form(self):
        user = user_test_reg()
        (browser.element(selector_credit_form.field_fio).should(be.visible).with_(time.sleep(1)).type(
            f'{user["last_name"]} '
            f'{user["first_name"]} '
            f'{user["middel_name"]}'
        )
        )
        browser.element(selector_credit_form.field_phone).should(be.visible).click()
        browser.element(selector_credit_form.field_phone).should(be.visible).type(f'9{user["phone"][2:]}')
        browser.element(selector_credit_form.field_email).type(f'{user["email"]}')
        browser.element(selector_credit_form.field_birthday).should(be.visible).type(
            f'{user["birth"]}')
        browser.element(selector_credit_form.checkbox_1).click()
        browser.element(selector_credit_form.checkbox_2).with_(timeout=15).click()
        browser.element(selector_credit_form.button_continue).with_(timeout=15).should(be.visible).click()


class MainMenuPage:

    def size_element_in_menu(self):
        browser.all(selector_menu.menu_buttons).should(have.size(13))

    def assert_text_and_click(self):
        browser.element(selector_menu.bankomats_and_office).should(have.text('Банкоматы и офисы')).click()


class MiddelPage:

    def type_all(self):
        browser.all(selector_found_middel.selector_switcher_for_all_and_business).first.should(
            have.text('Для всех')).with_(time.sleep(1)).click()

    def type_business(self):
        browser.all(selector_found_middel.selector_switcher_for_all_and_business).second.should(
            have.text('Для бизнеса')).with_(time.sleep(1)).click()

    def cards_list_all(self):
        cards = browser.all(selector_found_middel.card)
        cards.should(have.size(6))
        cards[0].should(have.exact_text('Кредитные карты'))
        cards[1].should(have.exact_text('Дебетовые карты'))
        cards[2].should(have.exact_text('Кредиты'))
        cards[3].should(have.exact_text('Ипотека'))
        cards[4].should(have.exact_text('Вклады и счета'))
        cards[5].should(have.exact_text('Премиум'))

    def card_list_bussines(self):
        cards = browser.all(selector_found_middel.card)
        cards.should(have.size(6))
        cards[0].should(have.exact_text('РКО'))
        cards[1].should(have.exact_text('Эквайринг'))
        cards[2].should(have.exact_text('Бизнес-карты'))
        cards[3].should(have.exact_text('Кредиты'))
        cards[4].should(have.exact_text('Гарантии'))
        cards[5].should(have.exact_text('ВЭД'))


menu_page = MainMenuPage()
main_page = MainPage()
credit_page = CreditPage()
middel_page = MiddelPage()
