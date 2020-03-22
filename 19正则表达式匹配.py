def match(L, pattern):
    if(not L or not pattern):
        return False
    return matchCore(L, pattern)

def matchCore(L, pattern):
    if(L == pattern):
        return True
    if( L != '' and pattern == ''):
        return False
    if(len(pattern) >= 2 and pattern[1] == '*'):
        if(L[0] == pattern[0] or (pattern[0] == '.' and L[0] != '')):
            return matchCore(L[1:], pattern[2:]) or\
                    matchCore(L, pattern[2:]) or\
                    matchCore(L[1:], pattern)
        else:
            return matchCore(L, pattern[2:])
    elif(L[0] == pattern[0] or (pattern[0] == '.' and L[0] != '')):
        return matchCore(L[1:], pattern[1:])
    return False

if __name__ == '__main__':
    a = 'aaa'
    b = 'a*a'
    print(match(a,b))