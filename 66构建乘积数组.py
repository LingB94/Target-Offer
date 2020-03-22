def multiply(l):
    if(not l or len(l)<1):
        return False
    length = len(l)
    result = [1]*length
    for i in range(1, length):
        result[i] *= l[i-1]
    tmp = 1
    for i in range(length-2, -1, -1):
        tmp *= l[i+1]
        result[i] *= tmp
    return result

if __name__ == '__main__':
    l = [1,2,3]
    print(multiply(l))