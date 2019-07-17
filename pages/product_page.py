﻿"""
Описать в нем метод для добавления в корзину.
Дописать методы-проверки.
Описать необходимые локаторы к элементам страницы.
"""
from base_page import BasePage
from selenium.webdriver.common.by import By
from locators import ProductPageLocators

from selenium.common.exceptions import NoSuchElementException

class ProductPage(BasePage):

    def click_add_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BUSKET)
        link.click()

    def get_code(self):
        self.solve_quiz_and_get_code()

    def should_be_goods_add_basket(self):
        assert self.is_element_present(*ProductPageLocators.ALERTTINNER), "Alert inner isn't presented"

    def should_be_message_cost_equal_price(self):
        try:
            price = self.browser.find_element(*ProductPageLocators.PRICE).text
        except NoSuchElementException:
            assert False, "NoSuchElementException for price"
        price_color = self.browser.find_element(*ProductPageLocators.PRICE_COLOR).text
        assert price == price_color, "Price is not equal"           #as string
