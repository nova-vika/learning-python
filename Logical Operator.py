# Logical Operator :
# there are three types :
      #>>>>> and
      #>>>>> or
      #>>>>> not

# and :
   # true if both are true 
   # otherwise false

a = 5 
print(a>2 and a<10)
print(a<2 and a<10)

# or :
   # true if any one is true
   # otherwise false

a = 5
print(a<6 or a>6)
print(a>7 or a>8)


# not :
   # reverse the condition

a = True
print(not(a))

b = False
print(not(b))  

# using integers

a = 0 
print(not(a))

b = 6
print(not(b))

#>>>>>>>>>>> QUIZZZZ

#find the output :

num = 10
print(num>5 and num<15)
print(num % 2==0 or num % 3 == 0)
print(not(num==0))