# # 1- to define tuple
# t = ('python', 'C#', 'java')
# myt = (334,False,'iti' ,'noha', 234.43, t, 'iti', 'iti')
#
#
# # access elements uning start form 0
# print(myt[2])
# # print(myl[5][1])
#
# print(len(myt))
#
# print(myt.count('iti'))
#
# print(myt.index('noha'))
#
# print('Ahmed' in myt)
#
# # tuple is immutable datatype
#
# ## tuple concatenation
# t1= ('Ahmed', 'Ali', 33)
# t2 = ('test', 'fdf', True)
# t3= t1 + t2
# print(t3)
#
# # myl =['Khaled', 'Ahmed', 'Ali', 'mona']
# # print(myl)
# # myl.sort()
# # print(myl)
# tt = (324,5646,'Ahmed', 'Ali', True)
#
# for item in tt:
#     print(f"item = {item}")
#
# for c in 'noha':
#     print(c)
#
# # for i in 324:
# #     print(i)
#
#
# t = (('ahmed',10),('Khaled', 20), ('ttt','rr','rr'))
# # for item in t:
# #     print(item)
# #     for k in item:
# #         print(k)
# #     print("----------------------")
#
# # for item1, item in t:
# #     print(f" {item1}: {item}")
# t = (('ahmed',10),('Khaled', 20), ('ttt','rr','rr'))
# for i in range(1,len(t)):
#     print(f"{i}: {t[i]}")
#
#
#
# print(min(('ahmed','noha', 'ali')))
# # print(min(True, False))
# # print(max([4,5], [40,5]))
#
# # t = (('ahmed',10),('Khaled', 20), ['ttt','rr','rr'])
# # t[2][2]= 'updated'
# # print(t)
ll= ['ttt','rr','rr']
t = (('ahmed',10),('Khaled', 20),ll )
t[2][2]= 'updated'
print(t)

# mys = list(t)
# print(mys)
#
# mys = tuple(mys)
# print(mys)




t= ('Ahmed',)
print(t, type(t))

mytuple = tuple('Noha')  # string is the iterable
print(mytuple)
mytuple2 = tuple(['noha', ['dfd']])  # this iterable
print(mytuple2)

########## to define a tuple
# t = ()
# myt = tuple([])
# mytt = tuple()

t = (33,)
myt = tuple([333],)  # item
mytee = tuple([[333]],)
# mytt = tuple(333)



myr = range(0,10,2)
myr = tuple(myr)
print(myr)


## generate tuple or list 0-0> accept only
# iterable object



