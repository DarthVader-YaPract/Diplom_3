import allure

from locators.header_locators import HeaderLocators
from locators.order_feed_locators import OrderFeedLocators
from pages.base_page import BasePage
from settings import ORDER_NUMBER_WAIT
from urls import Urls


class OrderFeedPage(BasePage):
    @allure.step("Открыть ленту заказов")
    def open(self):
        self.open_url(Urls.ORDER_FEED_PAGE)
        self.find(OrderFeedLocators.TITLE)
        return self

    def is_open(self):
        return self.url_is(Urls.ORDER_FEED_PAGE)

    @allure.step("Перейти в конструктор")
    def go_to_constructor(self):
        from pages.constructor_page import ConstructorPage

        self.click(HeaderLocators.CONSTRUCTOR_LINK)
        self.wait_url(Urls.MAIN_PAGE)
        return ConstructorPage(self.driver)

    def total_count(self):
        return int(self.text(OrderFeedLocators.TOTAL).replace(" ", ""))

    def today_count(self):
        return int(self.text(OrderFeedLocators.TODAY).replace(" ", ""))

    @allure.step("Дождаться изменения общего счётчика")
    def wait_total_increase(self, before):
        self.until(lambda: self.total_count() > before, ORDER_NUMBER_WAIT)
        return self.total_count()

    @allure.step("Дождаться изменения счётчика за сегодня")
    def wait_today_increase(self, before):
        self.until(lambda: self.today_count() > before, ORDER_NUMBER_WAIT)
        return self.today_count()

    @allure.step("Дождаться заказа в работе")
    def order_appears_in_progress(self, order_number):
        number = str(order_number)
        padded = number.zfill(7)

        def number_is_visible():
            text = self.text(OrderFeedLocators.IN_PROGRESS)
            return padded in text or number in text.split()

        return self.until(number_is_visible, ORDER_NUMBER_WAIT)
