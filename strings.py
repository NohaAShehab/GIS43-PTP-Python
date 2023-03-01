
work = "Information Technology Institute"

print(work[2:8])
print(len(work))
# print(work[100])

"""count"""

mystr = 'iti iti iti noha ahmed iti '
print(mystr.count('i'))
print(mystr.count('iti'))
print(mystr.count('f'))

#####################################
# print(work.__len__())

# fname = "Noha"
# mid = "Abd El-Hady"
# lastname = "Shehab"
# # fullname = fname + mid + mid + lastname
# fullname = fname + mid*2 + lastname
# print(fullname)
#

# name = 'ahmed mohamed mostafa'
# print(name.capitalize()) # return new string
# print(name.upper())
# name= name.upper()
# ############
# valuetoreplace= '@'
# mystr = 'repalced value'
# greet = """Welcome to your first python
# @  ----- @ ------- @
# course provided by @  @ """
# # print(greet.replace("@", "iti", 2 ))
# print(greet.replace(valuetoreplace, mystr, 1 ))

############# check string value
# teststr = 'Ahmed'
# ### check value in the string
# print(teststr.isdigit())  # check pure numbers or not
#
# if teststr.isdigit():
#     teststr = int(teststr)
#
# print(teststr.isalpha()) # return true if the string consists of
# ## pure alpahpets a-z
#
# print("Hello GIS".isalpha())
#
# mystr = '                             '
#
# print(mystr.isspace())
#
#
# print("234".isnumeric())  # suppert wider range of numbers
#
# print("my name is Noha".count(' '))
#

#######################################################3
# message = '$  Nice to     meet   you all   @'
# print(message)
# print(message.strip()) # strip spaces from the string from the
# # beginning and the end of the string   ### return new string
#
# print(message.lstrip())
# print(message.rstrip())
# print(message.strip("@$ "))
# print(message.lstrip("@$ "))

##########################################################
####### format string #############
# name = 'noha'
# age = 30
# info = 'My name is '+ name + 'I am '+ age + 'years old'
# infotemp = "My name is  {0} I am  {1} years old"
# print(infotemp.format(name,age))  # format ---> new string
# print(infotemp.format(name,age))
# print(infotemp.format(age, name))
#
# name = 'noha'
# age = 30
# infotemp = "My name is {myname} I am  {myage} years old"
# # print(infotemp.format(myage=age, myname=name))  # format ---> new string


############# f-format string #####################
name = 'noha'
age = 30
## define string temp dependent on existing variables
infotemp = f"My name is {name} I am  {age} years old, {num}"
print(infotemp)

















