def SumSquare(num1, num2, num3, num4):
    '''
    A function takes four integer inputs (num1, num2, num3, num4), and returns 
    the sum of squares of four numbers if the numbers meet the basic requirement. 
    The basic requirement is, if num1 is equal to num2 or num3 is equal to num4, 
    the result is sum of squares of all number otherwise 0 is returned. 
    '''
    SS_result = 0
    if num1==num2 or  num3==num4:
        SS_result = num1*num1 + num2*num2 + num3*num3 + num4*num4
    return SS_result

