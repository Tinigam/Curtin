def min3():
    
    value1 = int(input("Enter 1st number: "))
    value2 = int(input("Enter 2nd number: "))
    value3 = int(input("Enter 3rd number: "))
    result  = -1
    if value1<value2 and value1<value3:
        result = value1
    elif value2<value1 and value2<value3: 
        result = value2
    else:
        result = value3
    return result

