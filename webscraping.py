#import statements
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

#list of randomised responses
responses = ["Everything at the store was great! definately coming back"]

#setting up the driver
driver = webdriver.Chrome()
driver.get("https://www.kroger.com/hc/help/contact-us/customer-comments")
sleep(2)

#getting the buttons and such as variables
button = driver.find_element_by_xpath("//input[@value='optOut']")
topic = driver.find_element_by_xpath("//option[@value='Store']")
text = driver.find_element_by_xpath("//textarea[@name='comments']")
submit = driver.find_element_by_xpath("//button[@data-qa='cc-submit-button']")

#repeatedly send the messages
while True:
    driver.get("https://www.kroger.com/hc/help/contact-us/customer-comments")
    sleep(2)
    button.click()
    sleep(2)
    topic.click()
    sleep(2)
    zipc = driver.find_element_by_xpath("//*[@id='content']/div/div/section/section/div/form/div[3]/div[2]/div/input")
    zipc.click()
    zipc.send_keys("48168")
    zipc.send_keys(Keys.RETURN)
    sleep(2)
    text.send_keys(responses[random.randint(0,(len(responses))-1)])
    sleep(10)
    submit.click()

driver.quit()
