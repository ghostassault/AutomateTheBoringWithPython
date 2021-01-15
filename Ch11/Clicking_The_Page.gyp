from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://inventwithpython.com')
linkElem = browser.find_element_by_link_text('Read It Online')
type(linkElem)
linkElem.click()

""" This opens a web browser to http://inventwithpython.com/, 
gets the webElement object for the <a> element with the text Read It online, 
and then simulates clicking that <a> element."""

#Filling Out and Submitting Forms
 
