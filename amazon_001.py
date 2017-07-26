from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
'''
    Test Serial# : 1
    Test Name: amazon_001
    Steps:
        - Open Amazon Browser
        - Search for iPhone 7
        - Check whether every query result contains the substring 'iPhone 7'
        - If at any point, a result does not contain 'iPhone 7 in its
            text, then the test fails.
'''


# Open Chrome Webdriver
driver = webdriver.Chrome('/usr/local/bin/chromedriver')
# Navigate to Amazon web app and wait for 10 seconds
driver.get('https://www.amazon.com')
time.sleep(10)
# Run a query for iPhone 7 in amazon search bar
search_bar = driver.find_element_by_id('twotabsearchtextbox')
search_bar.clear()
# Enter query in search box
search_bar.send_keys("iPhone 7")
search_bar.send_keys(Keys.RETURN)
# Create a list to store query results
search_results = []
query_index = 0
element = driver.find_element_by_id('result_' + str(query_index))
while element:
    # I have a reference to result_0. But how do I get access to the sub web
    # element that contains the title?
    ''' I do know how to check if the string contains the 'iPhone 7
        My problem is that I cannot reach that string with xpath
    '''
    query_index += 1
driver.close()