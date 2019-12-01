def is_armstrong_number(number):
    """ Function returns True or False depending if Armstrong"""

    check = number          
    s=len(str(number))
    sum = 0
    while(number > 0):
        a = number % 10             # to get Unit place number
        sum = sum + (a ** s)
        number = int (number/10)    # To get the new number for next iteration
    if sum == check :               # Checks with the number
        return True
    else: 
        return False
