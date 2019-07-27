'''
实现一个栈的逆序，但是只能用递归函数和这个栈本身的pop操作来实现，而不能自己
申请另外的数据结构。给定一个整数数组A即为给定的栈，同时给定它的大小n，请返回逆序后的栈。
测试样例：
[4,3,2,1],4
返回：[1,2,3,4]
'''
class StackReverse:
    def get_bottom_ele(self,A):
        #获取栈底元素
        res = A.pop()
        if len(A) == 0:
            return res
        else:
            last = self.get_bottom_ele(A)
            A.append(res)
            return last

    def reverseStack(self, A, n):
        # write code here
        if len(A) == 0:
            return
        else:
            ele = self.get_bottom_ele(A)
            self.reverseStack(A, len(A))
            A.append(ele)
            return A


if __name__ == '__main__':
    A = [3,2,1]
    print(StackReverse().reverseStack(A,3))

