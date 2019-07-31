'''
请用非递归方式实现二叉树的先序、中序和后序的遍历打印。
给定一个二叉树的根结点root，请依次返回二叉树的先序，中序和后续遍历(二维数组的形式)。

'''
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Stack():
    def __init__(self):
        self.items =[]
    def push(self,val):
        self.items.append(val)
    def pop(self):
        if not self.items:
            return
        return self.items.pop()
    def top(self):
        return self.items[-1]
    def size(self):
        return len(self.items)

class TreeToSequence:

    def convert(self, root):
        pre = self.pre_non_recursive(root)
        mid = self.mid_non_recursive(root)
        back = self.back_noe_recursive(root)
        return [pre,mid,back]

    def pre_non_recursive(self,root):
        '''
        先序遍历实现思路:
        1 初始化一个栈结构stack
        2 然后将头节点root压入stack中
        3 每次从stack中弹出栈顶元素，即为cur,并打印cur值。
          如果cur的右孩子不为空，将cur的右孩子压入栈中，
          最后如果cur的左孩子不为空，将cur的左孩子压入栈中。
        4 不断重复步骤3,直到stack为空，全部过程结束
        '''
        #定义一个栈,实现先序遍历

        stack = Stack()
        res = []
        if not root:
            return
        stack.push(root)
        while stack.size() != 0:
            cur_node = stack.pop()
            res.append(cur_node.val)
            if cur_node.right is not None:
                stack.push(cur_node.right)
            if cur_node.left is not None:
                stack.push(cur_node.left)
        return res

    def mid_non_recursive(self,root):
        """
        1 初始化一个栈结构stack, 一个变量cur,初始时cur等于头节点root
        2 先把cur节点压入栈中，对以cur节点为头的整颗子树来说，依次把整颗
        树的左边界压入栈中，即不断令cur=cur.left,然后重复步骤2

        3 不断重复步骤2，直到发现cur为空，此时从stack中弹出一个节点，即为node
        打印node的值，并令cur = node.right,然后继续重复步骤2
        4 当stack为空并且cur为空时，整个过程结束
        """
        stack = Stack()
        res = []
        if not root:
            return
        cur = root
        stack.push(cur)

        while stack.size()!=0 or cur is not None:

            if cur is not None:
                cur = cur.left
                #如果当前节点不为空，一直添加节点左孩子
                if not cur:
                    continue
                stack.push(cur)
            else:

                #如果cur为空则从栈顶弹出一个元素,并令cur = cur.right
                node = stack.pop()
                res.append(node.val)
                cur = node.right
                if not cur:
                    continue
                stack.push(cur)

        return res


    def back_noe_recursive(self,root):
        """
        1 初始化两个栈,stack1、stack2,然后将头节点压入stack1中。
        2 从stack1中弹出的节点记为cur,然后先把cur的左孩子压入stack1中。
          再将cur的右孩子压入stack1中。
        3 将2过程中所有从stack1中弹出的节点都放入stack2中。
        4 不断重复步骤2和3，直到s1为空，过程停止。
        5 弹出stack2中元素，即为后序遍历顺序。
        """
        res = []
        stack1 = Stack()
        stack2 = Stack()
        if not root:
            return
        stack1.push(root)
        while stack1.size()!= 0:
            cur = stack1.pop()
            if cur.left is not None:
                stack1.push(cur.left)
            if cur.right is not None:
                stack1.push(cur.right)
            stack2.push(cur)

        while stack2.size()!=0:
            res.append(stack2.pop().val)
        return res

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
    print(TreeToSequence().pre_non_recursive(btree.root))
    print(TreeToSequence().mid_non_recursive(btree.root))
    print(TreeToSequence().back_noe_recursive(btree.root))

