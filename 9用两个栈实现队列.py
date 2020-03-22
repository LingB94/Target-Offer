class Stack(object):
    def __init__(self):
        self.__items = []
    def isEmpty(self):
        return self.__items == []
    def push(self, n):
        self.__items.append(n)
    def pop(self):
        return self.__items.pop()
    def top(self):
        return self.__items[-1]
    def depth(self):
        return len(self.__items)

class queue(Stack):
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
    def appendTail(self, n):
        self.stack1.push(n)
    def deleteHead(self):
        if(not self.stack2.isEmpty()):
            return self.stack2.pop()
        else:
            while(not self.stack1.isEmpty()):
                p = self.stack1.pop()
                self.stack2.push(p)
            return self.stack2.pop() if not self.stack2.isEmpty() else None

if __name__ == '__main__':
    q = queue()
    q.appendTail('a')
    q.appendTail('b')
    q.appendTail('c')
    print(q.deleteHead())
    print(q.deleteHead())
    q.appendTail('d')
    print(q.deleteHead())
    print(q.deleteHead())
