
# l = [3,3,4]
# l.append('iti')
# print(type(l))
# print(type('iti'))

# dims = [4,5,6]  # width, height, length

# dims= {'width':4, 'height':5, 'length':6 }  # data labels
#########################################
# emp1 = {
#     "id":1, "name":"Ahmed", "salary":1000
# }
# emp2 = {
#     "emp_id":2, "fullname":"Fares", "sal":25000
# }

############### create your own datatype === Classes
# class ---> structure or blueprint of the object

# class Employee:
#     pass

# # to take an object from class
# emp = Employee()
# print(emp)
# ### loosely dynamically typed lang.
# emp.name  ='Ahmed'
# emp.salary =2000
# # print(emp.name)
# # print(emp.email)
# emp3=  Employee()
# emp3.fullname ='noha'

##########################################################################
#
# class Employee:
#     def __init__(self):
#         # constructor
#         print('this function is called while creating the object ')
#         print(self)
#         print('------------------------------------------------------')
#
# emp =  Employee()
# print(emp)
#
# emp2= Employee()
#
# emp3 = Employee()
###########################################################33

# class Employee:
#     def __init__(self):
#         self.name = 'Ahmed'
#         self.salary=10000
#
# emp =  Employee()
# print(emp)
#
# emp2= Employee()
#
# emp3 = Employee()


#########################
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary=salary
#
# emp =  Employee('ahmed', 2000)
# print(emp.name)
# emp.name = 'Ahmed Mohamed'
# print(emp.name)
# emp.city = 'Cairo' # dependent on lang. behaviour
#
# emp2= Employee('ali', 3000)

# emp3 = Employee('mohamed', 4400)
######################################################3
# class Employee:
#     def __init__(self, name, salary=3000):
#         ### define properties of the object ,,,,, instance variable ?
#         self.name = name
#         self.salary =salary
#
# emp =  Employee('ahmed', 2000)
# emp2= Employee('ali')
###########################################################
# class Employee:
#     def __init__(self, name, salary=3000):
#         ### define properties of the object ,,,,, instance variable ?
#         self.name = name
#         self.salary =salary
#
#     ## instance method ---> applying behaviour on the the caller instance // object
#     def speak(self):  # self the caller instance
#         print(f"my name is {self.name}")
#
# emp =  Employee('ahmed', 2000)
# emp.speak()
#
# emp2= Employee('ali')
######################################################
# class Employee:
#     def __init__(self, name, salary=3000):
#         self.name = name
#         self.salary =salary
#
#     # def speak(self):  # self the caller instance
#     #     print(f"my name is {self.name}")
#     def speak(myvar):  # the first paramter in the function ---> represent the caller instance
#         print(myvar)
#         print(f"speak test {myvar.name}")
#
# emp =  Employee('ahmed', 2000)
# # print(emp)
# # emp.speak()
# Employee.speak(emp)
#
#
# # emp2= Employee('ali')
##########################################################
# class Employee:
#     def __init__(self, name, salary=3000):
#         self.name = name
#         self.salary =salary
#
#     # def speak(self):  # self the caller instance
#     #     print(f"my name is {self.name}")
#     # instance method ---> depends on the instance
#     def speak(self, message='Dummy message'):
#         print(f"my name is {self.name}, {message}")
#
#
# emp1 = Employee("Abdelrahman",4000)
# emp1.speak()
# emp1.speak("---Nice to meet you -----")

###################################### class variable
# class Employee:
#     nationality = 'Egyptian'  # class variable ---> represent property related to the class
#     def __init__(self, name, salary=3000):
#         self.name = name
#         self.salary =salary
#     def speak(self, message='Dummy message'):
#         print(f"my name is {self.name}, {message}")
#
#
# emp1 = Employee("Ahmed", 40000)
# # print(emp1.nationality)
#
# print(Employee.nationality)
#
# emp2 = Employee('Eman', 50000)
#
# Employee.nationality = 'American' ## modify the value of the nationality in the class itself


############### global scope and classes
# specialization = 'GIS'
# deduction = input("please enter deduction")
# try:
#     deduction= float(deduction)
# except Exception as e:
#     deduction = .2

# class Employee:
#     nationality = 'Egyptian'  # class variable ---> represent property related to the class
#     def __init__(self, name, salary=3000):
#         self.name = name
#         self.salary =(1-deduction)*salary
#     def speak(self, message='Dummy message'):
#         print(f"my name is {self.name}, {message}")
#         print(specialization)
#
#     def modifyGlobal(self):
#         global  specialization
#         specialization = 'Arc-GIS'
#
# emp1 = Employee("Ahmed", 40000)
# emp1.modifyGlobal()
# emp1.speak()
############################ class method

################################################################################333
# class Employee:
#     nationality = 'Egyptian'  # class variable ---> represent property related to the class
#     count = 0
#     def __init__(self, name, salary=999):
#         self.name = name
#         self.salary =salary
#         Employee.count +=1
#     def speak(self, message='Dummy message'):
#         print(f"my name is {self.name}, {message}")
#     @classmethod
#     def get_no_of_objects(cls):
#         print(cls.count, cls)
#         return cls.count
#
#     @classmethod   ### object factory ?
#     def generate_defaultEmployee(cls):
#         return cls("Ahmed", 40000)
#
# emp1 = Employee("Ahmed", 40000)
# Employee.get_no_of_objects()
# emp2 = Employee.generate_defaultEmployee()
##################################################################
# class MyComplex:
#
#     def __init__(self, real, img):
#         self.real= real
#         self.img = img
#     @classmethod
#     def addcomplex (cls, comp1, comp2):
#         r = comp1.real + comp2.real
#         i = comp1.img + comp2.img
#         return cls(r,i)
#
#     def __add__(self, other):
#         r = self.real + other.real
#         i = self.img + other.img
#         return MyComplex(r, i)
#
#
# c1 = MyComplex(4,5)
# c2 = MyComplex(6,7)
# # c3 = MyComplex.addcomplex(c1, c2)
# # print(c3, type(c3))
# c3 = c1+c2
#
#
# l = [4,5,6]
# l.append('rr')

################################################################################

# class Employee:
#     nationality = 'Egyptian'  # class variable ---> represent property related to the class
#     count = 0
#     def __init__(self, name, salary=999):
#         self.name = name
#         self.salary =salary
#         Employee.count +=1
#     def speak(self, message='Dummy message'):
#         print(f"my name is {self.name}, {message}")
#     @classmethod
#     def get_no_of_objects(cls):
#         print(cls.count, cls)
#         return cls.count
#
#     @staticmethod   # method is helper method ---> independent of the class , instance
#     def calnetsal(salary):
#         return salary * .89
#
# emp1 = Employee("Ahmed",30000)
# emp2= Employee('Ali', 40000)
#
# print(Employee.calnetsal(100000))
# print(Employee.calnetsal(emp1.salary))
#
# print(emp1.calnetsal(emp1.salary))
#
# def calnetsal(salary):
#     return salary*.89
# #
# print(calnetsal(emp1.salary))
# print(calnetsal(100000))
#
# print(emp1.__dict__)  # return object properties into a dict .


class Employee:
    __slots__ = ['name', 'salary']
    __dict__ = {}
    nationality = 'Egyptian'  # class variable ---> represent property related to the class
    count = 0
    def __init__(self, name, salary=999):
        self.name = name
        self.salary =salary
        Employee.count +=1



emp1= Employee('Ahmed', 34455)
print(emp1.__dict__)
# emp1.email = 'ahmed@gmail.com'

emp3= Employee('Ahmed', 34455)
# emp3.address = 'Cairo'
































































