import pytest
from selene.support.shared import browser
from selene import be, have


def test_find_selene(set_size_browser_window):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Yashaka/Selene Alternatives and Reviews (Jan 2023) - LibHunt'))

def test_negative(set_size_browser_window):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('vсрабждо321dfbsghrerh').press_enter()
    browser.element('[id="topstuff"]').should(have.text('По запросу vсрабждо321dfbsghrerh ничего не найдено.'))
