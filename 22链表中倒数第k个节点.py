class listNode(object):
    def __init__(self, n):
        self.val = n
        self.next = None

def findLastK(head, k):
    if(k <= 0 or head.next == None):
        return False
    p1 = head.next
    p2 = head.next
    step = 0
    while(p1):
        p1 = p1.next
        step += 1
        if(step > k):
            p2 = p2.next
    if(step < k):
        return False
    else:
        return p2

if __name__ == '__main__':
    h = listNode(0)
    a = listNode(1)
    b = listNode(2)
    c = listNode(3)
    d = listNode(4)
    e = listNode(5)
    f = listNode(6)
    h.next = a
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    print(findLastK(h, 6).val)