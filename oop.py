# Into to Object-Oriented Programming -> Classes & Objects/Instance
"""
Defining a class
constructor & Magic methods
variable in classes and methods(Instance & class attributes)
Instance Methods
Object initilization
"""

class Employee: #blueprint
    # class attributes
    
    def __init__(self, first_name, last_name, phone_number) -> object:
        # instance attributes
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.salary = 0
        
    def __str__(self) -> str:
        return f'{self.first_name}, {self.last_name} has a phone number of {self.phone_number}, and gets paid {self.salary}'
    
    def show_self(self):
        """Instance method"""
        return self
        
    # instance method
    def set_salary(self, salary):
        self.salary = salary
    


# instance / object

user1 = Employee("Jane", "Joe", '072200000')
user2 = Employee("John", "Joe", '011100000')
user3 = Employee("Kind", "Man", "")

user1.set_salary(1000)
user2.set_salary(3000)
user3.set_salary(65000)

print(user1.salary)
print(user1.show_self())
print(user2)
print(user3.last_name, user3.salary)



