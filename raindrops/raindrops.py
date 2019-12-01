def convert(number):
    s = ""
    if number % 3 == 0 :
        s = "Pling"
    elif number % 5 == 0 :
        s += "Plang"
    elif number % 7 == 0 :
        s += "Plong"
    else :
        s = str(number)
    
    return s

  
