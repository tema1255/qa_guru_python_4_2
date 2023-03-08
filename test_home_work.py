import pytest
from selene.support.shared import browser
from selene import be, have


def test_find_selene(set_size_browser_window, google_find):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_negative(set_size_browser_window, google_find):
    browser.element('[name="q"]').should(be.blank).type('vdfbsghrerh').press_enter()
    browser.element('[id="topstuff"]').should(have.text('ничего не найдено'))
