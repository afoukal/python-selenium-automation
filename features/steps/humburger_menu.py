from behave import then
from selenium.webdriver.common.by import By

HM = (By.ID, "nav-hamburger-menu")

@then("Locate  hamburger menu")
def locate_item(context):
    context.driver.find_element(*HM)