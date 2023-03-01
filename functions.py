

## functions
## functions known numbers of arguments

# def myfun():
#     pass
# r=myfun()
# print(r)
###############
# def myfun():
#     return
# r=myfun()
# print(r)
####
# def sayhello():
#     print("Hello world ")
#
# sayhello()
# sayhello()


# def sayhello(name):
#     print(f"Hello {name}")
#
# sayhello('Ahmed')

# def sumnums(num1, num2):
#     res = num1 +  num2
#     return res
#
# myres = sumnums(2,4)
# print(myres)

############
# def sumnums(num1, num2):
#     res = num1 +  num2
#     return res
#
# myres = sumnums("Ahmed", "Ali")
# print(myres)
##################3

# def sumnums(num1, num2):
#     res = num1 +  num2
#     return res

# myres = sumnums("Ahmed", 5)
# print(myres)

##################################

### check type of variable
# print(isinstance('noha', str))
# print(isinstance(12, str))

# def sumnums(num1, num2):
#     if isinstance(num1, int) and isinstance(num2, int):
#         res = num1 +  num2
#         return res
#
# myres= sumnums(3,'iti')



# def sumnums(num1 :int, num2 :int):
#     if isinstance(num1, int) and isinstance(num2, int):
#         res = num1 + num2
#         print(res)
#
# sumnums(4,5)
# sumnums('ahmed', 'ali')

# def getfullname(firstname, lastname):
#     fullname = firstname + " " + lastname
#     return fullname, firstname, True

# name = getfullname("Noha", 'Shehab')  # contain tuple of returned values
# print(name)
# def getfullname(firstname, lastname):
#     fullname = firstname + " " + lastname
#     return (fullname, firstname, True), 'False'
#
# name = getfullname("Noha", 'Shehab')  # contain tuple of returned values
# print(name)



######################################################
## python allow default arguments for the function

# def sumnum(num1, num2):
#     print(f"num1= {num1}, num2 = {num2}")
#     return num1+num2
#
# rs =sumnum(4,5)


# def sumnum(num1=1, num2=10):
#     print(f"num1= {num1}, num2 = {num2}")
#     return num1+num2
#
# rs =sumnum(4,5)
# rse =sumnum()
# ress= sumnum(3)


# def sumnum(num1, num2=10):
#     print(f"num1= {num1}, num2 = {num2}")
#     return num1+num2
# #
# rs =sumnum(4,5, 843987, 9234098)
# rse =sumnum(88)
# ress= sumnum(3)


# print("Ahmed", end='#')
# print("Mostafa")
# print("Ahmed", "Ali", 'Mohamed', sep='__||__')

# ################### functions with unknown number arguments
# print()
# print("Ahmed")
# print()
# print("000")

# def askforstudent( *students):  # * function accept zero or more arguments
#     print(students) #tuple
#
# askforstudent()
# askforstudent('Ahmed', 'Ali',44, (44,5,5))

###############################################################################
# def introduceyourself(** info):
#     print(info)
#     return
#
# introduceyourself(name='noha',work='iti',lives='cairo',age=30)
# introduceyourself()
# introduceyourself(fullname='Eman Ayman')

######################## string
mytemp= "My name is {0} , I lives in {1}."
print(mytemp.format('noha', 'cairo'))

mytemp= "My name is {username} , I lives in {city}."
print(mytemp.format(username='noha', city='cairo'))

































