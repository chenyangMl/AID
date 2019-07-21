class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution():
    # 重构二叉树
    def reConstructBinaryTree(self, pre, tin):
        if len(pre) == 0 or len(tin) == 0:
            return None
        rootNode = TreeNode(pre[0])
        root_idx =  tin.index(pre[0])
        rootNode.left = self.reConstructBinaryTree(pre[1:root_idx+1], tin[:root_idx])
        rootNode.right = self.reConstructBinaryTree(pre[root_idx+1:],tin[root_idx+1:])
        return rootNode


if __name__ == '__main__':
    # 测试，[10, 5, 3, 2, 4, 6]的前序和中序序列如下
    from binary_tree import BinTree
    pre = [10, 5, 2, 4, 3, 6]
    tin = [2, 5, 4, 10, 6, 3]
    rootNode = Solution().reConstructBinaryTree(pre,tin)
    print('重构结果的层次遍历结果:',BinTree().layer_order(rootNode))