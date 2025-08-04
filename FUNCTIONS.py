# FUNCTIONS :
     
#🧠 What is a Function?

#         A function is a block of reusable code that performs a specific task. Instead of writing the same code again and again, we just define it once and use it anywhere.

#✅ Why use Functions?

     #Reusability

        #Makes code clean and readable

           #Easy to debug and test

                 #Saves time

#🔤 Syntax of a Function

#def function_name(parameters):
#     code block
#       return result  # (optional)



            # EXAMPLES:

def greet():
  print("hello vikas!")
greet()  

def add():
  a = int(input())
  b = int(input())
  print(a+b)

add()


# RECURSIVE FUNCTION : 

       #  Recursive Function = Function that calls itself.

#It must have:

#✅ A base case (stop point)

#🔁 A recursive case (keep calling)


# BEST EXAMPLE - FACTORIAL OF a NUMBER . 

n = int(input("Enter a number:"))
def factorial(n):
  if n == 1:
    return 1 
  else:
    return n * factorial(n-1)
print(factorial(n))  
  

#🚀 . Using Built-in Function from Python

              #Python has a built-in way using the math module:

n = int (input("Enter a number:"))
import math 
print(math.factorial(n))

#Best for quick use — fast, clean, and optimized.


# FIBONACCI SERIES :

       # each num is the "sum of the previous 2 num".
       # 0,1,1,2,5,8,......etc
        
       # RULE :
           #......1st num = 0
           #......2nd num = 1
           #......3rd num = previous num + one before that.

           # so.....
               # 0+1 = 1
               # 1+1 = 2
               # 1+2 = 3
               # 2+3 = 5
               #.............etcc

# CODE :

n = int(input("Enter how many Fibonacci numbers to print: "))
def fibonacci(n):
  a = 0
  b = 1
  for i in range(n):
    print(a,end="")
    c = a+b
    a = b
    b = c
fibonacci(n)    
  