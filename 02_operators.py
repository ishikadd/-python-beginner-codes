a = 3
b = 2
# Aarithmetic Operators: (+, -, *, /)
print("The value of 3+2 is", 3+2)
# print("3*2 is", 3*2)
# print("the values of a+b & a*b are", a+b,"and", a*b)
print("The value of 3*2 is", 3*2)
print("The value of a-b is", a-b)
print("The value of a-b is", a/b)

# Assignment Operators: (+=, -=, *=, /=)
c = 5
c += 5 #(+= adds new value to the previous assigned value)
c -= 5 #(-= subtracts new value from the previous assigned value)
c *= 5 #(*= multiplies new value to the previous assigned value)
c /= 5 #( /= devides new value by the previous assigned value) as there is a float sign it will
# assign floating value
print(c)

# Comparison Operators (<, >, <=, >=, ==, !=)
d = (5<6) # it compares the two values and give boolean in return
d1 = (5>6)
''' d1 = (5<=6) # '<=' greater then or equals too; if 1 of the 2 is true then true or else false.
 d1 = (5>=6)
 d1 = (5==6) # equals too sign '=='
 d1 = (5!=6) # not('!') equals too sign '!=' '''
print(d)
print(d1)

# Logical Operators (and, or, not)
bool1 = True
bool2 = False
print("The value of bool1 and bool2 is", (bool1 and bool2)) 
''' ('and' is boolean alg which returns true in case both true or else false. )'''
print("The value of bool1 or bool2 is", (bool1 or bool2)) 
''' ('or' is boolean alg which returns true only if 1 of the 2 is true or else false. )'''
print("The value of not bool1 is", (not bool1)) 
''' ('not' is boolean alg which returns the opposite of the actual value and
it only works with one variable.)'''
