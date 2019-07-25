'''
解题思路:
1: 整型变量num,代表'('出现次数与')'出现次数的差值
2: 遍历过程中如果遇到‘('则num++
3: 遍历过程中如果遇到')'则num--
4：在num--过程中，如果num<0,则直接返回False
5:如果没有出现4的情况，则一直遍历
6:遍历完成后，如果num==0返回True,否则返回False
'''

class Parenthesis:
    def chkParenthesis(self, A, n):
        # write code here
        #定义一个变量记录'('和')'出现次数的差值
        num = 0
        flag=True
        for val in A:
            if val =="(":
                num+=1
            elif val ==")":
                num -=1
                if num < 0:
                    flag = False
        if num !=0:
            flag = False
        return flag