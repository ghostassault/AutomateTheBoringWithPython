
# What the program does

#DOES: Get a street address from the command line arguments or clipboard.

#Does: Opens the web browser to the Google Maps page for the address.

#TODO: Read the command line arguments from sys.argv.
#TODO: Read the clipboard contents.
#TODO: Call webbrowser.open() function to open the web browser

#Step 1: Figure out the URL

#set to open a browser to 'https://www.google.com/maps/place/your_address_string'

#Step 2: Handle the command line arguments

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    #Get address from command line.
    address = ' '.join(sys.argv[:1])
else:
    #Get address from clipboard
    address = pyperclip.paste()
webbrowser.open('https://www.google.com/maps/place/' + address)
https://www.google.com/maps/place/870+Valencia+St,+San+Francisco,+CA+94110