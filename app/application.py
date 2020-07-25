from pages.base_page import Page
from pages.humburger_menu import HamburgerMenu
from pages.product_page import Product
from pages.top_nav_menu import TopNavMenu
from pages.search_result_page import SearchResults
from pages.signin_page import SignInPage
from pages.cart_page import Cart

class Application:

    def __init__(self, driver):
        self.driver = driver

        self.page = Page(self.driver)
        self.top_nav_menu = TopNavMenu(self.driver)
        self.search_result_page = SearchResults (self.driver)
        self.signin_page = SignInPage(self.driver)
        self.cart_page = Cart(self.driver)
        self.product_page = Product(self.driver)
        self.hamburger_menu = HamburgerMenu(self.driver)