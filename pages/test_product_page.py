from product_page import ProductPage
import time

def test_guest_can_add_product_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link, 10)
    page.open()
    page.click_add_to_basket()
    page.get_code()
    page.should_be_goods_add_basket()
    page.should_be_message_cost_equal_price()
