# print("""---------- Welcome to our validation module,
# copyrights reserved to GIS@iti43""")




def validateNumber(num):
    if isinstance(num, int) or isinstance(num, float):
        return  num
    elif isinstance(num, str) and num.isdigit():
        return int(num)


# mynum = validateNumber('iti')
# print(mynum)
# mynum = validateNumber('44')

def get_char_index(char, word):
    indecies= []
    for i in range(len(word)):
        if word[i]==char:
            indecies.append(i)
    print( indecies)
    return indecies