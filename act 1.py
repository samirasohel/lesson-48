#Write a program to create two classes Dog and Cat, with the same attributes - 
# (name and age) and methods - 
# (info and make_sound). 
# Create different objects for each class and pass the parameters.
#  Showcase the concept of polymorphism in this program.

class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def make_sound(self):
        print("Dog Barks at strangers")

class cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def make_sound(self):
        print("Cat makes sound meow")

d1=Dog("Galaxy",2)
c1=cat("mimi",3)

for animal in (d1,c1):
    animal.make_sound()