﻿"""
pytest -v --tb=line --language=en test_main_page.py
"""

"""
def go_to_login_page(self):
    #link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
    link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
    link.click()
    return LoginPage(browser=self.browser, url=self.browser.current_url) 


def should_be_login_link(self):
    assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"  #* для распаковки кортежа
"""



from base_page import BasePage
from selenium.webdriver.common.by import By
from login_page import LoginPage

from locators import MainPageLocators

class MainPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

        
