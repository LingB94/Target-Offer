class listNode(object):
    def __init__(self, n):
        self.val = n
        self.next = None

def firstPublicNode(l1, l2):
    if(not l1 or not l2):
        return False
    length1, length2 = 0, 0
    p1 = l1
    while(p1):
        length1 += 1
        p1 = p1.next
    p2 = l2
    while(p2):
        length2 += 1
        p2 = p2.next
    if(length1 > length2):
        p = l1
        for i in range(length1-length2):
            p = p.next
        p2 = l2
        while(p.val != p2.val):
            p = p.next
            p2 = p2.next
        if(not p):
            return False
        return p
    else:
        p = l2
        for i in range(length2-length1):
            p = p.next
        p1 = l1
        while(p.val != p2.val):
            p1 = p1.next
            p = p.next
        if(not p):
            return False
        return p

if __name__ == '__main__':
    Node1 = listNode(1)
    Node2 = listNode(2)
    Node3 = listNode(3)
    Node4 = listNode(4)
    Node5 = listNode(5)
    Node6 = listNode(6)
    Node7 = listNode(7)

    Node1.next = Node2
    Node2.next = Node3
    Node3.next = Node6
    Node4.next = Node5
    Node5.next = Node6
    print(firstPublicNode(Node1, Node5).val)

