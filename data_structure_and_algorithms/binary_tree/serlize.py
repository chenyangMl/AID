'''
首先我们介绍二叉树先序序列化的方式，假设序列化的结果字符串为str，初始时str等于空字符串。
先序遍历二叉树，如果遇到空节点，就在str的末尾加上“#!”，“#”表示这个节点为空，节点值不存在，
当然你也可以用其他的特殊字符，“!”表示一个值的结束。如果遇到不为空的节点，假设节点值为3，
就在str的末尾加上“3!”。现在请你实现树的先序序列化。

给定树的根结点root，请返回二叉树序列化后的字符串。
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

class TreeToString:

    def toString(self, root):
        # write code here
        stack = Stack()
        string = ''
        if not root:
            return
        stack.push(root)
        while stack.size() != 0:
            cur_node = stack.pop()
            string+=str(cur_node.val)+'!'
            if cur_node.right is not None:
                stack.push(cur_node.right)
            else:
                string+='#!'

            if cur_node.left is not None:
                stack.push(cur_node.left)
            else:
                string+='#!'
        return string