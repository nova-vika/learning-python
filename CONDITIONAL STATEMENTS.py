# CONDITIONAL STATEMENTS :
      # it let ur program make decision based on condition.

      # TYPES:
            # if
             # else
               # elif
                  # nested if
# IF STATEMENT :

    # used when u want to do something only if the condition is true . 
    # syntax :
       # if<condition> : 

    # example:   

age = 18
if( age >= 18) :
    print("you can vote")

  # IF-ELSE STATEMENT :
      #  used when u want to  choose b\w 2 options .
       #  EXAMPLE :

age = 18 
if(age>=18):
    print("you can vote")
else:
    print("you cannot vote")        

  # IF-ELIF-ELSE STATEMENT :
      #used when you have multiple choices.
  # EXAMPLE:

marks = 75 
if(marks>=90):
    print("GRADE A")
elif(marks>=70):
    print("GRADE B")    
elif(marks>=50):
    print("GRADE C")
else:
    print("FAIL")        

   # NESTED IF STATEMENT:
     # used when u have a condition inside another condition.
     # EXAMPLE:

age = 20
if (age>=18):
    if(age>=60):
      print("senior citizen")
    else:
      print("adult")    



            # CHALLENGE - FIND THE NUM IS POSITIVE , NEGATIVE OR 0 :

number = int(input("Enter a number:"))
if(number==0):
    print("0 is neither positive nor negative")
elif(number>0):
    print(number,"is a positive number")   
elif(number<0):
    print(number,"is a negative number")     





