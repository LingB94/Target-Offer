class TreeNode(object):
    def __init__(self, n):
        self.val = n
        self.lchild = None
        self.rchild = None

def findKinTree(T,k):
    if(not T):
        return False
    result = []
    TreeToList(T, result)
    return result[k-1]

def TreeToList(T, result):
    if(not T):
        return None
    if(T.lchild):
        TreeToList(T.lchild, result)
    result.append(T.val)
    if(T.rchild):
        TreeToList(T.rchild, result)

if __name__ == '__main__':
    Node1 = TreeNode(5)
    Node2 = TreeNode(3)
    Node3 = TreeNode(7)
    Node4 = TreeNode(2)
    Node5 = TreeNode(4)
    Node6 = TreeNode(6)
    Node7 = TreeNode(8)

    Node1.lchild = Node2
    Node1.rchild = Node3
    Node2.lchild = Node4
    Node2.rchild = Node5
    Node3.lchild = Node6
    Node3.rchild = Node7
    print(findKinTree(Node1, 3))