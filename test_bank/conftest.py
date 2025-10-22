import allure
import pytest
import requests
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def browser_config_open():
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options


    yield
    browser.quit()