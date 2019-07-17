﻿from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators(object):
    LOGIN_USERNAME = (By.CSS_SELECTOR, "[name='login-username']")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "[name='login-password']")
    LOGIN_SUBMIT = (By.CSS_SELECTOR, "[name='login_submit']")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "[name='registration-email']")
    REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, "[name='registration-password1']")
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, "[name='registration-password2']")
    REGISTRATION_SUBMIT = (By.CSS_SELECTOR, "[name='registration_submit']")

class ProductPageLocators(object):
    BTN_ADD_TO_BUSKET = (By.CLASS_NAME, "btn-add-to-basket")    #"btn btn-lg btn-primary btn-add-to-basket")
    ALERTTINNER = (By.CLASS_NAME, "alert-info")    #"alertinner")    #check visibled
    PRICE = (By.XPATH, "//*[@id='messages']/div[3]/div/p[1]/strong")  #"//div[@class='alertinner']/p/strong")
    #PRICE_COLOR = (By.CLASS_NAME, "price_color")    #check visibled
    PRICE_COLOR = (By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/p[1]")