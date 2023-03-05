
# class Employee:
#     def __init__(self,name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
# e = Employee('Ahmed')
# print(e.name)
# print(e.get_name())

######################################################
"""
    accessibility levels ---> access modifiers
    public :: --->can be accessed anywhere ---> this ---> instance
    protected :: can be accesses only in the class -->derived classes
    private :: --> can be accessed only in the class

    ####################### In python No access modifiers #######################
    ## naming convention ---> access modifiers
    --> identifier ---> start (a-z) -----> public
                    ---> start(_) ---> protected
                    ---> start(__) ---> private

    -- special cases :
    __funct__ ===> special methods

"""
# class Employee:
#     def __init__(self,name, email, salary):
#         self.name= name # public
#         self._email = email  #protected
#         self.__salary = salary # private
#
#     def printInfo(self):
#         print(f"""My name is {self.name}
# email: {self._email}
# salary: {self.__salary}""")


# e = Employee("Ahmed", 'ahmed@gmail.com', 10000)
# e.printInfo()

############### use object to get data
# print(e.name)
# # print(e._email)  # ethically don't do this  # itworx
# # print(e._Employee__salary)  # scope binding ..  ## we don't do that here
# # print(e.__salary)
# print(e.__dict__)
############### use object to modify the data
# e.name= 'Ali'
############## ethically don't do this ######################
# e._email = 'ali@gmail.com'
# e.__salary=100000  # add new  property in the runtime
# print(e.__salary)
############## python support OOP
#################################################################################
# class Employee:
#     def __init__(self,name, email, salary):
#         self.name= name # public
#         self._email = email  #protected
#         self.__salary = salary # private
#
#     def printInfo(self):
#         print(f"""My name is {self.name}
# email: {self._email}
# salary: {self.__salary}""")
#
#     def get_salary(self):
#         return self.__salary
#
#     def set_salary(self, salary):
#         if (isinstance(salary, int) or isinstance(salary, float)) and salary >0:
#             self.__salary = salary
#         else:
#             raise Exception(f"salary should be number, can be {type(salary)} ")
#
#
#
#
# ## limit accessebility the properties
#
# e = Employee('Ahmed', 'ahmed@gmail.com', 10000)
# e.set_salary(30000)
# print(e.get_salary())
###################################################################
# class Employee:
#     def __init__(self,name, email, salary):
#         self.name= name # public
#         self._email = email  #protected
#         # self.__salary = salary # private
#         if (isinstance(salary, int) or isinstance(salary, float)) and salary > 0:
#             self.__salary = salary
#         else:
#             raise Exception(f"salary should be number, can be {type(salary)} ")
#
#     def printInfo(self):
#         print(f"""My name is {self.name}
# email: {self._email}
# salary: {self.__salary}""")
#
#     def get_salary(self):
#         return self.__salary
#
#     def set_salary(self, salary):
#         if (isinstance(salary, int) or isinstance(salary, float)) and salary >0:
#             self.__salary = salary
#         else:
#             raise Exception(f"salary should be number, can be {type(salary)} ")
#
#
#

## limit accessebility the properties

# e = Employee('Ahmed', 'ahmed@gmail.com', "iti")
# print(e.get_salary())


####################################
# class Employee:
#     def __init__(self,name, email, salary):
#         self.name= name # public
#         self._email = email  #protected
#         self.set_salary(salary)
#
#
#     def printInfo(self):
#         print(f"""My name is {self.name}
# email: {self._email}
# salary: {self.__salary}""")
#
#     def get_salary(self):
#         return self.__salary
#
#     def set_salary(self, salary):
#         if (isinstance(salary, int) or isinstance(salary, float)) and salary >0:
#             self.__salary = salary
#         else:
#             raise Exception(f"salary should be number, can be {type(salary)} ")
#
#
# e = Employee("Ahmed", 'ahmed@gmail.com', 10000)


#####################3
# class Employee:
#     def __init__(self,name, email, salary):
#         self.name= name # public
#         self._email = email  #protected
#         self.set_salary(salary)
#
#
#     def printInfo(self):
#         print(f"""My name is {self.name}
# email: {self._email}
# salary: {self.__salary}""")
#
#     # print(self.salary
#     def get_salary(self):
#         return self.__salary
#
#     ## self.salary = val
#     def set_salary(self, salary):
#         if (isinstance(salary, int) or isinstance(salary, float)) and salary >0:
#             self.__salary = salary
#         else:
#             raise Exception(f"salary should be number, can be {type(salary)} ")
#
#     @property
#     def salary(self):
#         return self.__salary
#
# e = Employee("Ahmed", 'ahmed@gmail.com', 10000)
# # e.set_salary(1000)
# print(e.get_salary())
# print(e.salary)

###########################################
# class Employee:
#     def __init__(self,name, email, salary):
#         self.name= name # public
#         self._email = email  #protected
#         self.salary = salary
#
#     def printInfo(self):
#         print(f"""My name is {self.name}
# email: {self._email}
# salary: {self.__salary}""")
#
#     @property
#     def salary(self):
#         return self.__salary
#
#     @salary.setter
#     def salary (self, salary):
#         if (isinstance(salary, int) or isinstance(salary, float)) and salary >0:
#             self.__salary = salary
#         else:
#             raise Exception(f"salary should be number, cannot be {type(salary)} ")
#
# e = Employee("Ahmed", 'ahmed@gmail.com', 10000)
# # e.set_salary(1000)
# print(e.salary)
#
# e.salary = 'iti'


###################################################
class Employee:
    def __init__(self,name, email, salary):
        self.name= name # public
        self._email = email  #protected
        self.salary = salary

    def printInfo(self):
        print(f"""My name is {self.name}
email: {self._email}
salary: {self.__salary}""")

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary (self, salary):
        if (isinstance(salary, int) or isinstance(salary, float)) and salary >0:
            self.__salary = salary
        else:
            raise Exception(f"salary should be number, cannot be {type(salary)} ")

    @salary.deleter
    def salary(self):
        self.__salary = None

e = Employee("Ahmed", 'ahmed@gmail.com', 10000)
print(e.salary)































