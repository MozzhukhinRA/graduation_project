import time

from selene import browser, be, have

from components_page.module_header.credit_card_application.credit_user import user_test_reg
from components_page.module_header.header import selector_found_header
from components_page.module_header.credit_card_application.credit_form import selector_credit_form


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


class CreditPage:

    def check_header(self):
        browser.element(selector_credit_form.header_name_form).should(have.text('Оформите заявку на кредитную карту'))

    def registration_credit_form(self):
        user = user_test_reg()
        (browser.element(selector_credit_form.field_fio).should(be.visible).type(
            f'{user["last_name"]} '
            f'{user["first_name"]} '
            f'{user["middel_name"]}'
        )
        )
        browser.element(selector_credit_form.field_phone).should(be.visible).with_(time.sleep(1)).click()
        browser.element(selector_credit_form.field_phone).should(be.visible).type(f'9{user["phone"][2:]}')
        browser.element(selector_credit_form.field_email).type(f'{user["email"]}')
        browser.element(selector_credit_form.field_birthday).should(be.visible).with_(timeout=15).type(
            f'{user["birth"]}')
        browser.element(selector_credit_form.checkbox_1).with_(timeout=15).click()
        browser.element(selector_credit_form.checkbox_2).with_(timeout=15).click()
        browser.element(selector_credit_form.button_continue).with_(timeout=15).should(be.visible).click()


main_page = MainPage()
credit_page = CreditPage()
