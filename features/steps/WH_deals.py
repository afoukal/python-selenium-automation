from behave import given, then
from selenium.webdriver.common.by import By

RESULTS = (By.CSS_SELECTOR, ".s-result-list.s-col-2 li")
REGULAR = (By.CSS_SELECTOR, ".s-result-list.s-col-2 span.wfm-sales-item-card__regular-price")
PRODUCT_NAME = (By.CSS_SELECTOR, ".s-result-list.s-col-2 span.wfm-sales-item-card__product-name")


@given('Open Amazon WholeFoods Deals')
def open_wh_deals(context):
    context.driver.get("https://www.amazon.com/wholefoodsdeals")


@then('Each item has {regular} field and Product name')
def verify_regular_field(context, regular):
    product_list = context.driver.find_elements(*RESULTS)
    for i in range(len(product_list)-1):
        assert 'Regular' in product_list[i].text
        assert len(product_list[i].find_element(*PRODUCT_NAME).text) > 0


