'''
解题思路
假设需要替换str中的空格为%20
1: 遍历初始的字符串，确定空格数量。
2: 替换后的字符长度为len(str)+空格数*3,
3: 根据字符长度进行对应位置的字符填值即可.
'''

class Replacement():
    def replaceSpace(self,iniStr):
        return iniStr.replace(' ', '%20')

    def replaceSpace1(self,iniStr):
        ini_n = len(iniStr)
        space_n = 0
        for val in iniStr:
            if val ==" ":
                space_n+=1
        total_n = ini_n + space_n * 3
        string = ''
        for i in range(total_n):
            pass