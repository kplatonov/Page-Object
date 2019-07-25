"""
pytest -s -m MARK_NAME test_product_page.py
"""
import pytest
from product_page import ProductPage
from cart_page import CartPage
import time

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]) 
@pytest.mark.add_to_card
def test_guest_can_add_product_to_cart(browser, link):
    #link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link, 5)
    page.open()
    page.click_add_to_basket()
    page.get_code()
    #time.sleep(50)
    page.should_be_goods_add_basket()
    page.should_be_message_cost_equal_price()
    page.should_be_name_equal()

@pytest.mark.see
def test_guest_cant_see_success_message_after_adding_product_to_cart(browser): 
    """
    Открываем страницу товара 
    Добавляем товар в корзину 
    Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    """
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link, 0)
    page.open()
    page.click_add_to_basket()
    page.get_code()
    page.should_not_be_success_message()  #is_not_element_present()


@pytest.mark.see
def test_guest_cant_see_success_message(browser): 
    """
    Открываем страницу товара 
    Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    """
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link, 0)
    page.open()
    page.should_not_be_success_message()  #is_not_element_present()

@pytest.mark.see
def test_message_disappeared_after_adding_product_to_cart(browser): 
    """
    Открываем страницу товара
    Добавляем товар в корзину
    по совету time.sleep(1)
    Проверяем, что нет сообщения об успехе с помощью is_disappeared
    """
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link, 0)
    page.open()
    page.click_add_to_basket()
    page.get_code()
    time.sleep(2)
    page.should_be_disappeared() 

@pytest.mark.new_design
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.new_design
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.step10
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    """
    pytest -s (-m step10 | -k product_in_cart) --tb=line test_product_page.py

    Гость открывает страницу товара
    Переходит в корзину по кнопке в шапке 
    Ожидаем, что в корзине нет товаров
    Ожидаем, что есть текст о том что корзина пуста 
    """
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.click_go_to_basket()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.should_not_be_goods_in_cart()
    cart_page.should_be_text_basket_is_empty()
