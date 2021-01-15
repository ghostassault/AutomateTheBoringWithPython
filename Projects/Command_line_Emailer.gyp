#Command line Emailer
""" Takes an email address and string of text on the command line and logs into an email account and sends an email of the content provided to the provided address"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys, time, os
email = "etest3109@gmail.com"
password = 'EmailTest2507359'
recip = input("enter a recipient email address:\n")
text = input("Enter a message: \n\n")
def sendEmail():
    #The 2 commented lines of code below allow a message to be typed directly into the terminal without an input() method but have been omitted because of the excess text that outputs to the email client.
    #ToEmail = sys.argv[0]
    #text = " ".join(sys.argv[2:])
    
    browser = webdriver.Safari()
    browser.set_window_position(0,0)
    browser.set_window_size(1600,900)
    browser.get("https://accounts.google.com/ServiceLogin/identifier?passive=1209600&continue=https%3A%2F%2Faccounts.google.com%2F&followup=https%3A%2F%2Faccounts.google.com%2F&flowName=GlifWebSignIn&flowEntry=AddSession")
    
    time.sleep(3)
    emailElem = browser.find_element_by_xpath('//*[@id="identifierId"]')
    emailElem.send_keys('etest3109@gmail.com')
    emailElem.send_keys(Keys.RETURN)
    
    
    time.sleep(3)
    passwordElem = browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
    passwordElem.send_keys(password)
    passwordElem.send_keys(Keys.RETURN)
    
    #clicks the google apps menu
    
    time.sleep(3)
    a = browser.find_element_by_xpath('//*[@id="gbwa"]/div/a')
    a.send_keys(Keys.RETURN)
    time.sleep(3)
    browser.get('https://mail.google.com/mail')
    time.sleep(3)
    browser.get('https://mail.google.com/mail/u/0/#inbox?compose=new')
    time.sleep(3)
    browser.find_element_by_css_selector('#\:8k > div').send_keys(recip)
    time.sleep(3)
    browser.find_element_by_css_selector('#\:8f').send_keys('This is from Terminal')
    time.sleep(3)
    browser.find_element_by_css_selector('#\:9k').send_keys(text)
    time.sleep(3)
    browser.find_element_by_css_selector('#\:85').click()
    input("Press enter to quit")
    
sendEmail()