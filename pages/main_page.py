﻿"""
pytest -v --tb=line --language=en test_main_page.py
"""

from .base_page import BasePage
from selenium.webdriver.common.by import By

from .locators import MainPageLocators

class MainPage(BasePage):

    def go_to_login_page(self):
        link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        link.click() 

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"  #* для распаковки кортежа