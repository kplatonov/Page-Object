from base_page import BasePage
from locators import LoginPageLocators
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        #assert self.browser.current_url == self.url, "Login link invalid"
        assert 'login' in self.browser.current_url
        assert True

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        #assert self.is_element_present(By.CSS_SELECTOR, LoginPageLocators.LOGIN_USERNAME), "There isn't login form"
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME), "There isn't login form"
        assert True

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        #assert self.is_element_present(By.CSS_SELECTOR, LoginPageLocators.REGISTRATION_EMAIL), "There isn't register form"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL), "There isn't register form"
        assert True


    def register_new_user(self, email, password):
        #принимает две строки и регистрирует пользователя. Реализуйте его, описав соответствующие элементы страницы.
        self.should_be_login_page()
        self.select_element(*LoginPageLocators.REGISTRATION_EMAIL, email) 
        self.select_element(*LoginPageLocators.REGISTRATION_PASSWORD1, password)
        self.select_element(*LoginPageLocators.REGISTRATION_PASSWORD2, password)

        self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT).click()
