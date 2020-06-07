from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:/Users/Bogos/QA docs/python-selenium-automation/chromedriver" )
driver.maximize_window()

driver.get('https://www.amazon.com/')
driver.implicitly_wait(4)

input_field = driver.find_element(By.ID, 'twotabsearchtextbox')

input_field.clear()
input_field.send_keys('saucony womens shoes')

search_icon = driver.find_element(By.XPATH, "//input[@value='Go']")
search_icon.click()
sleep(4)

driver.find_element(By.CSS_SELECTOR, "a[href*='B07KK58WGX']").click()
sleep(1)


driver.find_element(By.CSS_SELECTOR, ".a-dropdown-prompt").click()
driver.find_element(By.ID, "native_dropdown_selected_size_name_6").click()
sleep(2)
driver.find_element(By.ID, "add-to-cart-button").click()
driver.find_element(By.ID, "nav-cart").click()
print(driver.find_element(By.ID, "sc-subtotal-label-activecart").text)
print(driver.find_element(By.CSS_SELECTOR, ".sc-product-title").text)