def findNumsOnce(l):
    if(not l or len(l)<2):
        return False
    xorResult = 0
    for i in l:
        xorResult ^= i
    onePos = getOnePos(xorResult)
    a, b = 0, 0
    for i in l:
        if(isOne(i, onePos)):
            a ^= i
        else:
            b ^= i
    return [a, b]

def getOnePos(n):
    pos = 0
    while(n&1 == 0):
        n = n>>1
        pos += 1
    return pos

def isOne(n, pos):
    return (n>>pos)&1

def findNumOnce(l):
    if(not l or len(l)<4):
        return False
    bitSum = [0]*32
    for i in l:
        bitMask = 1
        for j in range(31,-1,-1):
            if(i&bitMask == 1):
                bitSum[j] += 1
            bitMask = bitMask << 1
    result = 0
    for i in bitSum:
        result = result << 1
        result += (i%3)
    return result

if __name__ == '__main__':
    l = [2,4,3,6,3,2,5,5]
    print(findNumsOnce(l))
    l1 = [2,3,3,2,1,3,2,4,4,4]
    print(findNumOnce(l1))