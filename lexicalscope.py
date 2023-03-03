
# course = 'python' # defined in the script
#
# #### course varaible is a global in the script ---> can be accessed anywhere in the script
#
# print(course)
# def printCourseformAfunction():
#     print(f"course={course}")

##############################################################
#
# def sayhello():
#     name= input("please enter name: ") # define new local variable
#     ## any variable defined inside the function can be accessed only inside the function
#     print(name)
#
# sayhello()
# print("=----")
# # print(name)
#
#

################################################################################33


# course = 'GIS'
#
# def modifycourse():
#     course = 'Python'
#     print(f"course= {course}---> from inside the function")
#
# print(course)
# modifycourse()
# print(course)

##############

# course = 'GIS'
#
# def modifycourse():
#     global course
#     course = 'Python'
#     print(f"course= {course}---> from inside the function")
#
# print(course)
# modifycourse()
# print(course)




# for num in range(10):
#     print(num)
#
# print(num)
#
#
# num=100
# print(num)
# for num in range(10,0,-1):
#     print(num)
# print(num)
########################################################################
### function inside a funciton

# def outerfunction():
#     track = 'GIS'  # local variable can be accessed anywhere in the function scope
#     def innerfunction():
#         print(f"from iside the inner function {track}")
#     innerfunction()
#
# outerfunction()
#############################################
# def outerfunction():
#    # local variable can be accessed anywhere in the function scope
#     track = 'GIS'
#     def innerfunction():
#         print(f"from iside the inner function {track}")
#     innerfunction()
#
#
# outerfunction()

#######################
# def outerfunction():
#    # local variable can be accessed anywhere in the function scope
#     track = 'GIS'
#     def modifyTrack():
#         track = 'GeoInformatics'  # new local variable for this function
#         print(f"from iside the inner function {track}")
#     modifyTrack()
#     print(track)
#
#
# outerfunction()

# def outerfunction():
#    # local variable can be accessed anywhere in the function scope
#     track = 'GIS'
#     def modifyTrack():
#         nonlocal track
#         track = 'GeoInformatics'  # new local variable for this function
#         print(f"from iside the inner function {track}")
#     modifyTrack()
#     print(track)
#
#
# outerfunction()
########################################

# def outerfunction():
#    # local variable can be accessed anywhere in the function scope
#     track = 'GIS'
#     def modifyTrack():
#         global track
#         track = 'GeoInformatics'
#         print(f"from iside the inner function {track}")
#     modifyTrack()
#     print(track)
#
# outerfunction()
# print(track)


def askforInt():
    while True:
        num = input("please enter number: ")
        if num.isdigit():
            return int(num)

        print('---- please enter valid number ')

# def calculator():
#     num1 = askforInt()
#     num2= askforInt()
#     res = num1 + num2
#     print(res)
#
# calculator()
#

"""
    generatearray(4,5)
    [5,6,7,8]

    abdulrahman 
    
    abdu
    lr
    ahm
    an
    
    
    ['iti', 'Ahmed', 'apple' , 'test']
    _____
    -----
    _pp__
    apple
    
    nshehab.iti43@gmail.com
"""

















































