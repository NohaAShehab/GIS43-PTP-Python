
try:
    fileobj = open("students.txt", 'w')
    ### open file for writing starting from the beginning of the file
    # if file doesn't exist python will try to create it ?
    # if the file exists ---> python will remove the data in the file.
except Exception as e:
    print(e)
else:
    print(fileobj)
    # fileobj.write("Random string")   # write from begining of files
    # fileobj.write("=========================")

    ############################3 write after byte 10
    # fileobj.seek(10)
    # fileobj.write('---- Random content --------\n')
    # fileobj.write("--- another content --------")
    # fileobj.seek(0)
    # fileobj.write('Hi')

    ############ writelines --> accept iterable of string
    # fileobj.writelines(['Ahmed', 'Fares', 'Mohamed', 'Mariam', 'Hager\n'])
    # fileobj.writelines(['Ahmed', 'Fares', 'Mohamed', 'Mariam', 'Hager'])
    data = ['Ahmed', 'Fares', 'Mohamed', 'Mariam', 'Hager']
    # convert iterable (consists of strings to a string )
    ## seprator.join(iterable)
    # data = ' '.join(data)
    data = '\n'.join(data)
    fileobj.write(data)

    fileobj.close()
