                                                                      
 #LIST:                                                                                                                        
    # A list in Python is like a basket where you can keep multiple items (like numbers, words, toys, anything!).

         #fruits = ["apple", "banana", "orange"]
     
            #Here, fruits is a list. It stores 3 items.



#🔢 Important Points:
       
       #Lists are ordered (items have positions starting from 0).

       #Lists are changeable (you can add/remove items).

       #Lists can store different types of data (numbers, words, even other lists!).


#🛠️ Common List Functions/Methods :

 #Method	                        What it does                           Example

#append(item)	              Adds item at the end	                  my_list.append(50)

#insert(index, item)	      Adds item at specific position	      my_list.insert(1, 15)

#remove(item)         	      Removes the first matching item         my_list.remove(20)

#pop()                   	  Removes the last item	                  my_list.pop()

#pop(index)                   Removes item at given index	          my_list.pop(0)

#clear()	                  Removes all items                       my_list.clear()

#index(item)                  Returns the index of an item	          my_list.index(30)

#count(item)	              Counts how many times item appears      my_list.count(10)

#sort()	Sorts                 the list in ascending order	          my_list.sort()

#reverse()                    Reverses the order of the list	      my_list.reverse()

#len()                        Returns the number of items	          len(my_list)

# min()                       minimum                                 min(my_list)

# max()                       maximum                                 max(my_list)

# sum()                       add                                     sum(my_list)

# EXAMPLE CODES :

numbers = [3, 1, 4, 1, 5]
numbers.append(6)
print(numbers)

numbers = [3, 1, 4, 1, 5]
numbers.extend([6,7])
print(numbers)

numbers = [3, 1, 4, 1, 5]
numbers.insert(0,2)
print(numbers)

numbers = [3, 1, 4, 1, 5]
numbers.remove(1)
print(numbers)

numbers = [3, 1, 4, 1, 5]
numbers.pop()
print(numbers)

numbers = [3, 1, 4, 1, 5]
numbers.pop(1)
print(numbers)

numbers = [3, 1, 4, 1, 5]
numbers.clear()
print(numbers)

numbers = [3, 1, 4, 1, 5]
print(numbers.index(4))


numbers = [3, 1, 4, 1, 5]
print(numbers.count(1))


numbers = [3, 1, 4, 1, 5]
numbers.sort()
print(numbers)

numbers = [3, 1, 4, 1, 5]
numbers.reverse()
print(numbers)

numbers = [3, 1, 4, 1, 5]
print(len(numbers))

numbers = [3, 1, 4, 1, 5]
print(min(numbers))
print(max(numbers))

numbers = [3, 1, 4, 1, 5]
print(sum(numbers))



       # LIST COMPREHENSSION :

           #List comprehension is a concise way to create a new list by applying an expression to each item in an iterable

           # 📌 Basic Syntax

                 #[expression for item in iterable]

                  #This is the same as:
   #                     new_list = []
  #                        for item in iterable:
 #                           new_list.append(expression)


 # EAMPLES : 

 #1. 🔢 Create a list of squares of numbers from 1 to 5 :

squares = [x**2 for x in range(1,6)]
print(squares)


#. 🔤 Create a list of uppercase letters:

letters = ['a','b','c']
uppercase = [char.upper() for char in letters]
print(uppercase)



#3. 🙅‍♀️ Add a condition (filter even numbers only):

even = [x for x in range(10) if x % 2 == 0]
print(even)


#4. filter nly even numbers:

odd = [x for x in range(10) if x%2==1]
print(odd)