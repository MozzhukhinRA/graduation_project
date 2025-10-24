import os
import pytest
from dotenv import load_dotenv
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils import attach


@pytest.fixture(scope='function')
def local_test():
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options

    browser.driver.set_window_size(1920, 1080)
    browser.open('https://uralsib.ru/')

    yield

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)

    browser.quit()


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope="function")
def selenoid_test():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "127.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True,
            "enableLog": True,
            "logName": "browser.log"
        }
    }
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        options=options)

    browser.config.driver = driver
    browser.driver.set_window_size(1920, 1080)
    browser.open('https://uralsib.ru/')

    yield browser

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)

    browser.quit()

@pytest.fixture(scope='function')
def allure_test():
    pass

@pytest.fixture(scope='function')
def bstack_test():
    pass