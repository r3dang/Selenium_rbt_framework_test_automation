from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import selenium.common.exceptions

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

''' Function Definitions '''


# Opens Selenium Webdriver and opens url given
def selenium_init(url):
    web_driver = webdriver.Chrome('/usr/local/bin/chromedriver')
    web_driver.get(url)
    time.sleep(5)
    return web_driver


# Closes webdriver
def selenium_tear_down(web_driver):
    web_driver.close()


# Funtion that searches for elements in a search bar.
def search_query(web_element, search_text):
    web_element.clear()
    web_element.send_keys(search_text)
    web_element.send_keys(Keys.RETURN)


def print_order_text(order_name, order_number):
    print(order_name + '\n')
    order_number += 1
    print("This is order " + str(order_number) + " on the page")


def check_for_text_on_page(order_string, contain_string):
    assert order_string.__contains__(contain_string)

''' End of function definitions'''

''' Begin Execution'''
driver = selenium_init('https://www.amazon.com/')
# Run a query for iPhone 7 in amazon search bar
search_bar = driver.find_element_by_id('twotabsearchtextbox')
search_query(search_bar, "iPhone 7")

query_index = 0
try:
    element = driver.find_element_by_id('result_' + str(query_index))
except selenium.common.exceptions.NoSuchElementException:
    print("No elements exist on page")

while element:
    try:
        element = driver.find_element_by_id('result_' + str(query_index))
        check_for_text_on_page(str(element.text), "iPhone 7")
        query_index += 1
    except selenium.common.exceptions.NoSuchElementException:
        print("Could not find element " + str(query_index))
        break
    except AssertionError:
        print_order_text(str(element.text), query_index)
        break

selenium_tear_down(driver)
''' End Execution '''
