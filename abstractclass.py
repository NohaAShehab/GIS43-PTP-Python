"""
    create common class structure
    ---> class contain only structure ----> there is no data ---
    ---> define base structure --->child classes must follow it.

    abstraction ---> handle complexity of the code by hiding unnecessary information from user

    ## abstract class {
        abstract method
    }
    ## functionality not complete ---> You cannot take object from it.

    # in python class ---> ABC ---> Abstract Base Class

"""
## Abstract class Person
# from abc import  ABC, ABCMeta, abstractmethod
# class Person(ABC):
#     @abstractmethod
#     def sayWelcome(self):
#         pass
#
# # p= Person()  # error
#
# # class Employee(Person):  # this abstract class
# #     pass
# #
# # e = Employee()
#
#
# class Employee(Person):  # this abstract class
#     def sayWelcome(self):
#         print('---------- Welcome--------------')
#
# e = Employee()
#
#
#
# class Car(metaclass=ABCMeta):
#     pass
#
# c = Car()
#############################################
## to create abstract class
## you must inherit from the ABC class and use the abstractmethod decorator to create
# fully abstract class
# from abc import  ABC, ABCMeta, abstractmethod
# class Person(ABC):
#     @abstractmethod
#     def sayWelcome(self):
#         print("----")
#         pass
#
#     def sayHello(self):
#         print('Hello')
#
# # p = Person()
# # p.sayWelcome()
#
#
# class Employee(Person):  # this abstract class
#     def sayWelcome(self):
#         print('---------- Welcome--------------')
#
# e = Employee()
# e.sayWelcome()
# e.sayHello()

############################################################
# from abc import  ABC, ABCMeta, abstractmethod
#
#
# class Animal(ABC):
#
#     def __init__(self, type):
#         self.type = type
#
#     @abstractmethod
#     def makenoise(self):
#         pass
#
#     def IntroduceMe(self):
#
#         print(f"--- I am an Animal - {self.type} ----")
#
# # a  = Animal('animal')
#
# #
# class Dog(Animal):
#     def makenoise(self):
#         print("--- Bark Bark Bark ")
#
# d = Dog('dog')
# d.makenoise()
# d.IntroduceMe()
#
# class Cat(Animal):
#     def makenoise(self):
#         print("---Meow Meow Meow ")
#
# c = Cat('cat')
# c.makenoise()
# c.IntroduceMe()



"""

    abstract class Animal {
        public int type=1; # property ? instance 
         
        
    
    }
    
    class Dog 




"""
# from abc import ABC, ABCMeta, abstractmethod
#
# ### create common type
# class Animal(ABC):
#     type =''  # class variable
#
#     @abstractmethod
#     def makenoise(self):
#         pass
#
#     @classmethod
#     def IntroduceMe(cls):
#         print(f"=========== I am a {cls.type}")
#
#
# # a  = Animal('animal')
#
# #
# class Dog(Animal):
#     type = 'dog'
#     def makenoise(self):
#         print("--- Bark Bark Bark ")
#
#
# d = Dog()
# d.makenoise()
# d.IntroduceMe()
#
#
# class Cat(Animal):
#     type = 'cat'
#     def makenoise(self):
#         print("---Meow Meow Meow ")
#
#
# c = Cat()
# c.makenoise()
# c.IntroduceMe()
#
# def describeAnimal(animal :Animal):
#     if isinstance(animal, Animal):
#         print(f"---I am Animal {animal} ---")
#         animal.IntroduceMe()
#         animal.makenoise()
#     else:
#         raise  TypeError(f'{type(animal)} ,not allowed Animal type required')
#
# # describeAnimal(10)
# describeAnimal(d)
####################################################################

from abc import ABCMeta, abstractmethod

# class Car(metaclass=ABCMeta):
#     pass
################# This is not allowed
#
# class Car(ABCMeta):
#     @abstractmethod
#     def test(cls):
#         pass
#
# ## create class ---> ABCMETA
# class BMW(Car):
#     def test(cls):
#         print("---- I am BMW 2024")
#
#
# b= BMW('fdd',('test',), {})
##################
""" to use ABCMeta to create abstract class ---> Car(metaclass=ABCMeta) """
class Car(metaclass=ABCMeta):  ### class Car(ABC)
    @abstractmethod
    def test(cls):
        pass
#
class BMW(Car):
    def test(cls):
        print("---- I am BMW 2024")

#
b= BMW()
b.test()



















###### interfaces ? in python
## no explicit inteface in python
## install package provide interface architecture  ---(Class )





