from product_page import ProductPage
import time

def test_guest_can_add_product_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link, 5)
    page.open()
    page.click_add_to_basket()
    page.get_code()
    #time.sleep(100)
    page.should_be_goods_add_basket()
    page.should_be_message_cost_equal_price()
