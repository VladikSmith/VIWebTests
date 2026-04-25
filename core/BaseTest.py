import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='session')
def browser():
    chrome_options = Options()
    chrome_options.add_argument('--lang=ru')
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()
