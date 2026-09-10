from selenium.webdriver.common.by import By


class HeaderLocators:
    CONSTRUCTOR_LINK = (
        By.XPATH,
        "//a[@href='/' and .//p[normalize-space()='Конструктор']]",
    )
    ORDER_FEED_LINK = (
        By.XPATH,
        "//a[@href='/feed' and .//p[normalize-space()='Лента Заказов']]",
    )
