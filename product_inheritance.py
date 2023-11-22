from datetime import datetime


class MockDb:
    """
    mock database that stores user data in a dictionary
    """

    def __init__(self):
        """Initializes the mock database"""
        self.users = {} # Attributes
        self.products = {}
        self.user_count = 0


    def drop(self):
        """Reinitializing the mock database"""
        self.__init__()
        
database = MockDb()

class User:
    """User class model to represents a user in the system."""

    def __init__(self, firstname, lastname, othername, email, phoneNumber, username):
        """Initializes the user details"""
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

    def view(self):
        """Method to jsonify user objects"""
        keys = ["id", "firstname", "lastname", "othername",
                "email", "phoneNumber", "username", "isAdmin"]
        return {key: getattr(self, key) for key in keys}


    def delete_user(self):
        """Method for deleting a user"""
        del database.users[self.id]

    @classmethod
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

class Product(MockDb):
    """Product class model to represent a product in the system."""
    
    def __init__(self, name, price, description, creator_id):
        """Initializes the product details"""
        super().__init__()
        self.name = name
        self.price = price
        self.description = description
        self.creator_id = creator_id  # ID of the user who created the product
        self.created_at = datetime.utcnow().isoformat()
        
        self.save_product()
    
    def save_product(self):
        """Method to save product to the database"""
        if not hasattr(self, 'id'):
            self.id = len(self.products) + 1  # Assign unique ID
        self.products[self.id] = self  # Update database with product
        return self.view()
    
    def view(self):
        """Method to jsonify product objects"""
        keys = ["id", "name", "price", "description", "creator_id", "created_at"]
        return {key: getattr(self, key) for key in keys}

# Example of usage:
if __name__ == "__main__":
    
    import pdb; pdb.set_trace()

    # Create users
    user1 = User("John", "Doe", "JD", "john@example.com", "123456789", "johndoe")
    user2 = User("Alice", "Smith", "", "alice@example.com", "987654321", "alicesmith")

    # Save users to the database
    user1.id = 1
    user2.id = 2
    database.users = {user.id: user for user in [user1, user2]}

    # Create products associated with users
    product1 = Product("Laptop", 1200, "High-performance laptop", creator_id=1)
    product2 = Product("Phone", 800, "Latest smartphone", creator_id=2)

    # Save products to the database
    product1.save_product()
    product2.save_product()

    # Retrieve products and their creators
    retrieved_product1 = database.products.get(1)
    retrieved_product2 = database.products.get(2)

    if retrieved_product1:
        creator_id = retrieved_product1.creator_id
        creator = database.users.get(creator_id)
        if creator:
            print(f"Product 1 (ID: {retrieved_product1.id}) created by {creator.firstname} {creator.lastname}")
        else:
            print("Creator details for Product 1 not found.")

    if retrieved_product2:
        creator_id = retrieved_product2.creator_id
        creator = database.users.get(creator_id)
        print(f"Product 2 (ID: {retrieved_product2.id}) created by {creator.firstname} {creator.lastname}")
