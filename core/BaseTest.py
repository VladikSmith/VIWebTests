import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='session')
def browser():
    chrome_options = Options()
    chrome_options.add_argument('--lang=ru')
    chrome_options.add_argument('--start-maximized')
    driver = webdriver.Remote(command_executor='http://83.222.25.223:4444',options=chrome_options)
    yield driver
    driver.quit()
