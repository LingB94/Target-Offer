class listNode(object):
    def __init__(self, n):
        self.val = n
        self.next = None

def MergeList(L1, L2):
    if(not L1):
        return L2
    if(not L2):
        return L1
    p1 = L1.next
    p2 = L2.next
    L = listNode(0)
    L.next = MergeCore(p1, p2)
    return L

def MergeCore(p1, p2):
    l = None
    if(not p1):
       return p2
    elif(not p2):
        return p1
    if(p1.val < p2.val):
        l = p1
        l.next = MergeCore(p1.next, p2)
    else:
        l = p2
        l.next = MergeCore(p1, p2.next)
    return l

if __name__ == '__main__':
    head1 = listNode(-1)
    a1 = listNode(1)
    b1 = listNode(3)
    c1 = listNode(5)
    head1.next = a1
    a1.next = b1
    b1.next = c1
    head2 = listNode(-1)
    a2 = listNode(2)
    b2 = listNode(4)
    c2 = listNode(6)
    head2.next = a2
    a2.next = b2
    b2.next = c2
    L = MergeList(head1, head2)
    while (L):
        print(L.val)
        L = L.next