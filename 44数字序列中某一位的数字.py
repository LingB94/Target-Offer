def countstep(n):
    assert n >= 0, 'n must be an integer beq 0'
    digits = 1
    while(True):
        total = digits * bitsOfdigits(digits)
        if(total > n):
            return specificstep(n, digits)
        else:
            n -= total
            digits += 1

def bitsOfdigits(n):
    if(n == 1):
        return 10
    num = 9*pow(10,n-1)
    return num

def specificstep(n, digits):
    if(digits == 1):
        number = n//digits
    else:
        number = n//digits + pow(10, digits-1)
    step = n % digits
    return str(number)[step]

if __name__ == '__main__':
    print(countstep(1001))

