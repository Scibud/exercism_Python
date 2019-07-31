def is_armstrong_number(number):
    check = number
    s=len(str(number))
    sum = 0
    while(number > 0):
        a = number % 10
        sum = sum + (a ** s)
        number = int (number/10)
    if sum == check :
        return True
    else: 
        return False
