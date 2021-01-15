#The search() method will return a match object of the first matched text in a searched string

#1 Matching Multiple groups with the pipe
import re
heroR = re.compile(r'Batman|Tina Fey')
mo1 = heroR.search('Batman and Tina Fey.')
print(mo1.group())


#2 Optional Matching with the Question Mark
batRe = re.compile(r'Bat(wo)?man')
mo1 = batRe.search('The adventures of Batman')
print(mo1.group())

# The (wo)? part of the regular expression means the pattern wo is an optional group
batRe = re.compile(r'Bat(wo)?man')
# The regex will match text that has "zero" ie one instance of wo in it.
mo1 = batRe.search('The adventures of Batwoman, and Batman')
print(mo1.group())

# Using Regex to look for phone numbers that do or do not have an area code
phoneRe = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRe.search('My number is 415-555-4242')
print(mo1.group())
#Match 0 or 1 of the group preceding this question mark. Questions (?) marks can be escaped with \?
mo2 = phoneRe.search('My number is 412-4565')
print(mo2.group())


#3 Matching zero or more with the Star. * means to match zero or more
batRe = re.compile(r'Bat(wo)*man')
mo1 = batRe.search('The adventures of Batman Batgirl')
print(mo1.group())

batRe = re.compile(r'Bat(wo)*man')
mo4 = batRe.search('The adventures of Batwowowowowowowoman')
print(mo4.group())


#4 Matching one or more with the plus
batRe = re.compile(r'Bat(wo)+man')
mo1 = batRe.search('The adventures of Batwowowoman')
print(mo1.group())

# The group preceding the plus must appear at least once
batRe = re.compile(r'Bat(wo)+man')
mo2 = batRe.search('The adventures of Batman')
print(mo2 == None )

# Matching specific repetitions with Curly Brackets
#If you have a group that you want to repeat a specific number of times, follow the group in your regex wit h number in curly brackets.

haRe = re.compile(r'(Ha){3}')
mo1 = haRe.search('HaHaHa')
print(mo1.group())
#Here, (Ha){3} matchers 'HaHaHa' but not 'Ha'. Since it doesnt match 'Ha 3', serach() returns None
mo2 = haRe.search('Ha')
mo2 == None
print(mo2)

#Greedy and Nongreedy matching
greedyHaRe = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRe.search('HaHaHaHaHa')
print(mo1.group())

nonegreedyHaRe = re.compile(r'(Ha){3,5}?')
mo2 = nonegreedyHaRe.search('HaHaHaHaHa')
print(mo2.group())
