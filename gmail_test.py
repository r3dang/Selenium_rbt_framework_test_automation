from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Open Chrome Webdriver
driver = webdriver.Chrome('/usr/local/bin/chromedriver')
# Navigate to gmail web app
driver.get('https://www.gmail.com')
time.sleep(5)
# store instance of username bar
username_bar = driver.find_element_by_name('t')

username_bar.clear()
# send info
username_bar.send_keys("r3dang@ucsd.edu")
username_bar.send_keys(Keys.RETURN)
password_bar = driver.find_element_by_name('q')
password_bar.clear()
password_bar.send_keys('abcsdefg')
username_bar.send_keys(Keys.RETURN)
assert "Inbox" not in driver.page_source
driver.close()



