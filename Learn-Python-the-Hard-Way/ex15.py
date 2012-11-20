# access sys module and import argv
from sys import argv

# assign contents of argv to variables
script, filename = argv

# create a file object and assign to a variable
txt = open(filename)

# prints to console
print "Here's your file %r:" % filename
# print a string that read returns from a file object
print txt.read()
txt.close()

# prints to console
print "Type the filename again:"
# prompts user for input which is assigned to a variable
file_again = raw_input("> ")

# create a file object and assign to a variable
txt_again = open(file_again)

# print a string that read returns from a file object
print txt_again.read()
txt_again.close()
