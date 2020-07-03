from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from behave import when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

TODAY_DEALS = (By.XPATH, "//a[contains(text(),'Deals')]")
UNDER_25 = (By.CSS_SELECTOR, "[data-value='-25'] a")
UNDER_25_SUM = (By.CSS_SELECTOR, ".a-link-normal.summary span")
ANY_DEAL = (By.CSS_SELECTOR, ".a-button-span12")
DEAL_OF_DAY = (By.CSS_SELECTOR, ".a-section.octopus-dlp-image-shield")
ADD_TO_CART = (By.ID, "add-to-cart-button")
CART = (By.ID, "nav-cart")
SUBTOTAL = (By.ID, 'sc-subtotal-label-activecart')


@when('Store original windows')
def store_original_windows(context):
    context.old_windows = context.driver.window_handles
    context.current_window = context.driver.current_window_handle


@when("Click to open Today's Deals in new tab")
def open_deals_under25(context):
    context.driver.find_element(*TODAY_DEALS).send_keys(Keys.CONTROL+Keys.ENTER)
    context.driver.wait.until(EC.new_window_is_opened)


@when('Switch to the newly opened window')
def switch_to_new_window(context):
    current_windows = context.driver.window_handles
    # for old_window in context.old_windows:
    #     current_windows.remove(old_window)
    # context.driver.switch_to_window(current_windows[0])
    context.driver.switch_to_window(current_windows[1])


@when("Choose Under 25")
def choose_under_25(context):
    context.driver.wait.until(EC.element_to_be_clickable(UNDER_25))
    context.driver.find_element(*UNDER_25).click()


@then('Verify that deals under 25 are shown')
def verify_under_25(context):
    under_25_text = context.driver.find_element(*UNDER_25_SUM).text
    assert 'Under $25' in under_25_text, f'Supposed to be deals under 25, but found {under_25_text}'


@when('User put any product into a cart')
def put_product_to_cart(context):
    context.driver.find_element(*ANY_DEAL).click()
    context.driver.find_element(*DEAL_OF_DAY).click()
    context.driver.find_element(*ADD_TO_CART).click()


@when('Close new window and can switch back to original')
def close_new_window(context):
    context.driver.close()
    context.driver.switch_to_window(context.current_window)


@when('Refresh the page')
def refresh_page(context):
    context.driver.refresh()
    context.driver.find_element(*CART).click()


@then('Cart has 1 item')
def verify_cart_item(context):
    subtotal_text = context.driver.find_element(*SUBTOTAL).text
    assert '1 item' in subtotal_text, f'Supposed to be 1 item , but found {subtotal_text}'





