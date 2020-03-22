def countNumof1(n):
    cnt = 0
    #python中通过将负数和十六进制的ffffffff做与运算来获得负数的补码
    if(n<0):
        n = n&0xffffffff
    while(n):
        n = n & (n-1)
        cnt += 1
    return cnt

if __name__ == '__main__':
    x = -1
    print(bin(x))
    print(countNumof1(x))