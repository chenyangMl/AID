"""

解题思路:
    1.判断str1,与str2的长度是否相等
    2.如果长度相等，生成str1+str1的大字符串
    3.判读str2是否包含在这个大字符中
"""
class Rotation:
    def chkRotation(self, A, lena, B, lenb):
        # write code here
        flag = False
        if not A or not B:
            return
        if lena == lenb:
            strAA = A+A
            if B in strAA:
                flag = True
        return flag