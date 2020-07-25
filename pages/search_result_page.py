from selenium.webdriver.common.by import By

from pages.base_page import Page


class SearchResults(Page):
    RESULTS_INFO = (By.CSS_SELECTOR, ".a-color-state.a-text-bold")


    def verify_found_result_text(self, search_word):
        self.verify_text(search_word, *self.RESULTS_INFO)



