import allure

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
from urls import Urls


class LoginPage(BasePage):
    @allure.step("Открыть страницу входа")
    def open(self):
        self.open_url(Urls.LOGIN_PAGE)
        self.find(LoginPageLocators.TITLE)
        return self

    @allure.step("Войти в аккаунт")
    def login(self, email, password):
        from pages.constructor_page import ConstructorPage

        self.fill(LoginPageLocators.EMAIL, email)
        self.fill(LoginPageLocators.PASSWORD, password)
        self.click(LoginPageLocators.SUBMIT)
        self.wait_url(Urls.MAIN_PAGE)
        return ConstructorPage(self.driver)
