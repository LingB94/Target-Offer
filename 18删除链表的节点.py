class listNode(object):
    def __init__(self, n):
        self.val = n
        self.next = None

def quickDelete(head, i):
    if(not head):
        return False
    if(i.next):
        pnext = i.next
        i.val = pnext.val
        i.next = pnext.next
        del pnext
    else:
        p = head
        while(p.next != i and p):
            p = p.next
        if(not p):
            return False
        p.next = None
        del i

if __name__ == '__main__':
    head = listNode(-1)
    a = listNode(1)
    # b = listNode(2)
    # c = listNode(3)
    head.next = a
    # a.next = b
    # b.next = c
    p = head.next
    while(p):
        print(p.val)
        p = p.next
    quickDelete(head, a)
    p = head.next
    while (p):
        print(p.val)
        p = p.next




