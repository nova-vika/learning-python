   # SOME LOGICAL PROBLEMS
    
# FINDING AVERAGE mark:

mark1 = float(input("Enter Physics Mark:"))
mark2 = float(input("Enter Chemistry Mark:"))
mark3 = float(input("Enter Maths Mark:"))
Total_mark = mark1 + mark2 + mark3
Average = Total_mark / 3 
print(Average)

# value substituting in an expression : a**3 + 2ab + c**2
 
a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))
value = a**3 + 2 * a * b + c**2
print(value)


# Unit digit : 
     # we can use negative index and also remainder method :

# negative indexing:     

num = (input())
print((num)[-1])

# REMAINDER METHOD :

       # UNIT DIGIT:

num = int(input())
print(num%10)

       # TENTH DIGIT :

num = int(input())
num = num//10
print(num%10)