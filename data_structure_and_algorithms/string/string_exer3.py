class Transform:
    def chkTransform(self, A, lena, B, lenb):
        # write code here
        flag = False
        if lena != lenb:
            return
        hash_a = self.hashmap(A)
        hash_b = self.hashmap(B)
        if hash_a == hash_b:
            flag = True
        return flag

    def hashmap(self, string):
        dic_a = {}
        for i in string:
            if i in dic_a:
                dic_a[i] += 1
            else:
                dic_a[i] = 0
        return dic_a