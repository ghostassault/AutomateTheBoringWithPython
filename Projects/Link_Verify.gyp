'''Given a Url of a web page, will attempt to download every linked page on the page.
The program should flag any pages that have a 404 "Not Found" Status code and print them 
out as broken links.'''

import sys, webbrowser, requests, bs4

def verify():
    url = input('Enter a Url that you would like to verify the links for:\n')

    res = requests.get(url)
    res.raise_for_status

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    linkElems = soup.select("a")
    badlinks = [] 

    for i in linkElems:
        try:
            a_url = i['href']
            if a_url.startswith('http'):
                to_check = a_url
                print(to_check)
            elif a_url.startswith('//'):
                to_check = 'https:' + a_url
                print(to_check)
            elif a_url.startswith('#'):
                to_check = url + a_url
                print(to_check)
            result = requests.get(to_check)

            if result.status_code == 404:
                badlinks.append(to_check)
        except:
            pass

    print(badlinks)

verify()
