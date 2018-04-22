class Solution:
    def func(self, st):
        ind, s = 0, st[0]
        ret = ""
        for index, ss in enumerate(st):
            if ss == s:
                continue
            else:
                ret = ret + str(index-ind) + str(s)
                ind = index
                s = ss
                
        ret = ret + str(len(st)-ind) + str(s)
                
        return ret
                
        
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n < 2:
            return "1"
        
        s = "1"
        for nn in range(n-1):
            s = self.func(s)
        
        return s
        
