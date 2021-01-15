#lucky.py
#Project: I'm Feeling Lucky" Google Search
""" 
This what the the program does:
    gets search keywords from the command line arguments.
    retrieves the search results page
    opens a browser tab for each result
The program will need to doe the following:
    Read the command line arguments from sys.argv.
    Fetch the search result page with the request module
    Find the links to each search result
    Call the webbrowser.open() function to open the web browser
"""

#Get the command line arguments and Request the search page

import requests, sys, webbrowser, bs4

print('Googling...') # display text while downloading the Google page
res = requests.get('htt[://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

#TODO: Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text)
#TODO: Open a browser tab for each result.
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href '))