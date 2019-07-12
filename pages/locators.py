from selenium.webdriver.common.by import By


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
