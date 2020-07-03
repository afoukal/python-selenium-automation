from time import sleep

from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

PECAN_LODGE = (By.XPATH, "//*[text()='pecanlodge.com']")
LOGO = (By.XPATH, "//img[@alt='Pecan Lodge']")


@given('Open Yelp web page')
def open_restaurant(context):
    context.driver.get("https://www.yelp.com/biz/pecan-lodge-dallas-3?osq=Restaurants")


@when('Click on restaurant web page')
def click_link(context):
    context.old_windows = context.driver.window_handles
    context.original_window = context.driver.current_window_handle
    context.driver.find_element(*PECAN_LODGE).click()


@when('Verify the new window was opened')
def verify_new_opened(context):
    context.driver.wait.until(EC.new_window_is_opened)
    current_windows = context.driver.window_handles
    #context.driver.switch_to_window(current_windows[1])
    for old_window in context.old_windows:
        current_windows.remove(old_window)
    context.driver.switch_to_window(current_windows[0])
    logo = context.driver.find_element(*LOGO)
    assert 'Pecan Lodge' in logo.get_attribute('alt')


@then('Close new window and return to Yelp')
def new_window_close(context):
    context.driver.close()
    context.driver.switch_to_window(context.original_window)


