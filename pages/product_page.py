from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By

from pages.base_page import Page


class Product(Page):
    ADD_TO_CART = (By.ID, "add-to-cart-button")
    SIZE_SELECTION_TOOLTIP = (By.ID, 'a-popover-content-1')
    NEW_ARRIVAL_BUTTON = (By.XPATH, "//span[contains(text(),'New Arrivals')]")
    NEW_ARRIVAL_OPTIONS = (By.ID, "nav-flyout-aj:https://www.amazon.com/images/G/01/softlines/megamenu/prod/megamenu-contents_en_US._TTH_.json:subnav-sl-megamenu-8:0")

    def open_product(self, product_id):
        self.open_page(f'dp/{product_id}')

    def hover_add_to_cart(self):
        cart_button = self.find_element(*self.ADD_TO_CART)
        self.actions.move_to_element(cart_button)
        self.actions.perform()

    def verify_size_tooltip(self):
        self.wait_for_element_appear(*self.SIZE_SELECTION_TOOLTIP)

    def hover_new_arrivals(self):
        new_arrival_button = self.find_element(*self.NEW_ARRIVAL_BUTTON)
        self.actions.move_to_element(new_arrival_button).perform()

    def verify_new_arrival_options_appear(self):
        self.wait_for_element_appear(*self.NEW_ARRIVAL_OPTIONS)