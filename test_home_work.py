import pytest
from selene.support.shared import browser
from selene import be, have


def test_find_selene(set_size_browser_window, google_find):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('selene полезная вещь'))

def test_negative(set_size_browser_window, google_find):
    browser.element('[name="q"]').should(be.blank).type('vdfbsghrerh').press_enter()
    browser.element('[id="topstuff"]').should(have.text('По запросу vdfbsghrerh ничего не найдено.'))
