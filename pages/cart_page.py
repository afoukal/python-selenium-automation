from selenium.webdriver.common.by import By
from pages.base_page import Page

class Cart(Page):

    EMPTY_MSG = (By.CSS_SELECTOR, ".sc-your-amazon-cart-is-empty h2")

    def verify_cart_empty(self, text):
        self.verify_text(text, *self.EMPTY_MSG)
