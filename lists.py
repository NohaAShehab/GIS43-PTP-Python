
# 1- to define a list
l = ['python', 'C#', 'java']
myl = [334,False,'iti' ,'noha', 234.43, l, 'iti', 'iti']

# access elements uning start form 0
print(myl[2])
print(myl[5][1])

print(len(myl))

print(myl.count('iti'))

## get index of element
myl = [334,False,'iti' ,'noha', 234.43, l, 'iti', 'iti']
print(myl.index('noha'))
print(myl.index('iti'))  # get the index of the first
# occurence of the element

### list is mutable ---> You change list content after creation
myl[3] = 'Noha Shehab'
print(myl)

## add element to the list
myl.append("new element")

## insert element at index
myl.insert(3, 'inserted element')
myl.insert(100, 'inserted element') # insert it at the end
## remove element from the list
popped_element=myl.pop()

#pop element at index
popped_element2 = myl.pop(4)

## remove  ---> value
myl.remove('iti') # remove first occurrence of the element

# myl.remove("Noha Shehab")
## in operator
if 'Noha Shehab' in myl:
    myl.remove("Noha Shehab")
else:
    print("--- element not found ---")

# list concat ?

l1= [4, 'iti', False]
l2 = ['val', True]
newl = l1 + l2   # return new list
l1.extend(l2)  # extend l1 with l2 content


### sort the list ---> make sure list elements from the same type
## sort the same object
# ll = [5,6,7,233,54,546,-19,-20, 'iti', False]
ll = [5,6,7,233,54,546,-19,-20]
print(ll)
# ll.sort()  # ascending
ll.sort(reverse=True)
print(ll)
## sorted
names = ['Ahmed', 'noha', 'Ali', 'Omar']  # asci code
names.sort()
print(names)
####################### reverse
# ll = [5,6,7,233,54,546,-19,-20, 'iti', False, ['ff', 'df']]
# ll.reverse()
# print(ll)

### loop over any

# for abbasss in myl:
#     print(f"element = {abbasss}")

ll = [324,5646,'Ahmed', 'Ali', True]
# countt = 0
# for item in ll:
#     if countt == 2:
#         break
#     print(f"item = {item}")
#     countt +=1
#

index = 0
for item in ll:
    print(f"{index}: {item}")
    index +=1

### min , max ?
print(min([4,5,6]))

############### genertate list of numbers
# ll = []
# num = 0
# while num < 11:
#     ll.append(num)
#     num +=1
#
# print(ll)

## range ?
## generate set of values

r = range(10) # range object
#
# for i in r:
#     print(f"i = {i}")


# cast it to a list
r = list(r)
print(r)

for i in range(3):
    print(i, ll[i])


myr= range(1, 3)
myr = list(myr)
print(myr)


num =  input("please enter number")



