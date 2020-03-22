def nthUglyNum(n):
    if(n <= 0):
        return False
    uglyArray = [1]
    step = 0
    step2, step3, step5 = 0, 0, 0
    while(step < n):
        while(uglyArray[step2]*2 <= uglyArray[-1]):
            step2 += 1
        while(uglyArray[step3] * 3 <= uglyArray[-1]):
            step3 += 1
        while(uglyArray[step5] * 5 <= uglyArray[-1]):
            step5 += 1
        minVal = min(uglyArray[step2]*2, uglyArray[step3]*3, uglyArray[step5]*5)
        uglyArray.append(minVal)
        step += 1
    return uglyArray[-1]

if __name__ == '__main__':
    n = 10
    print(nthUglyNum(n))