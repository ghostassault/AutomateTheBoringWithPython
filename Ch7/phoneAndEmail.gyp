""" Phone num project
- Get text off the clipboard
- Find all phone numbers and email addresses in the text
- paste them onto the clipboard
"""

# The code will need to do the following
"""
Use the pyperclip module to copy and paste all the things
create two regexes,
    one for matching the phone numbers
    one for mathcing the email addresses
find all matches for both regexs
Format all matched strings into a single string to pase
Display a message if no matches were found in the text
"""
import pyperclip, re

phoneregex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              #area code
    (\s|-|\.)?                      #seperator
    (\d{3})                           #first 3 digits
    (\s|-|\.)                       #seperator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extenstions
)''', re.VERBOSE)


# TODO: Create email regex
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+   # username
    @                   # at something
    [a-zA-Z0-9.-]+      # domain name
    (\.[a-zA_Z]{2,4})   # dot-somethine
    )''', re.VERBOSE)

# TODO: Find matches in clipboard text.
# phoneAndEmail.py - Finds phone numbers and email addressess on the clipboard

#Find matches in clipboard text
text = str(pyperclip.paste())
matches = []
for groups in phoneregex.findall(text):
    print(groups)
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
        matches.append(phoneNum)
        print(groups)
for groups in emailRegex.findall(text):
    matches.append(groups[0])
# TODO: Copy results to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addressess found.')