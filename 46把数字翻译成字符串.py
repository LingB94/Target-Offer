def translate(n):
    if(n < 0):
        return False
    s = str(n)
    cnt = translateCnt(s)
    return cnt

def translateCnt(s):
    length = len(s)
    cnts = [0]*length
    for i in range(length-1, -1, -1):
        cnt = 0
        if(i < length-1):
            cnt = cnts[i+1]
        else:
            cnt = 1
        if(i < length-1):
            digit1 = int(s[i])
            digit2 = int(s[i+1])
            num = digit1*10+digit2
            if(num >= 10 and num <= 25):
                if(i < length-2):
                    cnt += cnts[i+2]
                else:
                    cnt += 1
        cnts[i] = cnt
    return cnts[0]

if __name__ == '__main__':
    x = 12258
    print(translate(12258))