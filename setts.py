## set ---> non primitive mutable data structure
# that can hold different values from different datatypes


myset = set()
myset2 =set([])
## doesn't allow duplication in items
## no index
## unsorted day
s = {'Ahmed', 'Ali' , 55, True, 'Ahmed',445.55}
print(s)
### mutable
s.add('added element')
print(s)

## pop element form the set
popped_element=s.pop() # remove random element
print(popped_element)
print(s)

# t =('rr','uuu', 'rrr')

# mys= {'Ahmed', 4, ['test', 'iti', 'Ali'], 44.33}

# mys= {'Ahmed', 4, ('test', 'iti', 'Ali'), 44.33}
# mys= {'Ahmed', 4, ('test', 'iti', 'Ali', [33,444]), 44.33}
# ss = {"Ahmed", "Ali" , {33,455, 'mm'}}

## hashing depends on immutability

## update
myset ={"Samy", 'Fares', 'Eslam', 'Eman','Hager', 'Ahmed', 'Ahmed', 'Ali'}
sets = {"tt", 'fdf', 'Ahmed', 'Mohmaed', 100, 100}
# myset.update(sets)
# print(myset)
sets.update(myset)


# numbers are immutable datatypes
num =100
# num[0] = 200
### cast list to a set ..
l = [4,5,6,'iti','iti']
l = set(l)
print(l)
for item in l:
    print(item)

