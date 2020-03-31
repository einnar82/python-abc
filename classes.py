# A class is like a blueprint for creating objects
class User:
    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def greeting(self):
        print(f'Hi {self.name}')

# inheritance


class Customer(User):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'Hi {self.name}, your balance is {self.balance}'


john = User('John Doe', 10)
janet = Customer('Janet Doe', 100)
janet.set_balance(100)

print(john.getName())
print(john.age)
print(janet.greeting())
