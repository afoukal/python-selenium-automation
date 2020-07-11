from pages.base_page import Page
from selenium.webdriver.common.by import By


class TopNavMenu(Page):
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SEARCH_SUBMIT = (By.XPATH, "//input[@value='Go']")
    ORDERS = (By.XPATH, "//*[@id='nav-orders']/span[2]")
    CART = (By.ID, "nav-cart")
    HM = (By.ID, "nav-hamburger-menu")

    def search_word(self, search_word):
        self.input(search_word, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_SUBMIT)


    def click_orders(self, *locator):
        self.click(*self.ORDERS)


    def open_cart(self, *locator):
        self.click(*self.CART)


    def click_hamburger_menu(self, *locator):
        self.click(*self.HM)