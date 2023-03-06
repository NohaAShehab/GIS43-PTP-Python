### lamabda ---> anaymous function , clouser


### function return a function

# def base():
#     print("---- I am the base function ")
#
# def mymain ():
#     print("--- my function is called ")
#     return base
#
# x = mymain()
# # x()
# mymain()()


#####################################
# def incrementbyten(num):
#     print("---- incrementing by 10 ")
#     return num+10

# def askfornum():
#     num = input("please enter num1: ")
#     try:
#         num =  int(num)
#         print(num, type(num))
#         return lambda : num+10
#     except:
#         return None
#
# m= askfornum()
# print(m)
#
# print(m())



# def askfornum():
#     num = input("please enter num1: ")
#     try:
#         num =  int(num)
#         print(num, type(num))
#         return lambda num1 , num2, num3: num+num1+num2+num3
#     except:
#         return None
#
# m= askfornum()
# print(m(4,5,6))


# def askforstring(message):
#     mystr = input(message)
#     mystr = mystr.strip()
#     print(mystr)
#     return mystr, lambda msg='Hi': f"{msg} {mystr.upper()}"
#
#
# res = askforstring("please enter name ")
# print(res[1]())




# def demo():
#     print('demo')

# def myfun(test ):
#     print(test)
#
# myfun(demo)
#
# def testfun(m): ## m ---> callable object may be lamda
#     print(m)
#     print(m(10))
#
# testfun(lambda x: x*x)
####################################
# l = [3,5,10,20]
# # for item in l:
# #     print(item)
# ##
# myiterator = iter(l)
# print(myiterator)
#
# print(next(myiterator))
# print("---- hello world ----")
# print("-ksjfklsdj----")
# num = input("--- please enter num ----")
#
# myvar = next(myiterator)
# print(myvar+100)
#
#
# myvar = next(myiterator)
# print(myvar*100)
#
# myvar = next(myiterator)
# print(myvar)
#
# # myvar= next(myiterator)
# print(myiterator.__next__())
# print(next(myiterator))

######################## Generator
## special function ---:> generate values

# def generate_nums(start, end):
#     nums = []
#     for num in range(start, end):
#         print(num)
#         nums.append(num)
#
#     return nums
#
#
#
# numm=generate_nums(1,200)
# print(numm)

#
# def generate_nums(start, end):
#     for num in range(start, end):
#         yield num
#
#
#
#
# numm=generate_nums(1,200)
# print(numm)

# print(next(numm))
# print(next(numm))
# print(next(numm))
# print(next(numm))
#
# for num in numm:
#     print(num)
#################################################

# map is used to apply functionality on iterable
# names = ['ahmed', 'ali', 'abdelrahman', 'eman', 'mariam','hager', 'hadeer']
# for i in range(len(names)):
#     names[i] = names[i].upper()
#
# print(names)

# names = map(lambda name: name.upper(),
#             ['ahmed', 'ali', 'abdelrahman', 'eman', 'mariam','hager', 'hadeer'])
# ## map --> return map object ---> can be casted to a list
#
# print(list(names))


# nn = ['ahmed', 'ali', 'abdelrahman', 'eman', 'mariam','hager', 'hadeer']
# names = map(lambda name: name.upper(),nn)
# ## map --> return map object ---> can be casted to a list
#
# print(list(names))
############## filter

nn = ['ahmed', 'ali', 'abdelrahman', 'eman', 'mariam','hager', 'hadeer']
namess = filter(lambda name: name[0]=='a', nn)
print(namess)
print(list(namess))






















