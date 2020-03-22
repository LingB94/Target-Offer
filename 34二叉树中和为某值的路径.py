class TreeNode(object):
    def __init__(self, n):
        self.val = n
        self.lchild = None
        self.rchild = None

def findPath(T, distance):
    if(not T):
        return False
    result = []
    path = [T]
    pathSum = [T.val]
    dfs(T, path, pathSum, distance, result)
    return result

def dfs(T, path, pathSum, distance, result):
    if(not T.lchild and not T.rchild):
        if(pathSum[-1] == distance):
            result.append([p for p in path])

    if(T.lchild):
        path.append(T.lchild)
        pathSum.append(pathSum[-1] + T.lchild.val)
        dfs(T.lchild, path, pathSum, distance, result)
    if(T.rchild):
        path.append(T.rchild)
        pathSum.append(pathSum[-1] + T.rchild.val)
        dfs(T.rchild, path, pathSum, distance, result)
    path.pop()
    pathSum.pop()

def printPath(l):
    for i in l:
        print(i.val, end = ' ')

if __name__ == '__main__':
    pNode1 = TreeNode(10)
    pNode2 = TreeNode(5)
    pNode3 = TreeNode(12)
    pNode4 = TreeNode(4)
    pNode5 = TreeNode(7)

    pNode1.lchild = pNode2
    pNode1.rchild = pNode3
    pNode2.lchild = pNode4
    pNode2.rchild = pNode5
    result = findPath(pNode1, 22)
    for i in result:
        printPath(i)
        print('')
