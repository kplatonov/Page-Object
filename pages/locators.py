from selenium.webdriver.common.by import By


class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, "//span[@class='btn-group']/a[contains(@href, 'basket')]")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators(object):
    BASKET_TOTAL = (By.ID, "basket_totals")
    BASKET_IS_EMPTY_TEXT = (By.XPATH, "//*[@id='content_inner']/p/text()")

class LoginPageLocators(object):
    LOGIN_USERNAME = (By.CSS_SELECTOR, "[name='login-username']")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "[name='login-password']")
    LOGIN_SUBMIT = (By.CSS_SELECTOR, "[name='login_submit']")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "[name='registration-email']")
    REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, "[name='registration-password1']")
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, "[name='registration-password2']")
    REGISTRATION_SUBMIT = (By.CSS_SELECTOR, "[name='registration_submit']")

class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class ProductPageLocators(object):
    BTN_ADD_TO_BUSKET = (By.CLASS_NAME, "btn-add-to-basket")    #"btn btn-lg btn-primary btn-add-to-basket")
    ALERTTINNER = (By.CLASS_NAME, "alert-info")    #"alertinner")    #check visibled
    
    #PRICE = (By.XPATH, "//div[@class='alert alert-safe alert-noicon alert-info  fade in']/div[@class='alertinner ']/p[1]/strong")  #"//*[@id='messages']/div[3]/div/p[1]/strong")
    PRICE = (By.XPATH, "//div[contains(@class, 'alert-info')]/div[@class='alertinner ']/p[1]/strong")
    #By.cssSelector(".class1.class2")

    #PRICE_COLOR = (By.CLASS_NAME, "price_color")    # + By.TAG_NAME
    PRICE_COLOR = (By.XPATH, "//p[@class='price_color']")
    NAME_IN_MESSAGE = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    NAME_BOOK = (By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/h1")
    SUCCESS_MESSAGE = (By.XPATH, "//*[@id='messages']/div[1]/div")

