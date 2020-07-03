from behave import then, when
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


POPUP = (By.CSS_SELECTOR, "#nav-signin-tooltip span")


@then("Verify Sign in popup is present")
def popup_present_clickable(context):
    context.driver.wait.until(EC.presence_of_element_located(POPUP))
    context.driver.wait.until(EC.element_to_be_clickable(POPUP))


@when("Sign in popup disappears")
def invisible_popup(context):
    assert context.driver.wait.until(EC.invisibility_of_element(POPUP))


@then("Verify Sign in popup is not clickable")
def popup_unclickable(context):
    context.driver.wait.until(EC.invisibility_of_element(POPUP))
