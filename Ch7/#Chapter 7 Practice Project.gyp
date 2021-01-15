#Chapter 7 Practice Project
# Check Password Strength
# at least 8 characters long
# if password < 8
# contains upper and lowercase characters
# at least one digit
import re
a = re.compile(r'[A-Z]')
b = re.compile(r'[a-z]')
v = re.compile(r'\d')

def check_password(txt):
    return len(txt) >= 8 and bool(a.search(txt) and b.search(txt) and v.search(txt))

print(check_password('H'))
print(check_password('Hello1'))
print(check_password('hello'))
print(check_password('hellopassword'))
print(check_password('Hellopassword'))
print(check_password('HelloPassword123'))



#Project 2 Regex version of strip() method

#Write funcion that does the same thing as the strip 'strip()' string method

#no arguments are passed remove whitespace at the beginning and end of string

#character specified in second argument of function will be removed

def strip_regex(txt, st = None):
    if st == None:
        st_left = re.compile(r'^\s*')
        st_right = re.compile(r'\s*$')
    else:
        st_left = re.compile(r'^['+ re.escape(st) + r']*')
        st_right = re.compile(r'^['+ re.escape(st) + r']*$')
    txt = re.sub(st_left,"",txt)
    txt = re.sub(st_right,"",txt)
    return txt

q = '      .alphanumeric*425 123 '
print(strip_regex(q,' 123425'))
print(strip_regex(q,'numeric'))
print(strip_regex(q,'alpha'))
print(strip_regex(q,' '))
print(strip_regex(q))