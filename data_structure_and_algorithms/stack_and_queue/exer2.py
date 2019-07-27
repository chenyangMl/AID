'''
编写一个类,只能用两个栈结构实现队列,支持队列的基本操作(push，pop)。
给定一个操作序列ope及它的长度n，其中元素为正数代表push操作，为0代表pop操作，保证操作序列合法且一定含pop操作，请返回pop的结果序列。
测试样例：
[1,2,3,0,4,0],6
返回：[1,2]
'''
class Stack():
    def __init__(self):
        self.items = []

    def push(self,node):
        self.items.append(node)

    def pop(self):
        if self.items:
            return self.items.pop()

    def size(self):
        return len(self.items)

class TwoStack:
    def __init__(self):
        self.stackPush = Stack()
        self.stackPop = Stack()

    def twoStack(self, ope, n):
        # write code here
        res = []
        for op in ope:
            if op:
                #执行入队操作
                self.stackPush.push(op)
            elif op == 0:
                #执行出队操作
                # 必须保证stackPop为空，必须将stackPush所有元素都倒入到stackPop中
                if self.stackPop.size()==0:
                    while self.stackPush.size()!=0:
                        self.stackPop.push(self.stackPush.pop())
                # 出队
                res.append(self.stackPop.pop())
                # 再将剩余元素倒回到stackPush中
                while self.stackPop.size()!=0:
                    self.stackPush.push(self.stackPop.pop())
        return res

if __name__ == '__main__':
    ope = [1,2,3,0,4,0]
    length = 6
    print(TwoStack().twoStack(ope,length))
