# 判断A,B两二叉树结构和元素是否相同
from data_structure_and_algorithms.binary_tree import bin_tree

class Solution():
    def isSameBinTree(self,rootA,rootB):
        if not rootA or not rootB:
            return
        strA = self.serialize(rootA)
        strB = self.serialize(rootB)
        if strB == strA:
            return True
        return False

    def serialize(self,root):
        if not root:
            return '#'
        return str(root.val)+','+str(self.serialize(root.left))+','+\
                self.serialize(root.right)

# 测试
if __name__ == '__main__':
    abt = bin_tree.BinTree()
    abt.add(10)
    abt.add(5)
    abt.add(4)
    abt.add(3)
    abt.add(6)
    abt.add(8)

    bbt = bin_tree.BinTree()
    bbt.add(10)
    bbt.add(5)
    bbt.add(4)
    bbt.add(3)
    bbt.add(6)
    bbt.add(8)

    print(Solution().isSameBinTree(abt.root,bbt.root))