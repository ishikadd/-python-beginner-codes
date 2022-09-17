
from codecs import namereplace_errors


Greeting = "Good Morning!, "
you = "ASS :) "
# print(Greeting + you) # this way we can add and joint strings
a = Greeting + you #easy way to do the above 
print(a)
name = "Ishika"
print(name[0]) # write the no. of the index in the squarebrackets '[]' to get the letter.''
print(name[5])
# name[3] = "gg" # TypeError: 'str' object does not support item assignment
# slicing
''' '[0:length]' is 0 to length of the string i.e it will only print values  
 from 0 to (length-1); no. can be inter-changed'''
# print(name[1:5]) # print(name[0:5]), print(name[2:4]) etc.   
print(name[0:]) # is same as 0 to the end length i.e [0:6]
print(name[:6]) # is same as first word to length-1 i.e [0:6]
c = name[-6:-3] # is same as name[0:3]
print(c)
''' skipping in string slicing'''
# name = "Ishika"
# print(name[0::2]) # it will print all letters ":2" and skip every 2nd letter.