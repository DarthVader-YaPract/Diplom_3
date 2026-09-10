from selenium.webdriver import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as conditions
from selenium.webdriver.support.ui import WebDriverWait

from locators.common_locators import CommonLocators
from settings import ELEMENT_WAIT


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, ELEMENT_WAIT)

    @property
    def browser_name(self):
        return self.driver.name

    def open_url(self, url):
        self.driver.get(url)

    def find(self, locator):
        return self.wait.until(conditions.visibility_of_element_located(locator))

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def _no_visible_overlay(self, _):
        return not any(
            overlay.is_displayed()
            for overlay in self.find_all(CommonLocators.MODAL_OVERLAY)
        )

    def click(self, locator):
        self.wait.until(self._no_visible_overlay)
        element = self.wait.until(conditions.element_to_be_clickable(locator))
        try:
            element.click()
        except ElementClickInterceptedException:
            self.wait.until(self._no_visible_overlay)
            self.wait.until(conditions.element_to_be_clickable(locator)).click()

    def fill(self, locator, value):
        field = self.find(locator)
        field.clear()
        field.send_keys(value)

    def text(self, locator):
        return self.find(locator).text

    def child_text(self, parent_locator, child_locator):
        parent = self.find(parent_locator)
        return parent.find_element(*child_locator).text

    def texts(self, locator):
        return [
            element.text
            for element in self.find_all(locator)
            if element.is_displayed()
        ]

    def until(self, condition, timeout=ELEMENT_WAIT):
        return WebDriverWait(self.driver, timeout).until(lambda _: condition())

    def wait_url(self, url):
        self.wait.until(conditions.url_to_be(url))

    def url_is(self, url):
        return self.driver.current_url == url

    def wait_hidden(self, locator):
        self.wait.until(conditions.invisibility_of_element_located(locator))

    def click_last_visible(self, locator):
        elements = [
            element
            for element in self.find_all(locator)
            if element.is_displayed()
        ]
        elements[-1].click()

    def run_script(self, script, *args):
        return self.driver.execute_script(script, *args)

    def scroll_to(self, element):
        self.run_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def drag_to(self, source, target):
        ActionChains(self.driver).drag_and_drop(source, target).perform()
