#
# # l = ['Ahmed', 44, True,44,64 ,'Ali']
# # ## squence unpacking
# # # a,b,c,d = l
# # a,b,*c =l
#
# #######3 list comprehension
# ## generate list of even numbers from 0 to 11
# # nums = list(range(0,11, 2))
# # print(nums)
#
# ## generate list ---> number%7==0 ---> 0 , 101
# nums = [ i for i in range(1, 101) if i%7==0]
# print(nums)
#
#
# for index, value in enumerate((5,6,7,7,555)):
#     print(f"{index}:{value}")


l = [4,5,6,73,5, "False"]
print(all(l))  # retrun true if all values in the iterable ---> are truly value
print(any(l)) # return true if any if the values in the iterable are truly value

##########################################
# swap
num1 = 10
num2 = 'iti'
# temp = num1
# num1 = num2
# num2 = temp
print(f"num1={num1}, num2={num2}")
num1, num2 = num2, num1
print(f"num1={num1}, num2={num2}")

###########################################

l = [4,-60,100, 10,23]
# print(l)
# l.sort()  # sort the original list
# print(l)
# print(l.sort())

# print(sorted(l), l)  #new list sorted







