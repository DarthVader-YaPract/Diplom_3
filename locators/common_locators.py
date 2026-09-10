from selenium.webdriver.common.by import By


class CommonLocators:
    MODAL_OVERLAY = (
        By.CSS_SELECTOR,
        "div[class*='Modal_modal_overlay']",
    )
