'''
实现二叉树的深度优先遍历
'''

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class TreeToSequence:
    def __init__(self):
        self.pres=[]
        self.mid=[]
        self.back=[]

    def convert(self, root):
        pre = self.pre_order(root)
        mid = self.mid_order(root)
        back =self.back_order(root)
        res = []
        res.append(pre)
        res.append(mid)
        res.append(back)
        return res

    def pre_order(self,root):
        if not root:
            return
        self.pres.append(root.val)
        self.pre_order(root.left)
        self.pre_order(root.right)
        return self.pres

    def mid_order(self,root):
        if not root:
            return
        self.mid_order(root.left)
        self.mid.append(root.val)
        self.mid_order(root.right)
        return self.mid

    def back_order(self,root):
        if not root:
            return
        self.back_order(root.left)
        self.back_order(root.right)
        self.back.append(root.val)
        return self.back


