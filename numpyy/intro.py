
# ll = [4,5,6,True]
# print(ll)
#
# print(id(ll[0]))
#
# print(id(ll[1]))

#### create array using numpy
import numpy as np

## create array
# myarr = np.array([5,6,5,7])
#
# print(myarr)
# myarr = np.array([5,6,5,7, "test"])  # not valid
#
# print(myarr)
##################
#### size integers in python depend operating system
# myarr = np.array([5, 6, 5, 7])
# print(myarr.dtype)
#
# ## array of floats
# # lst = [5,6,7]
# # arr2 = np.array(lst, dtype=np.float16)  # iterable object
# # print(arr2)
# # print(arr2.dtype)
# #
# # for item in arr2:
# #     print(item)
# # print('----------------------')
# # for item in arr2.astype('int'):
# #     print(item)
# ######################################
# # lst = [7, 2, 9, 10, 11]
# # arr = np.array(lst)
# #
# # print(arr.shape)
# # print(arr)
#
# #############3
# # lst = [[7, 2, 9, 10, 11], [4,5,6,7,6]]
# # arr = np.array(lst)
# #
# # print(arr.shape)
# # print(arr)
#
# #########################
# # lst = [
# #     [[5, 3, 4], [9, 1, 3]],
# #     [[5, 3, 4], [9, 1, 3]],
# #     [[5, 3, 4], [9, 1, 3]]
# #
# # ]
# # arr = np.array(lst)
# # print(arr)
# #
# #
# # print(arr.shape)
#
# ############################3
# # myl = [1, 2, 3, 4, 5, 6]
#
# # arr = np.array(myl)
# # print(arr)
# # print(arr.shape)
# #
# # arr=arr.reshape(1,2,3)
# # print(arr)
# # print(arr.shape)
# #
# #################################
# # lst= [1, 2, 3, 4, 5, 6]
# # l2= lst+ [10]
# # arr = np.array(lst)
# # print(arr)
# #
# # print(arr + np.array([500]))
# #################
# lst= [1, 2, 3, 4, 6]
# l2= lst+ [10]
# arr = np.array(lst)
# print(arr)
#
# # print(arr + np.array('iti'))
# ###################
#
# res = np.append(arr, 1000)
# print(res)
#
# arr = res.reshape(3, 2, 1)
# print(arr)
#
# # print(arr + np.array([500])) # Broadcasting
#
#
# #############################
#
# # arr = np.arange(24)
# # print(arr)
#
# ## generate array using arange
# # arr = np.arange(24).reshape(2,3,4)
# # print(arr)
# #
# # print(arr.ndim)
# # print(arr.astype('float'))
# #
# #
# #####################################
#
# a = np.arange(1,25)
# # print(a)
#
# a=a.reshape(12,-1)
# # print(a)
# # # print(a.ravel())
# #
# # print(a.reshape(-1))
# # print(a.flatten(-1))
#
#
# a = np.expand_dims(a, axis=0)
#
# print(a)
################################
a = np.arange(1,25)

a=a.reshape(12,-1)
print(a)

# a = np.expand_dims(a, axis=0)
# print(a)



# a = np.expand_dims(a, axis=2)
# print(a)


# arr = np.arange(10).reshape(-1, 1, 1)
# print(arr)
# print(arr.squeeze())
####
arr = np.arange(1,11)
print(arr)

myarr = np.linspace(0,1,10)
print(myarr)

print(np.linspace(10, 100, 11))

print(np.random.rand())

## reverse string
name = 'noha'
print(name[::-1])