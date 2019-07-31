import string
def is_pangram(txt):
    txt=str.lower(txt)
    txt=list(txt)
    s=list(string.ascii_lowercase)
    for i in range(0,25):
        if s[i] not in txt:
            return False
    return True