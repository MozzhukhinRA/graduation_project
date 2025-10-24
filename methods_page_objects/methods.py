from selene import browser
from components_page.module_header.header import selector_found_header

def switch_product_on_main_page_left():
    browser.element(selector_found_header.selector_left_arrow).click()

def switch_product_on_main_page_right():
    browser.element(selector_found_header.selector_right_arrow).click()

def open_menu():
    browser.element(selector_found_header.selector_left_upper_button).click()

def open_login_page():
    browser.element(selector_found_header.selector_login_button).click()

def click_on_product():
    browser.element(selector_found_header.selector_middle_button).click()

