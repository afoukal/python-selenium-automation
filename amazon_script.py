from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path="C:/Users/Bogos/QA docs/python-selenium-automation/chromedriver" )
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')
driver.implicitly_wait(4)

input_field = driver.find_element(By.ID, 'twotabsearchtextbox')

input_field.clear()
input_field.send_keys('Dress')

search_icon = driver.find_element(By.XPATH, "//input[@value='Go']")
search_icon.click()
# wait for 4 sec
sleep(4)

# click search
text = driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text


# verify
assert text == '"Dress"', f'Incorrect text: {text}.'


driver.quit()
# driver.find_element(By.XPATH , "//*[@id='nav-orders']/span[2]").click()