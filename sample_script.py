from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:/Users/Bogos/QA docs/python-selenium-automation/chromedriver" )
driver.maximize_window()
#driver.implicitly_wait(4)
# open the url
driver.get('https://www.google.com/')

search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('Dress')

# wait for 4 sec
#sleep(4)
driver.wait = WebDriverWait(driver, 10)
driver.wait.until(EC.element_to_be_clickable((By.NAME, 'btnK'))).click()


# click search


# verify
assert 'Dress' in driver.find_element(By.XPATH, "//div[contains(@class,'commercial-unit-desktop-top')]").text
assert 'Dress' in driver.find_element(By.XPATH, "//div[@class='g']").text

driver.quit()
