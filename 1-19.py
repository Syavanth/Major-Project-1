class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Some generic sound"


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  
        self.breed = breed
    
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
    
    def speak(self):
        return "Meow!"


dog = Dog(name="Buddy", breed="Golden Retriever")
cat = Cat(name="Whiskers", color="Tabby")

print(dog.name)    
print(dog.breed)   
print(dog.speak()) 

print(cat.name)    
print(cat.color)   
print(cat.speak()) 
