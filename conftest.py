import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from helpers import provision_account, remove_account
from pages.constructor_page import ConstructorPage
from pages.login_page import LoginPage
from pages.order_feed_page import OrderFeedPage
from settings import ELEMENT_WAIT


os.environ["SE_SKIP_DRIVER_IN_PATH"] = "true"


def start_chrome():
    options = ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1440,1000")
    return webdriver.Chrome(options=options)


def start_firefox():
    options = FirefoxOptions()
    options.add_argument("-headless")
    options.add_argument("--width=1440")
    options.add_argument("--height=1000")
    return webdriver.Firefox(options=options)


BROWSERS = (
    pytest.param(start_chrome, id="chrome"),
    pytest.param(start_firefox, id="firefox"),
)


@pytest.fixture(params=BROWSERS)
def driver(request):
    driver = request.param()
    driver.set_page_load_timeout(ELEMENT_WAIT)
    yield driver
    driver.quit()


@pytest.fixture
def registered_user():
    user = provision_account()
    yield user
    remove_account(user)


@pytest.fixture
def constructor_page(driver):
    return ConstructorPage(driver).open()


@pytest.fixture
def feed_page(driver):
    return OrderFeedPage(driver).open()


@pytest.fixture
def feed(driver):
    return OrderFeedPage(driver)


@pytest.fixture
def signed_in_constructor(driver, registered_user):
    login = LoginPage(driver).open()
    return login.login(registered_user["email"], registered_user["password"])
