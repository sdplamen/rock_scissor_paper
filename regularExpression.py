# import a Regex module
import re
# search for ape in a string
if re.search('ape', 'The ape was at the apex'):
    print('There is an ape')

# findall returns a list of matches
# . is used to match any character of the list
allApes = re.findall('ape', 'The ape was at the apex')
for i in allApes:
    print(i)

# finditer returns an iterator to get location
# you can use span to get location
theSTr = 'The ape was at the apex'
for i in re.finditer('ape', theSTr):
    # span retruns a tuple
    locTuple = i.span()
    print(locTuple)
# slice the match out using the tuple values    
    print(theSTr[locTuple[0]:locTuple[1]])

# square brackets match any one of teh characters between the brackets not including upper and lowercase varietes unless they are listed
animalStr = 'Cat rat mat fat pat'

# . is used to match any character of the list
allAnimals = ('[crmfp]at', animalStr)
for i in allAnimals:
    print(i)

# use ^ to denote any characters but whatever the character between the brackets
animalStr = 'Cat rat mat fat pat'
someAnimals = ('[^Cr]at', animalStr)
for i in someAnimals:
    print(i)

# replace all matches in a string
owlFood = 'rat cat mat pat'

# you can compile a regex into patern objects which provide additional methods
regex = re.compile('[cr]at')

#  sub() replace items mathes the regex in the stringwith first atribute string passed to sub
owlFood = re.sub('rat', 'owl', owlFood)
print(owlFood)

# Regex use backslash to to designate special characters and Python does the same inside string which causes issues
# let's try to get stuff out of the string

randStr = 'Here is \\stuff'
# this won't find it 
print('Find \\stuff : ', re.search('\\stuff', randStr))
# this does we have to put four slashes which is messy
print('Find \\\\stuff : ', re.search('\\\\stuff', randStr))
# you can around this by using raw strings which escapes the slashes
print('Find \\stuff : ', re.search(r'\\stuff', randStr))
# matching the periods. do the same [, ] and others
randStr = 'F.B.I. I.R.S. CIA'
print('Matches : ', len(re.findall('.\..\..', randStr)))
print('Matches : ', re.findall('.\..\..', randStr))

# match any whitespace characters
randStr = '''This is the long
string that goes on
for many lines'''
print(randStr)
       
# removes new lines
regex = re.compile('\n')
randStr = regex.sub(' ', randStr)
print(randStr)

# \n - new line
# \b - backspace
# \f - formfeeed
# \r = carrige return
# \t - tab
# \v - vertical tab
# \d - can be used instead of [0, 9]
randStr = '12345'
print('Matches ; ', len(re.findall('\d', randStr)))
# you can matche multiple digits by following the \d with {numOfValues}
if re.search('\d{5}', '12345'):
       print('It\'s a zip code')
# matching the single letter or character
# \w is the same as [a-zA-Z0-9_]
phNum = '421-555- 1212'
# check if is phone number
if re.search('\d{3}-\d{3}-\d{4}', phNum):
    print('It\'s a phone number')
# check for valide first name between 2 and 20 characters
if re.search('^[a-zA-Z]{2,20}$', 'Toshio Muramatsu'):
       print('It\'s a valid name')

# matching whitespaces
# \s is the same as [ \t\n\r\f\v]
# check for valid first and last name with spaces
if re.search('w\{2, 20}s\w\{2, 20}', 'Toshio Muramatsu'):
    print('It\'s a valid full name')

# matching one or more characters
print('Matches :', len(re.findall('a+', 'a as ape bug')))
print('Matches :', re.findall('a+', 'a as ape bug'))

# create a regex that matches email form a list of emails
# 1. 1 to 20 lowerc and uppercase letters, numbers, plus ._%+-
# 2. am @ symbolf
# 3. 1 to 20 lowerc and uppercase letters, numbers, plus -
# 4. a period
# 5. 2 to 3 lower and uppercase letters

emailList = 'oqibz@example.com tzirw@example.com @apple.com db@aol.com qpmzj@example.com'
print('Email matches : ', len(re.findall('[\w._%+-]{1, 20}@[\w.-]{2, 20}.[A-Za-z]{2, 3}', emailList)))
print('Email matches : ', re.findall('[\w._%+-]{1, 20}@[\w.-]{2, 20}.[A-Za-z]{2, 3}', emailList))
