class Animal:
    def speak(self):
        return "Generic animal sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def animal_sound(animal):
    return animal.speak()

dog = Dog()
cat = Cat()
animal = Animal()

print(animal_sound(dog)) # Output: Woof!
print(animal_sound(cat)) # Output: Meow!
print(animal_sound(animal)) # Output: Generic animal sound
