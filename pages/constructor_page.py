import allure

from locators.constructor_locators import ConstructorLocators
from locators.header_locators import HeaderLocators
from pages.base_page import BasePage
from settings import ORDER_NUMBER_WAIT
from urls import Urls


FIREFOX_DRAG = """
const source = arguments[0];
const target = arguments[1];
const transfer = new DataTransfer();
transfer.setData('text/plain', 'ingredient');
source.dispatchEvent(new DragEvent('dragstart', {bubbles: true, dataTransfer: transfer}));
for (const name of ['dragenter', 'dragover', 'drop']) {
    target.dispatchEvent(new DragEvent(name, {bubbles: true, dataTransfer: transfer}));
}
source.dispatchEvent(new DragEvent('dragend', {bubbles: true, dataTransfer: transfer}));
"""


class ConstructorPage(BasePage):
    @allure.step("Открыть конструктор")
    def open(self):
        self.open_url(Urls.MAIN_PAGE)
        self.find(ConstructorLocators.TITLE)
        return self

    def is_open(self):
        return self.url_is(Urls.MAIN_PAGE)

    @allure.step("Перейти в ленту заказов")
    def go_to_feed(self):
        from pages.order_feed_page import OrderFeedPage

        self.click(HeaderLocators.ORDER_FEED_LINK)
        self.wait_url(Urls.ORDER_FEED_PAGE)
        return OrderFeedPage(self.driver)

    @allure.step("Открыть детали ингредиента")
    def open_ingredient(self):
        self.click(ConstructorLocators.BUN)
        self.find(ConstructorLocators.DETAILS_TITLE)

    def ingredient_details_are_open(self):
        return bool(self.texts(ConstructorLocators.DETAILS_TITLE))

    @allure.step("Закрыть детали ингредиента")
    def close_ingredient(self):
        self.click_last_visible(ConstructorLocators.MODAL_CLOSE)
        self.wait_hidden(ConstructorLocators.DETAILS_TITLE)

    def ingredient_details_are_closed(self):
        return not self.texts(ConstructorLocators.DETAILS_TITLE)

    def ingredient_count(self, card_locator):
        return int(self.child_text(card_locator, ConstructorLocators.COUNTER))

    def _drag_ingredient(self, card_locator):
        source = self.find(card_locator)
        target = self.find(ConstructorLocators.BASKET)
        self.scroll_to(source)
        if self.browser_name == "firefox":
            self.run_script(FIREFOX_DRAG, source, target)
        else:
            self.drag_to(source, target)

    @allure.step("Добавить ингредиент")
    def add_ingredient(self, card_locator):
        before = self.ingredient_count(card_locator)
        self._drag_ingredient(card_locator)
        self.until(lambda: self.ingredient_count(card_locator) > before)
        return self.ingredient_count(card_locator)

    def sauce_count(self):
        return self.ingredient_count(ConstructorLocators.SAUCE)

    def add_sauce(self):
        return self.add_ingredient(ConstructorLocators.SAUCE)

    def _order_number(self):
        for value in self.texts(ConstructorLocators.ORDER_NUMBER):
            if value.isdigit() and value != "9999":
                return int(value)
        return False

    @allure.step("Оформить заказ")
    def create_order(self):
        self.add_ingredient(ConstructorLocators.BUN)
        self.add_ingredient(ConstructorLocators.FILLING)
        self.click(ConstructorLocators.ORDER_BUTTON)
        return self.until(self._order_number, ORDER_NUMBER_WAIT)
