import os
import time 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

# Change the info here
messenger_link = "https://www.messenger.com/t/abc"
email = ""
password = ""
message = ""

os.environ["SELENIUM_SERVER_JAR"] = "selenium-server-standalone-2.41.0.jar"
browser = webdriver.Chrome("/Users/nvravicharan/Desktop/chromedriver")
# makes the browser wait if it can't find an element
browser.implicitly_wait(10)

browser.get(messenger_link)

time.sleep(2)

e_input = browser.find_element_by_xpath("//input[@id='email']")
p_input = browser.find_element_by_xpath("//input[@id='pass']")
e_input.send_keys(email)
p_input.send_keys(password)

submit = browser.find_element_by_xpath("//button[@id='loginbutton']")
submit.submit()
text_field = browser.find_element_by_xpath("//div[@aria-label='Type a message...']")
text_field.send_keys(message)
browser.find_element_by_xpath("//a[@aria-label='Send']").click()
time.sleep(5)

browser.quit()