
"""
try_except.py
=====
Follow the instructions in the comments.

Example Output:
that key doesn't exist
that index doesn't exist
you tried to divide by 0!
incorrect type!
foo isn't defined
"""

# create a dictionary named d with key 'color', value 'red'
d ={"color":"red","value":"0"}


# print out the value at key 'shape'
try:
	print d['shape']
except KeyError:
	print "that key doesnt exist"
# what kind of error occurs? Keep that in mind so that you can...
# go back and add a try except block around it... make sure to catch the right kind of error!
# print out your own message regarding the error



# create a list named numbers and set it equal to a range(10)
numbers = range(0,9)


# print out the value at index 20
try: 
	print number[20]
except IndexError:
	print "this index doesn't exist"
except NameError:
	print "this name doesn't exist"
	
# what kind of error occurs? Keep that in mind so that you can...
# go back and add a try except block around it...  make sure to catch the right kind of error!
# print out your own message regarding the error



# try dividing 9 by 0
d ={"score":9}
k ="score"
divisor = 0
try:
	print d[k]/divisor
except ZeroDivisionError:
	print "this doesnt work"

# what kind of error occurs? Keep that in mind so that you can...
# go back and add a try except block around it...  make sure to catch the right kind of error!
# print out your own message regarding the error



# try dividing 9 by "a string"
d ={"score":9}
k ="score"
divisor = "string"
try:
	print d[k]/divisor
except TypeError:
	print "you can't divide by strings"

# what kind of error occurs? Keep that in mind so that you can...
# go back and add a try except block around it...  make sure to catch the right kind of error!
# print out your own message regarding the error



# try calling a function that doesn't exist... for example, just type foo()
try:
	print foo()
except NameError:
	print "It doesn't exist"
# what kind of error occurs? Keep that in mind so that you can...
# go back and add a try except block around it...  make sure to catch the right kind of error!
# print out your own message regarding the error
