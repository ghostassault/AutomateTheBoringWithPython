# Write a program that goes to a photo-sharing site like Flickr or Imgur, 
# searches for a category of photos, and then downloads all the resulting images. 
# You could write a program that works with any photo site that has a search feature.

'''
This Programs opens a browser-tabs and automatically searches the most popular Photo-sharing 
sites for the entered search terms.
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, os, requests, bs4, re 

searchTerm = input('Input a search Term: \n')

# https://imgur.com/search?q=farm
# https://www.flickr.com/search/?text=farm
# https://www.pixiv.net/en/tags/


browser = webdriver.Safari()
browser.set_window_position(0,0)
browser.set_window_size(1600,900)


time.sleep(3)

#pixiv = browser.get('https://www.pixiv.net/en/tags/'+ searchTerm)
#time.sleep(3)

#deviant = browser.get('https://www.deviantart.com/search?q='+ searchTerm)




#TODO: WORK on flickr image downloader
def flickrImageDl():
    print("openng website")
    browser.get('https://www.flickr.com/search/?text=' + searchTerm) 
    time.sleep(2)
    #TODO: Create scrolling effect on the webpage
    
    dirName = 'flickr_'+ searchTerm
    os.makedirs(dirName, exist_ok=True)#creates a directory with the search term as the name
    
    url = requests.get('https://www.flickr.com/search/?text='+ searchTerm)
    url.raise_for_status
    soup = bs4.BeautifulSoup(url.text , 'html.parser') #parses the source code of the search webpage
    divElement = soup.findAll("div", {"class": "view photo-list-photo-view requiredToShowOnServer awake"}) #finds the class that contains the url to the photos being downloaded
    a = divElement
    #print(a)
    pattern = re.findall(r'url\(([^)]+)\)', str(a)) #The regular expression to extract the url of the image
    for i in pattern:
        imgURL = 'https:' + i #concatenates https on to the extracted url
        imgName = i[30:] #strips a portion of the url to use as a name for the dowloaded images.
        #print(imgURL)
        res = requests.get(imgURL)
        res.raise_for_status
        imageFile = open(os.path.join(dirName, os.path.basename(imgName)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
        
    print('Done downloading images from flickr')
    
   
    
#after above function is done change dir back to parent folder


#TODO: Done
def imgurImageDL():
    browser.get('https://imgur.com/search?q='+ searchTerm)
    #Add a scrolling function to the browser.get to scroll the page while downloading
    time.sleep(2)

    url = requests.get('https://imgur.com/search?q='+ searchTerm)
    url.raise_for_status
    soup = bs4.BeautifulSoup(url.text , 'html.parser')
    imgs = soup.findAll('img')

    directory_name = 'imgur_'+ searchTerm
    os.makedirs(directory_name, exist_ok=True)
    
    
    
    
    for i in imgs:
        image_url = i.get('src')
        res = requests.get('https:'+image_url)
        res.raise_for_status
        imageFile = open(os.path.join(directory_name, os.path.basename(image_url)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
            
    
    print('Done downloading images from imgur')
    os.chdir('..')


#TODO: Create a function for DeviantArt
#TODO: Create a function For Pixiv
imgurImageDL()
flickrImageDl()


