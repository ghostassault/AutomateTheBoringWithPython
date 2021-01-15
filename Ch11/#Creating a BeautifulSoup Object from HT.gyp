#Creating a BeautifulSoup Object from HTML
import requests, base64
res = requests.get('http://nostarch.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text)
type(noStarchSoup)

#This code uses requests.gey() to download the main page from the No Starch Press website and then passes the text attribute of the response to bs4.BeautifulSoup

#A HTML file can be loaded from your Hard Drive by passing a file object to bs4.BeautifulSoup()
exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile)
type(exampleSoup)

"""
Examples of CSS selectors

soup.select('div')                      All elements named <div>
soup.select('#author')                  The element with an id attribute of author
soup.select('.notice')                  All elements that use a CSS class attribute named notice
soup.select('div span')                 All elements named <span> that are within an element named <div>
soup.select('div > span')               All elements named <span> that are directly within an element named <div>, with no other element in between
soup.select('input[name]')              All elements named <input> that have a named attribute with any value
soup.select('input[type="button]')      All elements named <input> that have an attribute named type with value button
