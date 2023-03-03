

### operations on files ---> read , write , append
### read --> read file content
### write --> write data to the file starting from the beginning of the file (override)
### append  ---> write data to the file at the end of the file (keep old content)
#
# num =10
#
# def myfun():
#     print("0000")
############################################
### 1- open file stream ---> decide what do you want to do ? read , write , append
## 2- do operation ... read content, modify
### 3- close file
## open(file , mode) ---> mode r , w , a , r+

#################### Read ###################
# fileobj= open("mycv.txt", 'r')
# print(fileobj)
try:
    # fileobj = open("mycv.txt", 'r')
    fileobj = open("mycv.txt") # default mode --> is read
except Exception as e:
    print(e)
else:
    print(fileobj)  # file object ---> TextIOWrapper
    # data=fileobj.read()  # read all the content in the file into one string
    # print(data, type(data))
    ### read first 10 bytes from the file
    # data = fileobj.read(10)
    # print(data)
    # print("-----------------------")
    # data = fileobj.read()
    # print(data)

    # read from the 10 byte
    # fileobj.seek(10)
    # data = fileobj.read()
    # print(data)
    ########################### read file line by line
    # lines = fileobj.readlines()
    # print(lines)  # return content of the files in a list --->

    # data = fileobj.read()
    # lines = data.split('\n') #split string into a list
    # print(lines)

    ######
    lines = []
    for line in fileobj:
        lines.append(line)
    print(lines)

    ####
    fileobj.close()

