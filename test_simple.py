import pytest
import random

@pytest.fixture(scope='session')
def browser():
    print('откр браузер')
    yield random.randint(0, 100)
    print('закр браузер')

@pytest.fixture()
def get_admin(browser):  # фикстура get_admin зависит от browser
    return random.randint(0, 100)


def test_simple(get_admin, browser):  # функция зависит от get_admin
    #assert get_admin == 5, 'айдишник админа ожидался 5'
    print(browser)
    assert 1 == 1, 'единица не равна 2'

def test_somesing(get_admin, browser):  # функция зависит от get_admin
    #assert get_admin == 5, 'айдишник админа ожидался 5'
    print(browser)
    assert 1 == 1, 'единица не равна 2'