# for i in range(10):
#     # if i==5:
#     #     continue
#     print(f'i = {i}')
# else:
#     print('--- this block will be executed if the completed')
# print("---- Loop eneded -----")


""" if(name=='ahmed'){}"""
# for i in range(10):
#     if i==5:
#         pass
#     print(f'i = {i}')
# else:
#     print('--- this block will be executed if the completed')
# print("---- Loop eneded -----")

# for i in range(10):
#     pass
# name=''
# if name=='ahmed':
#     pass


for i in range(10):
    if i==4:
        continue  # go to next iteration
    if i==5:
        pass # do nothing
    print(f"i = {i}")


######################## enumerate
l = [3,5,6,7,4,44]
name = 'Ahmed'

# for i in l:
#     print(i)
for index, i in enumerate(l):
    print(f"{index}: {i}")


enum = enumerate(l)
print(enum)

myd= {"name":"noha", 'track':"GIS"}
for index, item in enumerate(myd):
    print(f"{index}: {item}, {myd[item]}")

