"""
对于一个字符串，请设计一个算法，只在字符串的单词间做逆序调整，
'也就是说，字符串由一些由空格分隔的部分组成，你需要将这些部分逆序。
给定一个原字符串A和他的长度n，请返回逆序后的字符串。

解题思路：
    1.首先实现一个能够将局部字符串所有字符逆序的函数f
    2.对整个句子使用一次f方法
    3.再对局部每个词使用一次f方法

    eg: Tom loves Jerry
        整句逆序: yrreJ sevol moT
        在局部逆序: Jerry loves Tom
"""
class Reverse:
    def reverseSentence(self, A, n):
        # write code here
        sen = self.reverseWord(A)
        res = []
        for i in sen.split():
            res.append(self.reverseWord(i))
        return ' '.join(res)

    # 局部逆序函数
    # 局部逆序切片方法word[::-1]
    def reverseWord(self,word):
        res = ''
        for i in word:
            res = i + res
        return res


if __name__ == '__main__':
    string = 'Tom loves Jerry'
    print(Reverse().reverseSentence(string,len(string)))