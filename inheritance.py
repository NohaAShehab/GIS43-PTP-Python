
# class Person:
#     pass
#
# class Employee(Person):
#     pass
#
# emp = Employee()
# print(emp, type(emp))
# print(isinstance(emp, Person))
####################################################
# class Person:
#     def __init__(self,name):
#         self.name= name
#
# class Employee(Person):
#     pass
#
# emp = Employee('Ahmed')
# print(emp, type(emp))
# print(isinstance(emp, Person))
#
####################################################################################
# class Person:
#     def __init__(self,name):
#         self.name= name
#
#     def speak(self):
#         print(f"--- from Person , I am {self.name}")
#
# class Employee(Person):
#     def __init__(self, name,email):
#         super().__init__(name)
#         self.email = email
#
#
# emp = Employee('Ahmed', 'ahmed@gmail.com')
# emp.speak()

############################
# class Person:
#     def __init__(self,name,has_brain):
#         self.name= name
#         self.has_brain = has_brain
#
#     def speak(self):
#         print(f"--- from Person , I am {self.name}")
#
# class Employee(Person):
#     def __init__(self, name,email):
#         self.email = email
#         # self.name = name
#         # self.has_eyes = True
#         super().__init__(name, True)
#         super(Employee, self).__init__(name, True)
#
#
# emp = Employee('Ahmed', 'ahmed@gmail.com')
# emp.speak()



#####################3

# class Person:
#     def __init__(self,name,has_brain):
#         self.name= name
#         self.has_brain = has_brain
#
#     def speak(self):
#         print(f"--- from Person , I am {self.name}")
#
# class Employee(Person):
#     pass
#
# class Manager(Employee):
#     def __init__(self, dept):
#         super(Manager, self).__init__('ahmed', True)
#         self.dept = dept
#
#
# m = Manager('GIS')

#####################################
# class Person:
#     def __init__(self,name,has_brain):
#         self.name= name
#         self.has_brain = has_brain
#
#     def speak(self):
#         print(f"--- from Person , I am {self.name}")
#
# class Employee(Person):
#     def __init__(self, email, salary):
#         self.email  = email
#         self.salary = salary
#         super(Employee, self).__init__('test', True)
#
# class Manager(Employee):
#     def __init__(self, dept):
#         super(Manager, self).__init__('ahmed', True)
#         self.dept = dept
#
#
# m = Manager('GIS')
#
# print(isinstance(m, object))
#
# ###
# l = []
# l.append('rrr')

############################ mutiple inheritence
# class A:
#     def display(self):
#         print("I am the display of Class A")
#
#
# class B(A):
#     # def display(self):
#     #     print("I am the display of Class B")
#     pass
#
#
# class C(A):
#     # def display(self):
#     #     print("I am the display of Class C")
#     pass
#
#
# class D(B, C):
#     # def display(self):
#     #     print("I am the display of Class D")
#     pass
#
#
# o = D()
# o.display()
#
#
#


################################



































