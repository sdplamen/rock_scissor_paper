# importing the string module
import string
def punct(text):
    for el in text:
        if el in string.punctuation:
            # printing the punctuation
            print('Your punctuaion here :', el, end = ' ')
text = input('Type a punctuated pharse : ')
punct(text)
