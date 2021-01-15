import re
#The findall() metchod will return the strings of every match in the search string.

phoneNumReg = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')#has groups
print(phoneNumReg.findall('Cell: 415-555-9999 work: 212-555-0000'))


phoneNumReg = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')#has no groups
print(phoneNumReg.findall('Cell: 415-555-9999 work: 212-555-0000'))


#Character Classes
#You can define custom character class using square brackets
#Example [aeiouAEIOU] this character class will match any vowel, both lower and uppercase.
vowelRe = re.compile(r'[aeiouAEIOU]')
print(vowelRe.findall('Robocop eats baby food. BABY FOOD!'))

#Ranges of letters or numbers can be included by using hyphen.
#Example, the character class[a-zA-Z0-9] will match all lowercase letters, uppercase letters, and numbers.
#Inside square brackets, the normal regex symbols are not interpreted "as such". You do not need to escape the .*?() characters with a backslash
#Example, the character class[0-5.] will match digits 0-5 and a period


#Placing a caret character ^ after the character class opening bracket will make the preceding class negative.
# It will match all the character that are not in the character class.

consonantRe = re.compile(r'[^aeiouAEIOU]')
print(consonantRe.findall('Robocop eats baby food. BABY FOOD!'))


# The Caret and dollar sign characters
#The ^caret symbol can be used at the start of a regex to indicate that a match must occur at the beginning of t hte searched text.
#The $dollar sign at the end of the regex to indicate the string must end with this regex pattern.
#Both symbols can be used together to indicate that the entire string must match the regex

#Example, the r'^Hello' regex string matches strings that begin with 'Hello.
beginHello = re.compile(r'^Hello')
print(beginHello.search('Hello World!'))

#The r'\d$' regex string matches strings taht end with a numeric value from 0 to 9
endNum = re.compile(r'\d$')
print(endNum.findall('Your number is 42'))

#the r'^\d+$' regex string matches strings that both begin and end with one or more numeric characters
wholeStringisNum = re.compile(r'^\d+$')
print(wholeStringisNum.search('1234567890'))
print(wholeStringisNum.search('12345xyz67890') == None)
print(wholeStringisNum.search('12    34567890') == None)

#The last two print statements demonstrate how the entire string must match the regex if ^ and $ are used.
#Carrots cost dollars is a mnemonic used to remember caret comes first and the dollar comes last.


#The Wildcard Character
#The . dot character is the wildcard character in a regex. It will match any character except for a newline.
#The dot character will match just one character, which is why the match for the text flat in the below example matched only lat
atRe = re.compile(r'.at')
print(atRe.findall('The cat in the hat sat on the flat mat.'))

#Matching everything with Dot-Star
#Used when you want to match everything and anything
#Dot charcter means any single character except the newline and the Star character means zero or more of the preceding character.
#Dot Star greedymode will always match as much text as possible.
nameRe = re.compile(r'First name: (.*) Last Name: (.*)')
mo4 = nameRe.search('First name: Al Last Name: Sweigart')
print(mo4.group(1))
print(mo4.group(2))

# To match text in nongreedy mode, use the dot, star, and question mark (.*?)
# Similar to curly brackest, the question mark tells python to match in a nongreedy way
nonGreedyRe = re.compile(r'<.*?>')
mo = nonGreedyRe.search('<To serve man> for dinner.>')
print(mo.group())

greedyRe = re.compile(r'<.*>')
mo = greedyRe.search('<To serve man> for dinner.>')
print(mo.group())


#Matching Newlines with the Dot Character
#Dot-Star will match everything except a newline.
#By passing re.DOTALL as a second argument to re.compile(), the dot character can match all characters, including newline

noNewLineRe = re.compile('.*')
print(noNewLineRe.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())

newLineRe = re.compile('.*', re.DOTALL)
print(newLineRe.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())


#Review of Regex Symbols

""" The ? matches zero or one of the preceding group.
    The * matches zero or more of the preceding group
    the + matches one or more of the preceding group
    the {n} matches exactly n of the preceding group
    the {n,} matches n or more of the preceding group
    the {,m} matches 0 to m of the preceding group
    the {n,m} matches at least n and at most m of the preceding group.
    ^spam means the string must begin with spam.
    spam$ means the string must end with spam
    The . matches any character, except newline characters.
    \d, \w, and \s match a digit, word, or space character, resepctively
    \D, \W, and \S match anything except a digit, word, or space character
    [abc] matches any character between the brackets( such as a, b, or c)
    [^abc] matches any character that isnt between the brackets
"""

#Case-Insensitve Matching
#To make regex cas-insensitive, you can pass re.IGNORECASE or re.I as a second argument to re.compile()
robocop = re.compile(r'robocop',re.I) #re.I is the same as re.IGNORECASE
print(robocop.search('RoboCop is part man, part machine, all cop').group())
print(robocop.search('ROBOCOP is part man, part machine, all cop').group())
print(robocop.search('robocop is part man, part machine, all cop').group())


#Substitution Strings with the sub() method
"""
Regex can also substitute new text in place of those patterns. The sub() method for regex objects is passed two arguments.
The first argument is a string to replace any matches. The second is the string for the regular expression.
The sub() method returns a string with the substitions applied.
"""

namesRe = re.compile(r'Agent \w+')
print(namesRe.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))

#Part of the matched text can be used for substitution, by typing \1, \2, \3. "It means enter the text group of 1, 2, 3 in the substitution group"
#If you wanted to censor a name by showing just the first letters of their names, you can do this by using the regex "Agent(as argument)" (\w)\w* and pass r'\1****' as the first argument to sub()
agentRe = re.compile(r'Agent (\w)\w*') #Agent is the word we are matching, (\w) represents the first letter of the word after agent, \w* is matching all word/characters after the first character
print(agentRe.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve Knew Agent Bob was a double'))#the \1**** is stating that the characater A in Alice should not be censored.'l','i','c','e' should be substitued with *

#Managing complex regexes
"""Complex regular expressions can besimplified by "telling" re.compile() function to ignore whitespace and comments inside the regular expression string
This is called verbose mode, it can be enabeled by passing the variable re.VERBOSE as the second argument to re.compile()
"""
#instead of thiss
phoneRe = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')

phoneRe = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              #area code
    (\s|-|\.)?                      #seperator
    \d{3}                           #first 3 digits
    (\s|-|\.)                       #seperator
    \d{4}                           # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?    # extenstions
)''', re.VERBOSE)

# triple quotes allows the spread of the regex definition over multiple lines, making it easier to read


#Combining re.IGNORECASE, re.DOTALL, and re.VERBOSE
#re.compile only takes a single value as its second argument. In order to combine re.IGNORECASE, re.DOTALL, and re.VERBOSE the pipe character must be used, otherwise known as the bitwise or operator

someRegex = re.compile('foo', re.IGNORECASE | re.DOTALL)

someRegex = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
