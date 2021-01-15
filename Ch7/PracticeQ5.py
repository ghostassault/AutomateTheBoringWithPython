import re
phoneRe = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo1 = phoneRe.search('My number is 415-555-4242')
print(mo1.group(0))
print(mo1.group(1))
print(mo1.group(2))