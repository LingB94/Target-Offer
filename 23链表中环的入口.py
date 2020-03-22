class listNode(object):
    def __init__(self, n):
        self.val = n
        self.next = None

def existCircle(head):
    if(not head.next):
        return False
    pFast = head.next
    pSlow = head
    while(pFast != pSlow and pFast):
        pFast = pFast.next.next
        pSlow = pSlow.next
    if(not pFast):
        return False
    else:
        return pFast

def circleNodes(head):
    if(not existCircle(head)):
        return False
    else:
        anchor = existCircle(head)
        p = anchor.next
        cnt = 1
        while(p != anchor):
            p = p.next
            cnt += 1
        return cnt

def findEntry(head):
    if(not existCircle(head)):
        return False
    k = circleNodes(head)
    p1, p2 = head, head
    step = 0
    while(step < k):
        p1 = p1.next
        step += 1
    while(p1 != p2):
        p1 = p1.next
        p2 = p2.next
    return p1

if __name__ == '__main__':
    h = listNode(0)
    a = listNode(1)
    b = listNode(2)
    c = listNode(3)
    d = listNode(4)
    e = listNode(5)
    h.next = a
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = c
    print(findEntry(h).val)