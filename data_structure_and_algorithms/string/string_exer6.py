"""
字符串移位问题：　
对于一个字符串，请设计一个算法，将字符串的长度为len的前缀
平移到字符串的最后。给定一个字符串str和它的长度n，同时给定len，
请返回平移后的字符串。
测试样例：
"ABCDE",5,3
返回："DEABC"

解题思路:
1. 将str[:len]做逆序调整
2. 将str[len:]做逆序调整
3.　整体做逆序调整
"""
class Translation:
    def stringTranslation(self, A, n, len):
        # write code here
        return (A[:len][::-1]+A[len:][::-1] )[::-1]

if __name__ == '__main__':
    # "JXJYAR"
    print(Translation().stringTranslation("RJXJYA",6,1))