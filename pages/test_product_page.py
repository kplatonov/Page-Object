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

"""
для разных тест-кейсов можно выделять общие функции, чтобы не повторять код. 
Эти функции называются setup — функция, которая выполнится перед запуском каждого теста из класса, 
обычно туда входит подготовка данных, и teardown — функция, которая выполняется ПОСЛЕ каждого теста из класса, 
обычно там происходит удаление тех данных, которые мы создали во время теста. 
Хороший автотест должен сработать даже на чистой базе данных и удалить за собой сгенерированные в тесте данные. 
Такие функции реализуются с помощью фикстур, которые мы изучили в предыдущем модуле. 
Чтобы функция запускалась автоматически перед каждым тест-кейсом, нужно пометить её как 
@pytest.fixture с параметрами scope="function", 
что значит запускать на каждую функцию, и autouse=True, что значит запускать автоматически без явного вызова фикстуры.

Мы уже немного говорили про независимость от контента в предыдущих шагах — идеальным решением было бы везде, 
где мы работаем со страницей продукта, создавать новый товар в нашем интернет-магазине перед тестом 
и удалять по завершении теста. К сожалению, наш интернет-магазин пока не имеет возможности создавать объекты по API, 
но в идеальном мире мы бы написали вот такой тест-класс в файле test_product_page.py:
"""

"""
@pytest.mark.login
class TestLoginFromProductPage(object):
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.product = ProductFactory(title = "Best book created by robot")
        # создаем по апи
        self.link = self.product.link
        yield
        # после этого ключевого слова начинается teardown
        # выполнится после каждого теста в классе
        # удаляем те данные, которые мы создали 
        self.product.delete()
        

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, self.link)
        # дальше обычная реализация теста

    def test_guest_should_see_login_link(self, browser):
        page = ProductPage(browser, self.link)
        # дальше обычная реализация теста

"""

@pytest.mark.step13
class TestUserAddToCartFromProductPage(object):
    #Шаги тестов не изменятся, добавится лишь регистрация перед тестами - реализовать в LoginPage метод register_new_user(self, email, password)
    @pytest.mark.parametrize('username', ["user-1", "user-2", "user-3"]
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, username):
        """
        открыть страницу регистрации
        зарегистрировать нового пользователя
        проверить, что пользователь залогинен
        """
        register_page = LoginPage(browser, 

    def test_user_cant_see_success_message(self):  #test_guest_cant_see_success_message
        """
        1) LoginPage.register_new_user

        Открываем страницу товара 
        Добавляем товар в корзину 
        Проверяем, что нет сообщения об успехе с помощью is_not_element_present
        """
        #link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"

        page = ProductPage(browser, link, 0)
        page.open()
        page.click_add_to_basket()
        page.get_code()
        page.should_not_be_success_message()  #is_not_element_present()

    def test_user_can_add_product_to_cart(self):   #test_guest_can_add_product_to_cart
        """
        1) LoginPage.register_new_user
        """
        #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

        page = ProductPage(browser, link, 5)
        page.open()
        page.click_add_to_basket()
        page.get_code()
        #time.sleep(50)
        page.should_be_goods_add_basket()
        page.should_be_message_cost_equal_price()
        page.should_be_name_equal()
