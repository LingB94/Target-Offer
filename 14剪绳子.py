def cutRope1(length):
    if(length < 1 or float(length) != length):
        return False
    if(length == 1):
        return 0
    if(length == 2):
        return 1
    if(length == 3):
        return 2
    maxProduct = [0]*(length+1)
    maxProduct[1], maxProduct[2], maxProduct[3] = 1, 2, 3
    for i in range(4,length+1):
        maxProduct[i] = max([maxProduct[j]*maxProduct[i-j] for j in range(1, i//2+1)])
    return maxProduct[length]

def cutRope2(length):
    if(length < 1 or float(length) != length):
        return False
    if(length == 1):
        return 0
    if(length == 2):
        return 1
    if(length == 3):
        return 2
    timesOf3 = length // 3
    #此时不应剪最后一段长度为3的绳子，因3*1 < 2*2
    if(timesOf3 * 3 == length - 1):
        timesOf3 -= 1
    timesOf2 = (length - timesOf3 * 3)/2
    return pow(3, timesOf3) *pow(2, timesOf2)

if __name__ == '__main__':
    print(cutRope1(5))
    print(cutRope2(5))


