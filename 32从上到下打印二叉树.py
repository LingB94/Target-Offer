from queue import Queue
class TreeNode(object):
    def __init__(self, n):
        self.val = n
        self.lchild = None
        self.rchild = None

def levelTrav(T):
    if(not T):
        return
    q = Queue()
    q.put(T)
    while(not q.empty()):
        p = q.get()
        print(p.val, end = ' ')
        if(p.lchild):
            q.put(p.lchild)
        if(p.rchild):
            q.put(p.rchild)

def levelTrav2(T):
    if(not T):
        return
    q = Queue()
    q.put(T)
    toBeprint, nextlevel = 1, 0
    while(not q.empty()):
        p = q.get()
        print(p.val, end = ' ')
        toBeprint -= 1
        if(p.lchild):
            q.put(p.lchild)
            nextlevel += 1
        if(p.rchild):
            q.put(p.rchild)
            nextlevel += 1
        if(not toBeprint):
            print('')
            toBeprint = nextlevel
            nextlevel = 0

def levelTrav3(T):
    if(not T):
        return
    s1 = [T]
    s2 = []
    level = 0
    while(s1 or s2):
        if(level&1 == 0):
            p = s1.pop()
            print(p.val, end = ' ')
            if(p.lchild):
                s2.append(p.lchild)
            if(p.rchild):
                s2.append(p.rchild)
            if(not s1):
                level += 1
                print('')
        else:
            p = s2.pop()
            print(p.val, end = ' ')
            if(p.rchild):
                s1.append(p.rchild)
            if(p.lchild):
                s1.append(p.lchild)
            if(not s2):
                level += 1
                print('')

if __name__ == '__main__':
    a = TreeNode(8)
    b = TreeNode(6)
    c = TreeNode(10)
    d = TreeNode(5)
    e = TreeNode(7)
    f = TreeNode(9)
    g = TreeNode(11)
    a.lchild = b
    a.rchild = c
    b.lchild = d
    b.rchild = e
    c.lchild = f
    c.rchild = g
    levelTrav3(a)

