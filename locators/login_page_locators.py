from selenium.webdriver.common.by import By


class LoginPageLocators:
    TITLE = (By.XPATH, "//h2[normalize-space()='Вход']")
    EMAIL = (By.CSS_SELECTOR, "input[type='text']")
    PASSWORD = (By.CSS_SELECTOR, "input[type='password']")
    SUBMIT = (By.XPATH, "//button[normalize-space()='Войти']")
