'''
OOPs Concepts:

    Object
    Class
    Method
    Inheritance
    Polymorphism
    Data Abstraction
    Encapsulation


'''


''' Class and Objects '''


class Animal:
    def speak(self):
        print("Animal Speaking")
# child class Dog inherits the base class Animal


class Dog(Animal):
    def bark(self):
        print("dog barking")


dog = Dog()
dog.bark()
dog.speak()


'''
o/p:

dog barking
Animal Speaking

'''

''' Constructor '''


''' inheritence '''
