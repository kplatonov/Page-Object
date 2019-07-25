from base_page import BasePage
from locators import MainPageLocators
from locators import BasketPageLocators

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class CartPage(BasePage):
    def should_not_be_goods_in_cart(self):
        """    
        Ожидаем, что в корзине нет товаров
        """
        assert self.is_not_element_present(*BasketPageLocators.BASKET_TOTAL), "Total basket is presented, but should not be"

    def should_be_text_basket_is_empty(self):
        """
        Ожидаем, что есть текст о том что корзина пуста 
        """
        assert self.is_not_element_present(*BasketPageLocators.BASKET_IS_EMPTY_TEXT), "Text about emptiness basket is present, but should not be"
