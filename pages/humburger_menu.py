from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



class HamburgerMenu(Page):
    AMAZON_MUSIC_MENU_ITEM = (By.XPATH, "//ul[contains(@class, 'hmenu-visible')]//div[contains(text(), 'Amazon Music')]")
    AMAZON_MUSIC_MENU_ITEM_RESULTS = (By.CSS_SELECTOR, "ul.hmenu-visible a:not(.hmenu-back-button)")

    def click_amazon_music(self,*locator):
        self.wait_for_element_click(*self.AMAZON_MUSIC_MENU_ITEM)


    def amazon_music_items_count(self, expected_item_count):
        self.driver.wait.until(EC.visibility_of_all_elements_located(self.AMAZON_MUSIC_MENU_ITEM_RESULTS))
        actual = len(self.driver.find_elements(*self.AMAZON_MUSIC_MENU_ITEM_RESULTS))
        assert expected_item_count == actual, f'Expected {expected_item_count} items, but got {actual} items'
