from selenium.webdriver.common.by import By

from settings import BUN_CARD_ID, FILLING_CARD_ID, SAUCE_CARD_ID


class ConstructorLocators:
    TITLE = (By.XPATH, "//h1[normalize-space()='Соберите бургер']")
    BUN = (By.CSS_SELECTOR, f"a[href='/ingredient/{BUN_CARD_ID}']")
    FILLING = (By.CSS_SELECTOR, f"a[href='/ingredient/{FILLING_CARD_ID}']")
    SAUCE = (By.CSS_SELECTOR, f"a[href='/ingredient/{SAUCE_CARD_ID}']")
    BASKET = (By.CSS_SELECTOR, "section[class*='BurgerConstructor_basket__']")
    COUNTER = (By.CSS_SELECTOR, "div[class*='counter_counter__'] p")
    DETAILS_TITLE = (
        By.XPATH,
        "//h2[normalize-space()='Детали ингредиента']",
    )
    MODAL_CLOSE = (By.CSS_SELECTOR, "button[class*='Modal_modal__close']")
    ORDER_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Оформить заказ']",
    )
    ORDER_NUMBER = (
        By.XPATH,
        "//p[normalize-space()='идентификатор заказа']/preceding-sibling::h2[1]",
    )
