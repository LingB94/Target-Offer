def Sum0(n):
    return 0

def SumForN(n):
    funChoice = {False:Sum0, True:SumForN}
    flag = not not n
    result = n+funChoice[flag](n-1)
    return result

if __name__ == '__main__':
    print(SumForN(5))