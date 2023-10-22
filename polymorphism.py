class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def animal_speak(animal):
    return animal.speak()

my_dog = Dog()
my_cat = Cat()

print(animal_speak(my_dog))
print(animal_speak(my_cat))
