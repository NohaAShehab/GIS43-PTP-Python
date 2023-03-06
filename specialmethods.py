
"""
    all class in python ---> implicitly extends from object class

# """
#
# l = [3,5]
# l.append('test')

# class Car:
#     def __init__(self, model , price, color):
#         self.model = model
#         self.price = price
#         self.color = color
#
#     def __str__(self):
#         return f"{self.model}"
#
# c = Car('MiniCoper', 100000, 'Blue')
# print(c)

########################3
# class Car:
#     def __init__(self, model , price, color):
#         self.model = model
#         self.price = price
#         self.color = color
#
#     # def __str__(self):
#     #     return f"{self.model}"
#
#     def __repr__(self):  # developer
#         return f"Car(model={self.model}, price={self.price}, color={self.color})"
#
#
# c = Car('KIA', 455666,'White' )
# ## when you try to print the object ---> check if the __str__ implement ---> call it
# ## if not ---> check if __repr__ implement ---> call it ---> else:---> print object address
# print(c)  # call __str__ function
# print(c.__repr__())
###################################
# l =[3,4,5]
# print(len(l))
# print(len(399999))
# class Car:
#     def __init__(self, model , price, color):
#         self.model = model
#         self.price = price
#         self.color = color
#
#     def __repr__(self):  # developer
#         return f"Car(model={self.model}, price={self.price}, color={self.color})"
#     def __len__(self):  #must retrun with number
#         return len(self.__dict__)
#
# c = Car('KIA', 455666,'White' )
# c.year= 303
# print(len(c))

##################### object callable


# class Car:
#     def __init__(self, model , price, color):
#         self.model = model
#         self.price = price
#         self.color = color
#         self.__no_of_calls= 0
#
#     def __repr__(self):  # developer
#         return f"Car(model={self.model}, price={self.price}, color={self.color})"
#     def __len__(self):  #must retrun with number
#         return len(self.__dict__)
#
#     def __call__(self, *args, **kwargs):
#         # print('car object is being called ')
#         print("||----------------------------------------------")
#         self.__no_of_calls +=1
#         pass
#


# c = Car('KIA', 455666,'White' )
# c()

#############################################
class Car:
    def __init__(self, model, price, color):
        self.model = model
        self.price = price
        self.color = color
        self.__no_of_calls = 0

    def __repr__(self):  # developer
        return f"Car(model={self.model}, price={self.price}, color={self.color})"

    def __len__(self):  # must retrun with number
        return len(self.__dict__)

    def __call__(self, *args, **kwargs):
        # print('car object is being called ')
        print("||----------------------------------------------")
        self.__no_of_calls += 1
        pass


    def __le__(self, other):  # less than or Equal, other ---> object from car
        return (self.price <= other.price)
        # return True

    def __lt__(self, other):
        return (self.price < other.price)

c = Car('Fait', 234234, 'black')
c2 = Car('ttt', 43980985, 'tt')
# print(c <= c2)  # __le__
# print(c < c2) #  __lt__
myl = [c, c2]
myl.sort()
print(myl)






















