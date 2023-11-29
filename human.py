class Human:
    species = "Homo sapiens"
    def __init__(self, name):
        self.name = name
        self._age = 0

    def get_age(self):
        print("Retrieving age.")
        return self._age

    def set_age(self, age):
        if (type(age) in (int, float)) and (0 <= age <= 120):
            print(f"Setting age to { age }.")
            self._age = age

        else:
            print("Age must be a number between 0 and 120.")

    age = property(get_age, set_age,)
    
user1 = Human('Guido')
user1.age = 45
print(user1.age)