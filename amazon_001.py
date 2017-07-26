from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Open Chrome Webdriver
driver = webdriver.Chrome('/usr/local/bin/chromedriver')
# Navigate to Amazon web app
driver.get('https://www.amazon.com')
time.sleep(5)
driver.close()