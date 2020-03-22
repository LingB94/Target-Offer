def BiPlus(a, b):
    maxb = 2**32
    while(b != 0):
        if(b == maxb):
            return a^(-1)*maxb
        sum = a^b
        carry = (a&b)<<1
        a = sum
        b = carry
    return sum

if __name__ == '__main__':
    print(BiPlus(5,-1))