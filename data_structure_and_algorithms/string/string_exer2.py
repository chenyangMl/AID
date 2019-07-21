# 存在漏洞
from data_structure_and_algorithms.binary_tree import bin_tree

class Soultion():
    def isSubBinTree(self,rootA,rootB):
        flag = False
        if not rootA or not rootB:
            return
        strA = self.serialize(rootA)
        strB = self.serialize(rootB)
        if len(strB)< len(strA):
            if strB in strA:
                flag = True
        return flag

    def serialize(self,root):
        res = ""
        if not root:
            return
        queue = [root]
        while queue:
            curNode = queue.pop(0)
            res+= str(curNode.val)
            if curNode.left is not None:
                queue.append(curNode.left)
            if curNode.right is not None:
                queue.append(curNode.right)
        return res


# 测试
if __name__ == '__main__':
    abt = bin_tree.BinTree()
    abt.add(10)
    abt.add(5)
    abt.add(3)
    abt.add(2)
    abt.add(4)
    abt.add(6)

    bbt = bin_tree.BinTree()
    bbt.add(10)
    bbt.add(5)
    bbt.add(3)
    bbt.add(2)

    print(Soultion().isSubBinTree(abt.root,bbt.root))

