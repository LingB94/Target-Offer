class Stack(object):
    def __init__(self):
        self.__stack = []
    def push(self, n):
        self.__stack.append(n)
    def pop(self):
        if(len(self.__stack) > 0):
            return self.__stack.pop()
        return False
    def top(self):
        if(len(self.__stack) > 0):
            return self.__stack[-1]
        return False
    def isEmpty(self):
        return (len(self.__stack) == 0)

def judgeRight(l1, l2):
    if(not l1 or not l2):
        return False
    if(len(l1) != len(l2)):
        return False
    s = Stack()
    step = 0
    for i in range(len(l1)):
        s.push(l1[i])
        if(l1[i] == l2[step]):
            s.pop()
            step += 1
    while(step < len(l2) and s.top() == l2[step] and not s.isEmpty()):
        step += 1
        s.pop()
    if(step == len(l2)):
        return True
    return False

if __name__ == '__main__':
    pushV = [1, 2, 3, 4, 5]
    popV = [4, 5, 3, 2, 1]
    popVF = [4, 5, 2, 1, 3]
    print(judgeRight(pushV, popV))
    print(judgeRight(pushV, popVF))





