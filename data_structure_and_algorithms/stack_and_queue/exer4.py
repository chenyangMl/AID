'''
请编写一个程序，按升序对栈进行排序（即最大元素位于栈顶），要求最多只能使用一个额外的栈存放临时数据，但不得将元素复制到别的数据结构中。

给定一个int[] numbers(C++中为vector&ltint>)，其中第一个元素为栈顶，请返回排序后的栈。请注意这是一个栈，意味着排序过程中你只能访问到第一个元素。

测试样例：
[1,2,3,4,5]

返回：[5,4,3,2,1]
'''
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

class TwoStacks:
    def __init__(self):
        #申请一栈用于辅助排序
        self.temp = Stack()
        self.nums = Stack()

    def twoStacksSort(self, numbers):
        # 这里的numbers不是stack对象，先将其元素添加到stack中
        for ele in numbers:
            self.nums.push(ele)

        # while self.nums.size() !=0:
        #     print(self.nums.pop())

        while self.nums.size() != 0:
            cur_ele = self.nums.pop()
            # 和 辅助栈中栈顶元素比较，如果

            if self.temp.size() == 0:
                # 先将第一个元素添加到辅助栈中
                self.temp.push(cur_ele)
                continue

            while self.temp.size() != 0:
                #遍历比较辅助栈中的元素和cur_ele
                if self.temp.size() ==0:
                    break
                tem_ele = self.temp.pop()

                if cur_ele > tem_ele:
                    # 如果cur_ele 大于辅助栈中弹出元素，则将辅助栈元素压入到nums栈中.
                    self.nums.push(tem_ele)
                    self.temp.push(cur_ele)
                    break
                else:
                    # 如果当前元素小于辅助栈中弹出的元素，则将cur_ele入栈.并结束循环
                    self.temp.push(tem_ele)
                    self.temp.push(cur_ele)
                    break

        while self.temp != 0:
            self.nums.push(self.temp.pop())
        return self.nums

if __name__ == '__main__':
    num = [5,4,3,2,1]
    print(TwoStacks().twoStacksSort(num))

