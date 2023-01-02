txt = 'I have {an:.2f} Ruppes!'
print(txt.format(an = 4))

# #### Using a Single Formatter
# using format option in a simple string
print('{}, A computer science portal for geeks.'.format('GeeksforGeeks'))

# using format option for a value stored in a variable
str = 'This article is written in {}'
print(str.format('Python'))

# formatting a string using a numeric constant
print('Hello, I am {} years old !'.format(18))

# #### Using with multiple placeholders
# Multiple placeholders in format() function
my_string = '{}, is a {} science portal for {}'
print(my_string.format('GeeksforGeeks', 'computer', 'geeks'))
# different datatypes can be used in formatting
print('Hi ! My name is {} and I am {} years old'.format('User', 19))
# The values passed as parameters are replaced in order of their entry
print('This is {} {} {} {}'.format('one', 'two', 'three', 'four'))

# #### Using IndexError
# parameters in format function.
my_string = '{}, is a {} {} science portal for {}'

print(my_string.format('GeeksforGeeks', 'computer', 'geeks'))

# #### Using Escape Sequences
#\n Breaks the string into a new line
print('I designed this rhyme to explain in due time\nAll I know')
# \t Adds a horizontal tab
print('Time is a \tvaluable thing')
# \\ Prints a backslash
print('Watch it fly by\\as the pendulum swings')
# \' Prints a single quote
print('It doesn\'t even matter how hard you try')
# \" Prints a double quote
print('It is so\"unreal\"')
# \a makes a sound like a bell
print('\a')

# #### Using Positional and Keyword Arguments
# Positional arguments are placed in order
print('{0} love {1}!!'.format('GeeksforGeeks', 'Geeks'))
# Reverse the index numbers with the parameters of the placeholders
print('{1} love {0}!!'.format('GeeksforGeeks', 'Geeks'))
print('Every {} should know the use of {} {} programming and {}'.format('programmer', 'Open', 'Source', 'Operating Systems'))
# Use the index numbers of the values to change the order that they appear in the string
print('Every {3} should know the use of {2} {1} programming and {0}'.format('programmer', 'Open', 'Source', 'Operating Systems'))

# #### Keyword arguments are called by their keyword name
print('{gfg} is a {0} science portal for {1}'.format('computer', 'geeks', gfg='GeeksforGeeks'))

# #### Using Type Specifying
# Using %s – string conversion via str() prior to formatting
# Use the format code syntax {field_name: conversion},
# where field_name specifies the index number of the argument to the str.format() method,
# and conversion refers to the conversion code of the data type.
print('%20s' % ('geeksforgeeks', ))
print('%-20s' % ('Interngeeks', ))
print('%.5s' % ('Interngeeks', ))

# #### Using %c– character  prior to formatting
type = 'bug'
result = 'troubling'
print('I wondered why the program was %s me. Then it dawned on me it was a %s.' % (result, type))
# Using %i signed decimal integer and %d signed decimal integer(base-10) prior to formatting
match = 12000
site = 'amazon'
print('%s is so useful. I tried to look up mobile and they had a nice one that cost %d rupees.' % (site, match))

# #### Convert base-10 decimal integers to floating-point numeric constants
print('This site is {0:f}% securely {1}!!'.format(100, 'encrypted'))
# To limit the precision
print('My average of this {0} was {1:.2f}%'.format('semester', 78.234876))
# For no decimal places
print('My average of this {0} was {1:.0f}%'.format('semester', 78.234876))
# Convert an integer to its binary or with other different converted bases.
print('The {0} of 100 is {1:b}'.format('binary', 100))
print('The {0} of 100 is {1:o}'.format('octal', 100))

# #### Type Specifying Errors
# When explicitly converted floating-point values to decimal with base-10 by 'd' type conversion we encounter Value-Error.
print('The temperature today is {0:d} degrees outside !'.format(35.567))
# Instead write this to avoid value-errors
''' print('The temperature today is {0:.0f} degrees outside !'.format(35.567))'''

# #### Padding Substitutions or Generating Spaces
# To demonstrate spacing when strings are passed as parameters
print('{0:4}, is the computer science portal for {1:8}!'.format("GeeksforGeeks", "geeks"))
# To demonstrate spacing when numeric constants are passed as parameters.
print('It is {0:5} degrees outside !'.format(40))
# To demonstrate both string and numeric constants passed as parameters
print('{0:4} was founded in {1:16}!'.format('GeeksforGeeks', 2009))
# To demonstrate aligning of spaces
print('{0:^16} was founded in {1:<4}!'.format("GeeksforGeeks", 2009))
print('{:*^20s}'.format('Geeks'))

# #### Applications
# which prints out i, i ^ 2, i ^ 3, i ^ 4 in the given range

# Function prints out values in an unorganized manner
def unorganized(a, b):
    for i in range(a, b):
        print(i, i**2, i**3, i**4)
# Function prints the organized set of values
def organized(a, b):
    for i in range(a, b):
        # Using formatters to give 6 spaces to each set of values
        print('{:6d} {:6d} {:6d} {:6d}'.format(i, i ** 2, i ** 3, i ** 4))

# Driver Code
n1 = int(input('Enter lower range :-\n'))
n2 = int(input('Enter upper range :-\n'))
print('------Before Using Formatters-------')
# Calling function without formatters
unorganized(n1, n2)
print()
print('-------After Using Formatters---------')
print()
# Calling function that contains formatters to organize the data
organized(n1, n2)

# #### Using a dictionary for string formatting
introduction = 'My name is {first_name} {middle_name} {last_name} AKA the {aka}.'
full_name = {'first_name': 'Tony','middle_name': 'Howard','last_name': 'Stark','aka': 'Iron Man',}
# Notice the use of "**" operator to unpack the values.
print(introduction.format(**full_name))

# #### Using list
# Python code to truncate float values to 2 decimal digits.
# List initialization
Input = [100.7689454, 17.232999, 60.98867, 300.83748789]
# Using format
Output = ['{:.2f}'.format(elem) for elem in Input]
# Print output
print(Output)
