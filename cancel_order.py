from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:/Users/Bogos/QA docs/python-selenium-automation/chromedriver")
driver.maximize_window()

driver.get('https://www.amazon.com/gp/help/customer/display.html ')
search_box = driver.find_element(By.ID,'helpsearch')
search_box.send_keys("Cancel order")

search_button = driver.find_element(By.XPATH, "//input[@type='submit' and @class='a-button-input']")
search_button.click()

result = driver.find_element(By.XPATH, "//p[@class='a-color-secondary']/b")
text_result = result.text

assert text_result == 'Cancel order', f'Incorrect text {text_result}'

driver.quit()

# driver.get('https://www.amazon.com/ap/signin?_encoding=UTF8&accountStatusPolicy=P1&openid.assoc_handle=usflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fcss%2Forder-history%3Fie%3DUTF8%26ref_%3Dnav_orders_first&pageId=webcs-yourorder&showRmrMe=1')
# sign_in_text = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
# print(driver.title)
