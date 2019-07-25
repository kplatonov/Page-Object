import pytest
from main_page import MainPage
from product_page import ProductPage
from cart_page import CartPage
from login_page import LoginPage

def test_guest_cant_see_product_in_cart_opened_from_main_page(browser):
    """
    Гость открывает главную страницу 
    Переходит в корзину по кнопке в шапке сайта
    Ожидаем, что в корзине нет товаров
    Ожидаем, что есть текст о том что корзина пуста 
    """
    link = "http://selenium1py.pythonanywhere.com"
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.click_go_to_basket()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.should_not_be_goods_in_cart()
    cart_page.should_be_text_basket_is_empty()

@pytest.mark.login_guest
class TestLoginFromMainPage(object):
    # не забываем передать первым аргументом self                       
    def test_guest_can_go_to_login_page(self, browser):     
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link, 10)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()
