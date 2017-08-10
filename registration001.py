from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import selenium.common.exceptions
import os

'''
    Test Serial# : 1
    Test Name: registration001
    Steps:
        - Open Selenium Demo Website
        - Enter details in each element
        - Quit Driver
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


# Function Writes text to element
def enter_in_field(web_driver, element_id, box_text):
    web_element = web_driver.find_element_by_id(element_id)
    web_element.clear()
    web_element.send_keys(box_text)


# Chooses an option in the radio driver
def choose_radio_option(web_driver, path):
    web_driver.find_element_by_xpath(path).click()


def find_option_in_dropdown(drop_down, option):
    driver.find_element_by_xpath("//select[@name='" + drop_down + "']/option[text()='" + option + "']").click()
''' End of function definitions '''

''' Begin Execution '''

driver = selenium_init('http://demoqa.com/registration/')
# find the name field on webpage
enter_in_field(driver, 'name_3_firstname', 'Rajit')
enter_in_field(driver, 'name_3_lastname', 'Dang')


choose_radio_option(driver, "//input[@value='single']")
choose_radio_option(driver, "//input[@value='reading']")

find_option_in_dropdown('dropdown_7', 'United States')
find_option_in_dropdown('date_8[date][mm]', '5')
find_option_in_dropdown('date_8[date][dd]', '17')
find_option_in_dropdown('date_8[date][yy]', '1997')

enter_in_field(driver, 'phone_9', '8589008424')
enter_in_field(driver, 'username', 'test_user123')
enter_in_field(driver, 'email_1', 'test_user@gmail.com')

driver.find_element_by_id("profile_pic_10").send_keys(os.getcwd()+"/Event iOS DB Schema.png")

enter_in_field(driver, 'description', 'I am awesome')
enter_in_field(driver, 'password_2', 'abc12345')
enter_in_field(driver, 'confirm_password_password_2', 'abc12345')

driver.find_element_by_name('pie_submit').click()
time.sleep(20)
selenium_tear_down(driver)

''' End Execution '''




