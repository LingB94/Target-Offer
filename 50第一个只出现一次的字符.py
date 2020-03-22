def firstNoRepeatingChar(s):
    if(not s):
        return False
    Table = {}
    for i in s:
        if(Table.get(i)):
            Table[i] += 1
        else:
            Table[i] = 1
    for i in s:
        if(Table[i] == 1):
            return i
    return -1

if __name__ == '__main__':
    s = 'abaccdeff'
    print(firstNoRepeatingChar(s))