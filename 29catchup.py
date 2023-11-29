# 29th Nov 2023 => Python catch
"""
1. front end = Vanilla JS/Frameworks[Vue, Svellte, Quick, Next]
2. server = Node[express], PHP[Laravel], Python[Django/flask]...
    > API/RESTful /Endpoint
     - urls that point to a resource
     - It will recieve a tuple obj from the db, convert it to a dictionary then manipulate it.
     - it serializes to an obj and push the data to the client
     
3. Database
     - relational(Table[columns, rows]) or non-relational(Documents/objects)
     - Source of truth
        -- firstName = "B@rcl@y"
        
        
// CRUD
"""

"""
??? Lesson Plan
1. Intro to Python
2. Data types
3. Control flow & loop
5. Functions

4. Python special syntax
    - lambda, comprehension & generators, 

6. Data Structures
7. OOP & decorators
    inhertance
    encapsulation
    arrtibutes & properties
    getter & setters
    magic methods & super keyword
8. Regular expression
"""

###> Intro to Python
# print("Python is a high level, interpreted language.")
# print('Emphasizes on readability')

# variables
"""
name, assignment operator, value
name = value
"""
x = None
floating_number = 2.3
is_Student = False
annon_func = lambda x: x

# print(type(x), type(floating_number), type(is_Student), type(annon_func))


###> Data types
'''
Special type of data/value
Integers: Whole numbers (0-9).
Floats: Numbers with decimal points (3.14, 2.5).
Strings: Text enclosed in quotes ('Hello', "Python").
Booleans: Represents truth values (True, False).
None: empty value
List: [] [x for x in arry if x <= 2]
Tuple: (1,)
Dictionary: {key:value} read/delete O(1) [constant time]
Sets: Unique value
'''

###> Control flow & loop
"""
1. Conditional statements
    => if condition:
        # Excute if conditon is true
       else:
        # Execute if condition is false  
        
    => if condition:
        # run code
       elif condition:
        # run code
       elif condition:
        # run code
       else:
        # default code is run here
    
2. Loops
    => for item in iterable: => O(n)
        # execute for each item
        
    => while condition:  situations where the number of iterations is not predetermined O(n), O(1)
        # Code block executed as long as condition is true
        
"""

###> Functions
"""
*Keyword -> def
*name of function -> snake_case
*does it take any parameters
function signature
"""

def find_values(*args):
    return args

def find_int(**kwargs):
    return type(kwargs)

# print(find_int(name = 45))

def find_value(arr, target):
    i = 0
    while i < len(arr):
        print(i)
        if arr[i] == target:
            return (f'{i} is the index we are looking for')
        i += 1
    return -1

# print(find_value([1,2,3,4,5,6], 7))
# print(find_value([1,2,3,4,5,6], 5))

###> Special py syntax
'''lambda, comprehension & generators, decorators'''

# lambda
add = lambda x,y: x + y

# print(add(0,9))

num = [2.3,6.8,8.5,2.7,6.3,6.6,8]

sqtr_num = list(map(lambda x: x**2, num))
# print(sqtr_num)

data = [(1, 'David'), (2, 'Charlie'), (7, 'Alice'), (4, 'Brian'), (5, 'Ouma'), (6, 'Stanley'),(3, 'Willy')]
sorted_data = sorted(data, key=lambda x: x[1])
# print(sorted_data)

# comprehension & generators
"""
a concise way to create lists, dictionaries, and sets in Python
"""
# lists
a = []
b = list()

b.append((1,2,3))
# print(b)

#dictionary
d = {}
e = dict()

# set
g = set()

# normall for loop
def even_digits(x) -> list[int]:
    new_Arry = list()
    for item in range(len(x)): #O(n)
        if x[item] % 2 == 0:
            new_Arry.append(x[item]) 
            
    return new_Arry

# print(even_digits([1,2,3,4,5,6,7,8]))

def even_number(arry) -> list[int]:
    return [elem for elem in arry if elem % 2 == 0]

# print(even_digits([1,2,3,4,5,6,7,8,10]))

 ###> Object Oriented Programming
 
class Princess:
    # class attributes/variable
    continent = ["Asia", 'Africa', 'North America', 'South America', 'Antarctica', 'Europe', 'Australia']
    
    # create instance attribute
    def __init__(self, name, hair_type, height):
        self._name = name
        self.hair_type = hair_type # private attr
        self.height = height
        # self.race = self.continent
        
    def __repr__(self) -> str:
        return f"{self.name} has {self.hair_type} hair type, and a height of {self.height}."
    
    def say_your_name(self, x):
        return f"My name is {self.name}, and I am from {self.continent[x]}"

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if (isinstance(name, str)):
            self._name = name
    
    name = property(get_name, set_name)
    
    
"""Final beauty Pagent being held in LV"""  
princess1 = Princess("Mulan", "Natural", "5`4``") #Asian
princess4 = Princess("Senje", "Dreadlock", "6`2``") #African Queen
princess5 = Princess("Lexi", "Raven", "5`6``") #South America
princess9 = Princess("Baljeet", "Curly", "4`9``") #Indian

# print(princess1, princess4, princess5, princess9)

print(princess1.name)
princess1.set_name('Nalum')
print(princess1.name)

