from pages.base_page import Page
from selenium.webdriver.common.by import By

class SignInPage(Page):
    SIGN_IN_TEXT = (By.XPATH, "//h1[@class='a-spacing-small']")


    def sign_in_text(self, text):
        self.verify_text(text, *self.SIGN_IN_TEXT)


    def verify_title(self, text):
        title = self.driver.title
        assert text in title, f'{title} is displayed instead'