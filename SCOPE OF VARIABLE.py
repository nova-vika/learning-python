# SCOPE OF VARIABLES :

 # SCOPE :
    # where a variable can be used or accesed in a code .
 
 # Two main types of scope :

        #... global scope -- a variable outside of all functions.
      
        #...local scope -- a variable inside a function.


# KEY RULES TO REMEMBER : 

      #.. local variable can access global variable .

      #.. globle variable cannot access local variable inside a function.

      #.. if u try to change a global variable inside a function u need to use GLOBAL keyword .

# EXAMPLE :

x = 10 
def my_function():
  y = 5
  print("Inside function : x = ",x)
  print("Inside function : y = ",y)
my_function()
print("outside function:x = ",x)
#print("outside function:y = ",y) --> error : 'y' is not defined


# EXAMPLE with global keyword :

x = 5
def change():
   global x 
   x = 10
change()
print(x)   

