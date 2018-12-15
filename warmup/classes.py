# Create class1
class User:

    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
    
    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    def has_birthday(self):
        self.age += 1

# Init user object
amir = User('Amir Mahmoud', 'amirebrahimi5@gmail.com', 27)

# Edit property
amir.age = 38
janet = User('Jannet', 'jannet@gmail.com', 26)

janet.has_birthday()

# Call method
print(janet.greeting())

# Extend class
class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0
    
    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and I owe a balance of {self.balance}$'

# Init customer
john = Customer('John Doe', 'john@gmail.com', 40)
john.set_balance(4000)

print(john.greeting())

# print(john.balance)