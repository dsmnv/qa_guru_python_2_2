from selene.support.shared import browser
from selene import be, have

search = 'biburibaba'
def test_find_selene_positive(open_browser_fhd):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_find_selene_negative(open_browser_fhd):
    browser.element('[name="q"]').should(be.blank).type(search).press_enter()
    browser.element('[id="topstuff"]').should(be.visible)
    browser.element('[id="topstuff"]').should(have.text(search))
