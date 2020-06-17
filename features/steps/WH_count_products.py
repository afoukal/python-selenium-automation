from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

from behave import given, when
from selenium.webdriver.common.by import By

PRODUCTS = (By.CSS_SELECTOR, "a.menu__link.menu--main__link[href*='products']")
FIND_STORE = (By.CSS_SELECTOR, ".Input-InputField--KUzM1")
#FIND_STORE2 = (By.CLASS_NAME, "StoreSelector-Option--mQyct")
#FIND_STORE2 = (By.CSS_SELECTOR, "StoreSelector-Option--mQyct")
FIND_STORE2= (By.XPATH, "//div[@class='StoreSelector-Option--mQyct']")

@given('Open Whole Foods page')
def open_wh_page(context):
    context.driver.get("https://www.wholefoodsmarket.com/")


@when("Click on Browse Products")
def click_browse_products(context):
    context.driver.find_element(*PRODUCTS).click()
    sleep(2)


@when("Choose the store")
def choose_store(context):
    context.driver.find_element(*FIND_STORE).send_keys("75019")
    context.driver.find_element(*FIND_STORE2).click()
    sleep(10)
