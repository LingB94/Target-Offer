def Reorder(L):
    start, end = 0, len(L) - 1
    if(not L):
        return False
    while(start < end):
        if(not isEven(L[start])):
            start += 1
            continue
        if(isEven(L[end])):
            end -= 1
            continue
        L[start], L[end] = L[end], L[start]
    return L

def isEven(num):
    return (num&1 == 0)

if __name__ == '__main__':
    l = [1,2,3,4,5]
    print(Reorder(l))