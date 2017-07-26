from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Open Chrome Webdriver
driver = webdriver.Chrome('/usr/local/bin/chromedriver')
# Navigate to gmail web app
driver.get('https://www.gmail.com')
time.sleep(5)
# store instance of username bar
username_bar = driver.find_element_by_id('identifierId')

# Clear information
username_bar.clear()
# send info
username_bar.send_keys("r3dang@ucsd.edu")
username_bar.send_keys(Keys.RETURN)
time.sleep(5)
password_bar = driver.find_element_by_xpath('//input[@type="password"]')
password_bar.clear()
driver.find_element_by_xpath('//div[text()='Wrong password. Try again.']')
driver.close()