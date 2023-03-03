### I want raise an exception  --->

def divnums():
    num1 = input("please enter num1 : ")
    num2 = input("please enter num2 : ")
    if num2=='0':
        raise ZeroDivisionError("-----Cannot divide num1 by zero- ---")
    if num1.isdigit() and num2.isdigit():
        num1 = int(num1)
        num2 = int(num2)
        res = num1/ num2
        print(res)

divnums()