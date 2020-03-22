class ClistNode(object):
    def __init__(self, n):
        self.val = n
        self.pnext = None
        self.psibling = None

def copyList(L):
    if(not L):
        return False
    cloneNode(L)
    cloneSibling(L)
    return splitList(L)

def cloneNode(L):
    p = L
    while(p):
        cloneNode = ClistNode(0)
        cloneNode.pnext = p.pnext
        cloneNode.val = p.val
        p.pnext = cloneNode
        p = cloneNode.pnext

def cloneSibling(L):
    p = L
    while(p):
        pclone = p.pnext
        if(p.psibling):
            pclone.psibling = p.psibling.pnext
        p = pclone.pnext

def splitList(L):
    p = L
    cloneHead = p.pnext
    pclone = p.pnext
    p.pnext = pclone.pnext
    p = p.pnext
    while(p):
        pclone.pnext = p.pnext
        pclone = pclone.pnext
        p.pnext = pclone.pnext
        p = p.pnext
    return cloneHead

if __name__ == '__main__':
    node1 = ClistNode(1)
    node2 = ClistNode(3)
    node3 = ClistNode(5)
    node1.pnext = node2
    node2.pnext = node3
    node1.psibling = node3
    cloneHead = copyList(node1)
    print(cloneHead.psibling.val)