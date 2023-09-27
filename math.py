import math
method = input("Are you adding, subtracting, multiplying or dividing these numbers?")
method = method.lower()
int_a = input("What is the first integer?")
int_a = int(int_a)
int_b = input("What is the second integer?")
int_b = int(int_b)
if method == "adding":
    print("INITIALISING.")
    value = (int_a+int_b)
    value = str(value)
    print("Sum:"+value+".")
if method == "subtracting":
    print("INITIALISING.")
    value = (int_a-int_b)
    value = str(value)
    print("Sum:"+value+".")
if method == "multiplying":
    print("INITIALISING.")
    value = (int_a*int_b)
    value = str(value)
    print("Sum:"+value+".")
if method == "dividing":
    print("INITIALISING.")
    value = (int_a/int_b)
    value = str(value)
    print("Sum:"+value+".")
else:
    print("INADEQUATE METHOD.")
