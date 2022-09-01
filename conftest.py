import pytest
from selene.support.shared import browser

@pytest.fixture()
def browser_config_fhd():
    browser.config.window_width = 1920
    browser.config.window_height = 1080

@pytest.fixture()
def open_browser_fhd(browser_config_fhd):
    browser.open('https://google.com/ncr')