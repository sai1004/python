'''
OOPs Concepts:

    Object
    Class
    Constructor
    Inheritance
    Polymorphism
    Data Abstraction
    Encapsulation


'''


''' Class and Objects '''


class Animal:
    def speak(self):
        print("Animal Speaking")


'''

 Constructor 
 
class Profile:

    def __init__(self,name,email,mobile):

        self.name = name
        self.email = email
        self.mobile = mobile      
 
 '''


''' 
inheritence 

'''


class Animal:

    def speak(self):

        print("animal Speaking")

# child class Dog inherits the base class Animal


class Dog(Animal):

    def bark(self):
        print("dog Barking!")


pugDog = Dog()

print(pugDog.bark())
print(pugDog.speak())

'''
o/p:

dog barking
Animal Speaking

'''


class Cat(Animal):

    def Meoow(self):
        print("cat Meow")


cat = Cat()

print(cat.Meoow())
print(cat.speak())
