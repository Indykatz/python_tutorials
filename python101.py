# PYTHON 101 - Kat

# Covers: printing in the terminal; data types; using methods on a string ("A string looks like this") 
# Dont worry if some of the code confuses you at first as you continue they will make sense. 
# The # at the start means these are comments and not part of the code
# The \n is a styling function 
# Build in functions (methods) end in brackets and what is in the bracket is called the parameter 
# Here I am using the functions print() and input() function

print("\nHi Welcome to my python tutorial 101.\n")
input("Press Enter to continue ... \n")

# print() Prints in Terminnal
# The print function prints the text in the terminal.
# A sentence known as a string is also help in quotaions "". A string is a word or set of words
print("A print statement, prints in the terminal")

# input() requires the user to press enter you will learn more about this as we continue 
input("\nPress Enter to continue ... \n")

# DATA TYPES - data types are the types of data used we know them as words and numbers but computers don't
print("DATA TYPES\n")

input("Press Enter to continue ... \n")

# Using the method print() and type() the computer can tell us what data type it is storing

# string or str is a word or sentence
print("I AM A STRING\n")
print(type("I AM A STRING")) 

input("\nPress Enter to continue ... \n")

# integer or int - a whole number 
print(100)
print(type(100)) 

input("\nPress Enter to continue ... \n")

# float, a decmimal point number
print(1.00)
print(type(1.00)) 


input("\nPress Enter to continue ... \n")

# None, a none type 
print(None)
print(type(None))

input("\nPress Enter to continue ... \n")

# Boolen or bool, a True or False
print(True)
print(type(True)) 

input("\nPress Enter to continue ... \n")
 

# METHODS - methods are build into python to help 
print("METHODS\n")

input("Press Enter to continue ... \n")


# the method len() will return the length of what is in the brackets

# EXAMPLE
print("The length of this string is")
print(len("The length of this string is"))

input("\nPress Enter to continue ... \n")

# index - PYTHON STARTS FROM INDEX[0] (not index[1])
# as you learn more you will see why but 0 is also the first index
print("The first character indexed is")
print("The first character indexed is"[0])

input("\nPress Enter to continue ... \n")

print("The last character indexed is")
print("The last character indexed is"[-1])

# here is an example of why 0 is the first index as the last index is -1

input("\nPress Enter to continue ... \n")

# DOT NOTATION, this is build in function which calls specific methods.
# Here we will look at the use on strings
print("DOT NOTATION")

input("\nPress Enter to continue ... \n")

# .upper() - change all characters to upper case
print("i am now upper case".upper())

input("\nPress Enter to continue ... \n")

# .lower() - change all characters to lower case
print("I AM NOW LOWER CASE".lower())

input("\nPress Enter to continue ... \n")

# caps - capitalize starting character
print("start with capital letter".capitalize())
input("\nPress Enter to continue ... \n")

# count - counts "l"
print("Count how many letter 'e', there is")
print("Count how many letter 'e', there is".count("e"))

input("\nPress Enter to continue ... \n")

# find - finds first index of character
print("Index is the letter, i")
print("Index is the letter, i".find("i"))  # ITS LOOKSING FOR LOWER CASE 'i'

input("\nPress Enter to continue ... \n")

# replace - replace parts of string with new words
print("replace parts of string with new words")
print("replace parts of string with new words".replace("parts of string", "new words"))

input("\nPress Enter to continue ... \n")

# Strip - removes blank spaces at start and end
print("         Look at all the space at the start    ")
print("         Look at all the space at the start    ".strip())

input("\nPress Enter to continue ... \n")

#Strip - removes blank spaces at start and end
print("strip can also strip")
print("strip can also strip".strip("strip"))

input("\nPress Enter to continue ... \n")

print("Thank you for following my python tutorial 101 ")

