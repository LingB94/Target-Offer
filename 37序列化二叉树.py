class TreeNode(object):
    def __init__(self, n):
        self.val = n
        self.lchild = None
        self.rchild = None

def serialize(T, result):
    if(not T):
        result.append('$')
        return
    result.append(str(T.val))
    serialize(T.lchild, result)
    serialize(T.rchild, result)

def deserialize(l):
    T, step = deserializeCore(l, 0)
    return T

def deserializeCore(l, step):
    if(not l[step].isdigit() or step >= len(l)):
        return None, step+1
    node = TreeNode(int(l[step]))
    step += 1
    node.lchild, step = deserializeCore(l, step)
    node.rchild, step = deserializeCore(l, step)
    return node, step

if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)

    node1.lchild, node1.rchild = node2, node3
    node2.lchild = node4
    node3.lchild, node3.rchild = node5, node6
    seList = []
    serialize(node1, seList)
    print(seList)
    T = deserialize(seList)
    print(T.lchild.val)
