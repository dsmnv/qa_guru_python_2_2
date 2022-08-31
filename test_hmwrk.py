import pytest
from selene.support.shared import browser
from selene import be, have, config

config.hold_browser_open = True

@pytest.fixture()
def browser_config_fhd():
    browser.config.window_width = 1920
    browser.config.window_height = 1080

@pytest.fixture()
def browser_config_mobile():
    browser.config.window_width = 390
    browser.config.window_height = 844

@pytest.fixture()
def open_browser_fhd(browser_config_fhd):
    browser.open('https://google.com/ncr')

@pytest.fixture()
def open_browser_mobile(browser_config_mobile):
    browser.open('https://google.com/ncr')

# ПК
def test_find_selene_positive(open_browser_fhd):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_find_selene_negative(open_browser_fhd):
    browser.element('[name="q"]').should(be.blank).type('selenium').press_enter()
    browser.element('[id="search"]').should(have.no.text('Selene - User-oriented Web UI browser tests in Python'))

# моб

def test_find_selene_positive_mobile(open_browser_mobile):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_find_selene_negative_mobile(open_browser_mobile):
    browser.element('[name="q"]').should(be.blank).type('selenum').press_enter()
    browser.element('[id="search"]').should(have.no.text('Selene - User-oriented Web UI browser tests in Python'))