"""
pytest -v --tb=line --language=en test_main_page.py
"""
from pages.main_page import MainPage

# error page "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"

def test_guest_can_go_to_login_page(browser): 
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link, 10)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы - переходим на страницу логина


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link, 10)
    page.open()
    page.should_be_login_link()
