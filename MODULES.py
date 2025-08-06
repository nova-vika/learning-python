                                      # MODULES : 

 #A module is just a Python file (.py) that contains code you can reuse — like functions, variables, or classes.

#It helps you:

     #Organize code into parts ✅

       #Avoid repeating code ✅

          #Use helpful tools made by others ✅


#📦 2 Types of Modules:

  
#Type                     	 Examples

#Built-in	              math, random, time, os 

#user defined function     your own py file


#🧠 Why are modules useful?

#They help you:

#    Keep code clean and organized

#    Reuse code across projects

#    Access powerful features (like math, dates, random numbers) without writing from scratch


#🔹 How to Use a Module?

#>>>>>>>> Use the keyword import.

#Example 1: Import a built-in module:

import math
print(math.sqrt(16))   # Output: 4.0

#Example 2: Import specific function:

from math import sqrt
print(sqrt(25))   # Output: 5.0



                        # PACKAGES 


 # A package is a collection of Python modules grouped together inside a folder.

    #Real Life Example:

           #Suppose you have a project about math tools:

           #Your folder (package) looks like this:


#          math_tools/         ← 📁 this is your package
#         │
#         ├── __init__.py     ← 🧠 tells Python this is a package
#         ├── add.py          ← ➕ module to add numbers
#         └── multiply.py     ← ✖️ module to multiply numbers



#🧠 What is __init__.py?

      # It is a special Python file.

          # It can be empty.

               # Its main job: tell Python that this folder is a package.

                      # Without it, Python won’t treat the folder as a package.


 #✅ Summary to Remember:

             #Concept	Meaning :

#                   Package	  --->   A folder with Python files (modules)

#                   Module	  --->   A .py file with functions/variables

#                 __init__.py --->   Tells Python that folder is a package                     