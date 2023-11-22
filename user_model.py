from datetime import datetime

class MockDb:
    """mock database that stores user data in a dictionary"""
    def __init__(self):
        """Initializes the mock database"""
        self.users = {} # Attributes
        self.user_count = 0

    def drop(self):
        """Reinitializing the mock database"""
        self.__init__()

class User:
    """User class model to represents a user in the system."""
    def __init__(self, firstname, lastname, othername, email, phoneNumber, username) -> object:
        """Initializes the user state"""
        self.id = None
        self.firstname = firstname
        self.lastname = lastname
        self.othername = othername
        self.email = email
        self.phoneNumber = phoneNumber
        self.username = username
        self.registered = datetime.utcnow().isoformat()
        self.isAdmin = False

    def save_user(self):
        """Method to save user to the database"""
        database.user_count += 1
        self.id = database.user_count  # Set user ID
        database.users[self.id] = self
        return self.view

    def save_admin(self):
        """Method to register an Admin"""
        setattr(self, 'isAdmin', True)
        setattr(self, 'id', database.user_count + 1)
        database.users.update({self.isAdmin: self})
        database.users.update({self.id: self})
        database.user_count += 1
        return self.view

    def view(self) -> object:
        """Method to jsonify user objects"""
        keys = ["id", "firstname", "lastname", "othername",
                "email", "phoneNumber", "username", "isAdmin"]
        return {key: getattr(self, key) for key in keys}

    def delete_user(self):
        """Method for deleting a user"""
        del database.users[self.id]

    @classmethod #metaprogramming
    def get_user_by_id(cls, id):
        """Method for getting user by id"""
        user = database.users.get(id)
        if not user:
            return False
        return user

    @classmethod
    def get_user_by_email(cls, email):
        """Method for getting user by email"""
        for id_ in database.users:
            user = database.users.get(id_)
            if user.email == email:
                return user
        return None

# Function calls to interact with the classes and methods
if __name__ == "__main__":
    database = MockDb()

    
    # Create instances of User
    user1 = User("John", "Doe", "", "john@example.com", "123456789", "johndoe")
    user2 = User("Alice", "Smith", "", "alice@example.com", "987654321", "alicesmith")
    
    # Create an admin user
    admin_user = User("Admin", "User", "", "admin@example.com", "9876543210", "adminuser")

    # Save users to the database
    user1.save_user()
    user2.save_user()
    
    # Save user as an admin
    admin_user.save_admin()


    # Retrieve a user by ID and print their details
    retrieved_user = User.get_user_by_id(2)  # Assuming the ID is 1
    if retrieved_user:
        print("Retrieved User Details:")
        print(retrieved_user.view())
    else:
        print("User not found.")

    # Delete a user (assuming it exists)
    if retrieved_user:
        retrieved_user.delete_user()
        print("User deleted.")
        
    # Retrieve the admin user by email
    retrieved_admin = User.get_user_by_email("admin@example.com")

    if retrieved_admin:
        print("Admin User Details:")
        print(retrieved_admin.view())
    else:
        print("Admin user not found.")

