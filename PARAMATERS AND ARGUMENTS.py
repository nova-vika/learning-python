# PARAMETERS AND ARGUMENTS :

#  parameter = variable name in function ("variable")

# argument = real value you give when calling the function ("value")


# EXAMPLE:

def greet(name):                    # ----> parameter  (variable)
    print("hello", name)
greet("vikas")                      # ----> argument    (value)




# TYPES OF ARGUMENTS :

# 1.  positional argument :

# you pass values in crt order 
# assign the values crt ly in orderwise 

#  EXAMPLE :

def add(a, b):
    print(a + b)
add(3, 6)                # a = 3 ; b = 6  output: 9



# 2.  keyword argument :

# you use parameternames which calling the function . 
# order doesn't matter .
# you name the argument , so python knows where to put each value .

# EXAMPLE : 

def add(a, b):
    print(a + b)
add(b=3, a=4)          # a + b = 4+3 = 7




# 3. default argument :

# you give a default value in the function definition.
# if no argument is passed the default value is used .

# EXAMPLE : 

def greet(name="vikas"):
    print("hello", name)
greet()                              # output : hello vikas
greet("vikashini")                   # output : hello vikashini