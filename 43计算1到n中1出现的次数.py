def count1(n):
    if(n <= 10):
        return 1 if n>=1 else 0
    s = str(n)
    digitCnt = len(s)
    #5位数，计算1到9999的1的个数
    cnt1lower = countTo9(digitCnt-1)
    highestDigit = int(s[0])
    low_part = n - pow(10,highestDigit)
    #计算最高位1出现的次数
    if(highestDigit == 1):
        cnt1highest = low_part+1
    if(highestDigit != 1):
        cnt1highest = (highestDigit-1)*cnt1lower+pow(10,digitCnt-1)
    return cnt1lower+cnt1highest+count1(low_part)

def countTo9(n):
    if(n <= 0):
        return 0
    if(n == 1):
        return 1
    else:
        return pow(10,n-1)+9*countTo9(n-1)

if __name__ == '__main__':
    x = 12345
    print(count1(x))