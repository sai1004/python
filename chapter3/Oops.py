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



''' Constructor '''





''' inheritence '''

    class Animal:  
        def speak(self):  
            print("Animal Speaking")  
    #child class Dog inherits the base class Animal  
    class Dog(Animal):  
        def bark(self):  
            print("dog barking")  
    d = Dog()  
    d.bark()  
    d.speak()  
    
    
    '''
    o/p:
    
    dog barking
    Animal Speaking

    '''
