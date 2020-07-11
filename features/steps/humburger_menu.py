from behave import then, when
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


@when("Click on hamburger menu")
def locate_item(context):
    context.app.top_nav_menu.click_hamburger_menu()


@when('Click on Amazon Music menu item')
def click_amazon_music(context):
    context.app.hamburger_menu.click_amazon_music()

@then('{expected_item_count} menu items are present')
def verify_amount_of_items(context, expected_item_count):
    expected_item_count = int(expected_item_count)  # 6
    context.app.hamburger_menu.amazon_music_items_count(expected_item_count)




#     context.driver.wait.until(correct_menu_items_present(AMAZON_MUSIC_MENU_ITEM_RESULTS, expected_item_count), "Amount of items is incorrect")
#     actual = len(context.driver.find_elements(*AMAZON_MUSIC_MENU_ITEM_RESULTS))
#     assert expected_item_count == actual, f'Expected {expected_item_count} items, but got {actual} items'
#
# class correct_menu_items_present(object):
#     def __init__(self, locator, amount):
#         self.locator = locator
#         self.amount = amount
#
#     def __call__(self, driver):
#         elements = driver.find_elements(*self.locator)  # Finding the referenced element
#         if len(elements) == self.amount:
#             return elements
#         else:
#             return False