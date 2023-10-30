def ifPalindrom(s):
    l = len(s)
    i = 0
    while i < l//2:
        if s[i] == s[l-i-1]:
            i += 1
        else:
            return False
    return True



str = ""
print(ifPalindrom(str))
