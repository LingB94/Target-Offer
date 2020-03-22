class TreeNode(object):
    def __init__(self, n):
        self.val = n
        self.lchild = None
        self.rchild = None

def depth(T):
    if(not T):
        return 0
    left = depth(T.lchild)
    right = depth(T.rchild)
    if(left>right):
        return 1+left
    else:
        return 1+right

if __name__ == '__main__':
    Node1 = TreeNode(1)
    Node2 = TreeNode(2)
    Node3 = TreeNode(3)
    Node4 = TreeNode(4)
    Node5 = TreeNode(5)
    Node6 = TreeNode(6)
    Node7 = TreeNode(7)

    Node1.lchild = Node2
    Node1.rchild = Node3
    Node2.lchild = Node4
    Node2.rchild = Node5
    Node3.rchild = Node6
    Node5.lchild = Node7
    print(depth(Node1))