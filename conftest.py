import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def user_language_addoption(parser):
   parser.addoption('--language', action='store', default=None,
                     help="Choose frome langs: (en/ru/es/...)")

@pytest.fixture(scope="function")
def browser(request):
    user_laguage = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome("D:\Python\Python310\chromedriver.exe", options=options)
    yield browser
    browser.quit()