from main_page import MainPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link, 10)
    page.open()
    login_page = page.go_to_login_page()
    login_page.should_be_login_page()



#second approach
#comment last line in go_to_login_page:
#def go_to_login_page(self):
#    link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
#    link.click()
#    # return LoginPage(browser=self.browser, url=self.browser.current_url) 

from pages.login_page import LoginPage

def test_guest_can_go_to_login_page_2(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link, 10)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()