from fractions import Fraction
def my_pow1(num, expo):
    if(num == 0 and expo == 0):
        return 0
    minus_flag = False
    if(expo < 0):
        expo = (-1) * expo
        minus_flag = True
    i = 0
    result = 1
    while(i < expo):
        result *= num
        i += 1
    if(minus_flag == True):
        result = Fraction(1, result)
    return result

def my_pow2(num, expo):
    if(num == 0):
        return 0
    if(expo == 1):
        return num
    if(expo == -1):
        return Fraction(1, num)
    result = my_pow2(num, expo >> 1)
    result *= result
    if((expo & 0x1) == 1):
        result *= num
    return result

if __name__ == '__main__':
    x, y = 3,-3
    print(my_pow1(x, y))
    print(my_pow2(x, y))