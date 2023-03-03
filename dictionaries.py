
### key value pair datatype ---> access element using keys

# to define a dict
d = {}
myd = dict([])

## comma -sepereated key value pair
## dict doesn't allow key duplicates
## from python 3.6 --> dictionary ---> sorted
myd = { "name":"noha", "track": "GIS","branch":"smart", "name":"Noha Shehab"}
print(myd)
#### mutable datatype
myd["track"]= "GeoInformatics"  # update
print(myd)
myd["intake"]=43  # if key not exists --> will add the pair to the dict
print(myd)
print(myd["name"])

myd = { "name":"noha", "track": "GIS","branch":"smart",5:"iti"}
print(myd[5])
myd[5]='updated'

# myinfo = [4,63,4,5,6]
# myinfo={"width":4, 'heigh':63, "depth":5}

## dict
myd = { "name":"noha", "track": "GIS","branch":"smart",5:"iti"}
# print(len(myd))
# keys = myd.keys()
# print(keys)  # iterable object can be casted to list or tuple
# # for k in keys:
# #     print(k)
# keys =list(keys)
# print(keys)

myd = { "name":"noha", "track": "GIS","branch":"smart",5:"iti"}
vals = myd.values()
print(vals)
items = myd.items()
print(items)

# for item in myd:
#     print(item)  # keys

test = {"name":"ahmed", "track":'GIS', 'branch':"smart"}
# for item in test:
#     print(f"key ={item}, value = {test[item]} ")
test = {"name":"ahmed", "track":'GIS', 'branch':"smart"}
for k, v in test.items():
    print(f"{k}:{v}")


for m in test.items():
    print(m)


# updated

test = {"name":"ahmed", "track":'GIS', 'branch':"smart"}
myd = {'intake':43, "track":"GeoInformatiocs"}
test.update(myd)
print(test)

# if "ahmed" in test:  # check in keys
#     print("found")
# else:
#     print("not found")

if "ahmed" in test.values():  # check in keys
    print("found")
else:
    print("not found")


# test.clear()  # empty dict

# del test  # remove any reference / variable from the memory

## pop key:value pair from the dict
popped_item=test.pop("name")  # pop remove
print(popped_item)
print(test)




