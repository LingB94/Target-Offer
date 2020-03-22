def Print1toMax(num):
    if(num <= 0):
        return False
    numArray = ['0'] * num
    while(not Incre(numArray)):
        printNum(numArray)

def Incre(L):
    lastone = False
    takeover = 0
    length = len(L)
    for i in range(length-1, -1, -1):
        plusone = int(L[i])+takeover
        if(i == length-1):
            plusone += 1
        if(plusone >= 10):
            if(i == 0):
                lastone = True
            else:
                takeover = 1
                plusone -= 10
                L[i] = str(plusone)
        else:
            L[i] = str(plusone)
    return lastone

def printNum(L):
    start = 0
    allZero = False
    while(L[start] == '0'):
        start += 1
        if(start == len(L)):
            allZero = True
            break
    if(not allZero):
        for i in range(start, len(L)):
            print("%c" % L[i], end='')
        print('')

def print1toMax2(num):
    if(num <= 0):
        return False
    numArray = ['0']*num
    for i in range(10):
        numArray[0] = str(i)
        printWithRec(numArray, 0, num)

def printWithRec(L, index, num):
    if(index == num - 1):
        printNum(L)
        return
    for i in range(10):
        L[index+1] = str(i)
        printWithRec(L, index+1, num)

if __name__ == '__main__':
    Print1toMax(2)
    print1toMax2(2)