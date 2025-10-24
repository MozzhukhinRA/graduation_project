import time

import pytest
from selene import browser, have
import methods_page_objects
from methods_page_objects.methods import click_on_product
from test_bank.conftest import local_test


def test_browser(selenoid_test):
    browser.element('[type="submit"]').click()

# browser.all(selector_found_header.selector_middle_button).first.click()
# browser.all(selector_found_header.selector_middle_button).second.click()
# browser.all(selector_found_header.selector_middle_button)[2].click()

@pytest.mark.usefixtures('local_test')
class TestProductBannerAndFormCredit:

    def test_take_card(self):
        click_on_product()
        browser.element('#card-enerjeans-name').type('12345')
        time.sleep(3)