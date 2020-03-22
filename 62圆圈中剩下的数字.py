def remainNum(n, k):
    if(n<1 or k<1):
        return False
    tmp = 0
    for i in range(1,n+1):
        tmp = (tmp+k) % i
    return tmp+1

if __name__ == '__main__':
    print(remainNum(5, 2))