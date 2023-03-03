
try:
    fileobj = open("students.txt", 'w')
    ### open file for writing starting from the beginning of the file
    # if file doesn't exist python will try to create it ?
    # if the file exists ---> python will remove the data in the file.
except Exception as e:
    print(e)
else:
    print(fileobj)
    fileobj.close()
