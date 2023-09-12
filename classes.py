# Function sample
# def add(x, y):
#     return x + y

# sum = add(3, 5)
# print(sum)

# Sample use of class
class Animal:
    # Write Initializing function
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print("Eating....")
    def breathe(self):
        print("Breathing...")

# Calling the Animal class functions    
# animal1 = Animal("dog")
# animal1.eat()
# animal1.breathe()

# Inheritance
class Dog(Animal):
    def sound(self):
        print("Barking...")

class Cat(Animal):
    def sound(self):
        print("Meow...")
        
# Printing dog abilities
dog1 = Dog("labrador")
dog1.eat()
dog1.sound()

# Printing cat abilities
cat1 = Cat("Sheyne")
cat1.eat()
cat1.sound()
