# LOOPS :

   # .. do something reapeatedly based on the condition .


   #                   TWO TYPES 

   #            /                    \ 
   #   entry control loop      exit control loop

   #     /         \                   \
   #   for     while                  python does not have this .

#_________________________________________________________________________________________________
#                                  FOR LOOP : 
  
   # it is used to repeat a block of code for each item in a sequence ( like a string , list or a range of numbers).

   # syntax :

     #  for variale in sequence:
          # code block to repeat 

  # you dont need to increase the variable manually - python does it for you.


#                                EXAMPLES : 

# EG 1 - PRINT NUMBERS 1 TO 5:

for i in range(1,6):                      # note :  range(1,6)- starts from 1 go up to 5 not 6  
    print(i)                                 
                                                 # range(start  ,   end ,    step)
                                                 #         |         |         |
                                                 #     starting     ending    increment or decrement 
                                                 #      value       value      value


# EG 2 - PRINT CHARACTERS OF A STRING:

for letters in "vikas":
    print(letters)

    


# EG 3 - LOOP THROUGH LIST :

fruits = ["apples","banana","cherry"]
for fruits in fruits:
    print(fruits)    

#__________________________________________________________________________________________________    
 
     #                                      WHILE LOOP : 
    
           # reapeatedly runs a block of code as long as a condition is true .

           # syntax:
               # while(condition):
                   # block of code 

           # python checks the condition .
           # if true- it runs the code.
           # it keeps checking and running again and again until the condition become false.

                          # EXAMPLE:
count = 1                                     # IMPORTANT : 
while count <= 5:                                  # ALWAYS UPDATING THE VARIABLE (LIKE COUNT+=1)
    print(count)                                   # OR IT BECOMES AN INFINITE LOOP.
    count += 1 
