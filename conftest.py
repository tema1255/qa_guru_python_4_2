import pytest
from selene.support.shared import browser
@pytest.fixture()
def set_size_browser_window():
        browser.config.window_width = 1024
        browser.config.window_height = 768