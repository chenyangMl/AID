'''
二叉树的层次遍历。

层次遍历并打印行信息，这里需要两个变量。

'''

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Queue1():
    #数组实现队列,先进先出
    def __init__(self):
        self.items = []
    def push(self,val):
        if not val:
            return
        self.items.append(val)

    def pop(self):
        if self.size() <=0:
            return
        return self.items.pop(0)

    def size(self):
        return len(self.items)

class TreePrinter:
    def printTree(self, root):
        # write code here
        return self.bfs_order(root)

    def bfs_order(self,root):
        '''
        实现二叉树从左到右的打印
        初始化一个队列
        last: 表示正在打印的当前行的最右节点
        nlast: 表示下一行的最右节点
        1: 初始化时，令last和nlast都等于root节点。
        '''
        res = []
        queue = Queue1()
        last = root
        nlast = root
        queue.push(root)
        eles = []
        line =0
        while queue.size() !=0 :
            cur = queue.pop()
            eles.append(cur.val)
            if cur.left:
                queue.push(cur.left)
                nlast = cur.left
            if cur.right:
                queue.push(cur.right)
                nlast = cur.right

            if cur == last:
                # 说明二叉树该换行了
                last = nlast
                res.append(eles)
                line +=1
                eles = []

        return res

    # def bfs_order_z(self,root):
    #     #定义一个队列
    #     res = []
    #
    #     queue = Queue1()
    #     queue.push(root)
    #     eles = []
    #     n = 1
    #     last = root
    #     nlast = root
    #     while queue.size() !=0:
    #         cur = queue.pop()
    #         eles.append(cur.val)
    #
    #         if n % 2 !=0:
    #             #遍历奇数行的所有元素
    #
    #             if cur.right:
    #                 queue.push(cur.right)
    #                 nlast = cur.right
    #             if cur.left:
    #                 queue.push(cur.left)
    #                 nlast = cur.left
    #
    #         else:
    #             #遍历偶数行的所有元素
    #
    #             if cur.left:
    #                 queue.push(cur.left)
    #                 nlast =cur.left
    #
    #             if cur.right:
    #                 queue.push(cur.right)
    #                 nlast = cur.right
    #
    #         if cur == last:
    #
    #             res.append(eles)
    #             last = nlast
    #             eles = []
    #             n +=1
    #
    #     return res


if __name__ == '__main__':
    arr = {132,11,375,625,225,416}
    from bin_tree import BinTree
    btree = BinTree()
    btree.add(132)
    btree.add(11)
    btree.add(375)
    btree.add(625)
    btree.add(225)
    btree.add(416)
    print(TreePrinter().bfs_order(btree.root))
    print(TreePrinter().bfs_order_z(btree.root))