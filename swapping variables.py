#swapping  variables :

  # there are multiple methods but there are 2 commonly used methods:
           # they are:
                 # temporary method
                 # pythonic method 

# temporary method:
 
a = 5
b = 7 
print (a,b)
tem = a
a = b 
b = tem 
print(a,b)

# pythonic method:

a = 5 
b = 7 
print ( a, b)
a,b = b,a
print(a,b)