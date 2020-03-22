class Stack(object):
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, n):
        self.items.append(n)
    def pop(self):
        return self.items.pop()
    def top(self):
        return self.items[-1]
    def depth(self):
        return len(self.items)

class listNode(object):
    def __init__(self, n):
        self.val = n
        self.next = None

def inverse_print1(S):
    s = Stack()
    p = S
    while(p):
        s.push(p.val)
        p = p.next
    while(not s.isEmpty()):
        print(s.pop())

def inverse_print2(S):
    if(S):
        inverse_print2(S.next)
        print(S.val)

if __name__ == '__main__':
    a = listNode(1)
    b = listNode(2)
    c = listNode(3)
    a.next = b
    b.next = c
    inverse_print1(a)
    inverse_print2(a)
