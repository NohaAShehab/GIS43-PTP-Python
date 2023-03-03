# ### syntax error ---> must resolved
# print("-----")
# print('gis'

###################logical errors
# def sumnums(num1, num2):
#     res = num1 * num2
#     print(res)
#
# sumnums(2,2)
# sumnums(3,4)

### unit-test ---->test cases for your scripts
## developer --> unit test for their/code
#################################Runtime errors ######################################

# print("-----------------------------------------------")
# print(name)  # runtime =---> exception

### runtime error / exception ---> unexpected event cased the application to crash

# num = input("please enter number: ")

################# handle the exception
# num = input("please enter number: ")
#
# try:
#     num = int(num)
# except:
#     print("Not valid number ")
#
# print(f"-------------- {type(num)}")

############################3
# num = input("please enter number ")
# try:
#     num = int(num)
# except:
#     print("""Not valid number---the script will continue
# assuming that we are in the equater """)
#     num = 0
#
# print(f"-------------- {type(num)}")


################################################3
# print(course)

# try:
#     print(course)
# except Exception as e:
#     print(e)
#     course = 'Python'
#
# print('---------- after the exception')


# try:
#     print(course)
# except Exception as e:
#     pass
#
# print('---------- after the exception')

# print(int('iti'))

# course ='iti'
# try:
#     print(course)
#     num = input("please enter num: ")
#     num = int(num)
#     # print(6/0)
# except NameError as ne:
#     print(ne)
#     num = 0
# except ValueError as ve:
#     print(ve)
#     num = 1
# except Exception as e:
#     print(e)

#######################################
# course ='iti'
# try:
#     print(course)
#     num = input("please enter num: ")
#     num = int(num)
#     # print(6/0)
# except NameError as ne:
#     print(ne)
#     num = 0
# except ValueError as ve:
#     print(ve)
#     # num = 1
# except Exception as e:
#     print(e)
# else:
#     print("---- the block will be executed only when there is no exceptions ----")
#     print("---------- no problem happened ")
#     num +=10
####################################
# course ='iti'
# try:
#     print(course)
#     num = input("please enter num: ")
#     num = int(num)
#     error = False
# except Exception as e:
#     print(e)
#     error = True
# finally:
#     print("---- this block will be executed always ")
#     if error:
#         exit(100)
#     else:
#         exit()
################33
course ='iti'
try:
    print(course)
    num = input("please enter num: ")
    num = int(num)
except Exception as e:
    print(e)
    error = True
else:
    error = False
finally:
    print("---- this block will be executed always ")
    if error:
        exit(100)
    else:
        exit()































