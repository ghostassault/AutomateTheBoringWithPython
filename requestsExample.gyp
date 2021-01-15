import requests
res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
type(res)
res.status_code == requests.codes.ok
len(res.text)
print(res.text[:250])

#Saving Downloaded Files to the Hard Drive
res.raise_for_status()
playfile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    playfile.write(chunk)
playfile.close()