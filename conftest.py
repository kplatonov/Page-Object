import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome", help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en", help="Enter language")


#@pytest.mark.parametrize('language', ["ru", "en-gb"])
#def test_guest_should_see_login_link(browser, language):
#    link = "http://selenium1py.pythonanywhere.com/{}/".format(language)
#    browser.get(link)
#    browser.find_element_by_css_selector("#login_link")

"""
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
browser = webdriver.Chrome(options=options)
Для Firefox объявление нужного языка будет выглядеть немного иначе:

fp = webdriver.FirefoxProfile()
fp.set_preference("intl.accept_languages", user_language)
browser = webdriver.Firefox(firefox_profile=fp)
"""

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")     # ?? request.config.getoption("browser_name")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        print("Browser {} still is not implemented".format(browser_name))
    yield browser
    print("\nquit browser..")
    browser.quit()


#@pytest.fixture()
#def login_page(web_driver) -> LoginPage:
#    """
#    Фикстура для быстрого перехода на страницу авторизации
#    :param web_driver: фикстура инициализации веб драйвера
#    :return: экземпляр класса LoginPage
#    """
#    page = LoginPage(web_driver)
#    page.navigate()
#    return page

