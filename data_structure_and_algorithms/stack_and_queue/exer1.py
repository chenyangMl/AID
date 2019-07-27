'''
定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数。
思路: 利用两个栈来实现，一个栈为原本的栈结构，一个用于同步记录最小值
    这里栈的实现使用数组
'''
class Solution:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, node):
        self.stack.append(node)
        #记录最小值
        if not self.stack:
            self.minStack.append(node)
        else:
            if node <= self.minStack[-1]:
                self.minStack.append(node)

    def pop(self):
        if not self.stack:
            raise ('栈为空')
        if not self.minStack:
            return
        self.minStack.pop(-1)
        return self.stack.pop(-1)

    def top(self):
        if not self.stack:
            return
        return self.stack[-1]

    def min(self):
        # write code here
        if not self.minStack:
            return
        return self.minStack[-1]