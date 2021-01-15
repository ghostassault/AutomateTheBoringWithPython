#xkcdcomics.gyp
#Here's what the program does
""" 
Loads the XKCD home page.
Saves the comic image on that page
Follows the Previous Comic Link
Repeats untio it reaches the first comic
"""
#This means the code will need to do the following
"""
Download pages with the request module.
Find the URL of the comic image for a page using Beautiful Soup
Download and save the comic image to the hdd with iter_content()
Find the URL of the Previos Comic link, and repeat
"""

import requests, os, bs4
url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)
while not url.endswith('#'):
    #TODO: Download the page.
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)
    #TODO: Find the url of the comic image
    comicElem = soup.select('#comic image')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicURL = comicElem[0].get('src')

        #TODO: Download the image
        print('Downloading image %s...' % (comicURL))
        res = requests.get(comicURL)
        res.raise_for_status()
        #TODO: Save the image to ./xkcd
        imageFile = open(os.path.join('xkcd', os.path.basename(comicURL)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    #TODO: Get the Prev button's url
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')

print('Done')