from behave import given, then
from selenium.webdriver.common.by import By

LINKS= (By.CSS_SELECTOR, "#zg_tabs li")
HEADER = (By.ID, "zg_banner_text_wrapper")

@given("Open Amazon Best Sellers page")
def open_best_sellers(context):
    context.driver.get("https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers")


@then("Check that {links} links are present")
def link_quantity(context, links):
    bs_links = context.driver.find_elements(*LINKS)
    assert len(bs_links) == int(links), f'{links} links should be displayed on Amazon Best Seller Header, but instead {len(bs_links)} are displayed'


@then('Click on each link and validate the header')
def click_link_check_header(context):
    bs_links = context.driver.find_elements(*LINKS)
    for i in range(len(bs_links)):
        bs_links = context.driver.find_elements(*LINKS)
        title = bs_links[i].text
        bs_links[i].click()
        assert title in context.driver.find_element(*HEADER).text
