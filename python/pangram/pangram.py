def is_pangram(txt):
    list(txt)
    a="abcdefghijklmnopqrstuvwxyz"
    list(a)
    txt.lower()
    i=j=p=0
    
    for i in len(a):
        for j in len(txt):
            if a[i] is txt[j]:
                p +=1
                break
                
            else :
                p-=1
                break
    if p >= 26 :
        return True
    else:
        return False
                

