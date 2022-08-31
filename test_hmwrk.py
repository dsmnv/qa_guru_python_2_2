import pytest
from selene.support.shared import browser
from selene import be, have, config


@pytest.fixture()
def open_browser():
    browser.open('https://google.com/ncr')

@pytest.fixture()
def resize_browser_fhd():
    browser.config.window_width = 1920
    browser.config.window_heightn = 1080


def test_positive(open_browser, resize_browser_fhd):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

