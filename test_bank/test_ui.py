import time

from selene import browser, have
from components_page.module_header.header import selector_found_header

def test_browser(selenoid_test):
    browser.element('[type="submit"]').click()

# browser.all(selector_found_header.selector_middle_button).first.click()
# browser.all(selector_found_header.selector_middle_button).second.click()
# browser.all(selector_found_header.selector_middle_button)[2].click()
