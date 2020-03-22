class listNode(object):
    def __init__(self, n):
        self.val = n
        self.next = None

def reversedList(L):
    if(L.next == None or not L):
        return False
    p = L.next
    pPrev = None
    reversedHead = listNode(0)
    while(p):
        pPost = p.next
        if(pPost == None):
            reversedHead.next = p
        p.next = pPrev
        pPrev = p
        p = pPost
    return reversedHead

if __name__ == '__main__':
    head = listNode(-1)
    a = listNode(1)
    b = listNode(2)
    c = listNode(3)
    head.next = a
    a.next = b
    b.next = c
    p = reversedList(head)
    while(p):
        print(p.val)
        p = p.next

