# JUMP STATEMENT : 
#      |
#      |____  BREAK    --->   stops the loop immediately .
#      |
#      |____  CONTINUE --->   skip the current step and goes to the next .
#      |
#      |____  PASS  ------>   does nothing , used when you want to right the code later .

# EXAMPLES :

# BREAK STATEMENT :

for i in range(1,6):
 if i == 3 :
  break
 print(i)


# CONTINUE STATEMENT :

for i in range(1,6):
 if i == 3:
  continue
 print(i)


# PASS STATEMENTS :

for i in range(1,6):
 if i == 3:
  pass
 print(i) 
