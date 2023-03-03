""" any python (.py) is a python
module and can be imported anywhere in other script"""

################ import all the module ##################33
# import validationModules
#
# age =  input("please enter age: ")
# age = validationModules.validateNumber(age)
# if age:
#     print("--- it is a number:")
# else:
#     print("--- not valid ====")
#################################
#### when we import the module we use module name to access any part of the module
# import validationModules as vm
# print(vm.mynum)
# age =  input("please enter age: ")
# age = vm.validateNumber(age)
# if age:
#     print("--- it is a number:")
# else:
#     print("--- not valid ====")

##############################################3


################## Import part of the module

# from validationModules import validateNumber
#
# age =  input("please enter age: ")
# age = validateNumber(age)
# if age:
#     print("--- it is a number:")
# else:
#     print("--- not valid ====")
#
# from validationModules import validateNumber as vn
#
# age =  input("please enter age: ")
# age = vn(age)
# if age:
#     print("--- it is a number:")
# else:
#     print("--- not valid ====")

####################

# def get_char_index(char, word):
#     indecies= []
#     for i in range(len(word)):
#         if word[i]==char:
#             indecies.append(i)
#     print( indecies)
#     return indecies
import iti.subfolder.test
from validationModules import get_char_index
# get_char_index('i', 'information technology institute')

# apple  , _pp__






################## any folder / directory contain python modules ---> package --
## import package ===> or part of it

# import gis.greeting
#
# gis.greeting.greet("Ahmed")

# import packagename.modulename
# import gis.greeting  as gt
# gt.sayWelcome("Ahmed")

#### import only function from the package
# from gis.greeting import sayWelcome
# sayWelcome("Ali")

####


from gis.greeting import *  # import all functions in the greeting


### import packagename.modulename
## from packagename.modulename import funcationname, variablename
## from packagename.modulename import *



####
# import iti.math_module
# iti.math_module.sumnum(3,5)

# from iti.math_module import sumnum
# sumnum(4,5)

# import  iti


# import gis
#
# gis.greeting.sayWelcome("jjjj")



# from iti import sumnum  # call function using package name

# from iti.subfolder.test import saytest

# from iti import saytest
# saytest()

# import iti

# iti.saytest()

from iti import *
# iti.subfolder.test.saytest()










