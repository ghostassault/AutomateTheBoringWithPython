'''write a program that will open the game at 
https://gabrielecirulli.github.io/2048/ and keep sending up, right, down, and left keystrokes to
automatically play the game.'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def main():
    url = 'https://gabrielecirulli.github.io/2048/'
    browser = webdriver.Safari()
    browser.set_window_position(0,0)
    browser.set_window_size(1600,900)   
    browser.get(url)
    time.sleep(3)
    
    a = browser.find_element_by_tag_name('html')
    while True:
        a.send_keys(Keys.UP)
        a.send_keys(Keys.RIGHT)
        a.send_keys(Keys.DOWN)
        a.send_keys(Keys.LEFT)


    print("Game over")


main()