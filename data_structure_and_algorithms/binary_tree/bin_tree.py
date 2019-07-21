'''
ADT-Binary tree
'''

class TreeNode():
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class BinTree():
    def __init__(self):
        self.root = None
        self.res = []

    def add(self,val):

        if self.root is None:
            self.root = TreeNode(val)
            return
        newNode = TreeNode(val)
        queue = [self.root]
        while queue:
            curNode = queue.pop(0)
            if curNode.left is None:
                curNode.left = newNode
                return
            else:
                queue.append(curNode.left)

            if curNode.right is None:
                curNode.right = newNode
                return
            else:
                queue.append(curNode.right)

    # 层次遍历,从上往下打印出二叉树的每个节点，同层节点从左至右打印
    def layer_order(self,root):
        if not root:
            return '#'
        queue = [root]
        while queue:
            curNode = queue.pop(0)
            self.res.append(curNode.val)
            if curNode.left is not None:
                queue.append(curNode.left)
            if curNode.right is not None:
                queue.append(curNode.right)
        return self.res

    # 前序序列化二叉树,root->left->right
    def serialize(self,root):
        if not root:
            return '#'
        return str(root.val)+','+str(self.serialize(root.left))+','+\
                str(self.serialize(root.right))
    #前序遍历
    def pre_order(self,root):
        if root is not None:
            self.res.append(root.val)
            self.pre_order(root.left)
            self.pre_order(root.right)
        return self.res


    #中序遍历
    def mid_order(self,root):
        if root is not None:
            self.mid_order(root.left)
            self.res.append(root.val)
            self.mid_order(root.right)
        return self.res

    #后序遍历
    def back_order(self,root):
        if root is not None:
            self.back_order(root.left)
            self.back_order(root.right)
            self.res.append(root.val)
        return self.res


if __name__ == '__main__':
    btree = BinTree()
    btree.add(10)
    btree.add(5)
    btree.add(3)
    btree.add(2)
    btree.add(4)
    btree.add(6)

    print('层次遍历结果:',BinTree().layer_order(btree.root))
    print('序列化结果:',BinTree().serialize(btree.root))
    print('前序遍历结果:',BinTree().pre_order(btree.root))
    print('中序遍历结果:',BinTree().mid_order(btree.root))
    print('后序遍历结果：',BinTree().back_order(btree.root))