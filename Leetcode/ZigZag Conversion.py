class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        if not s:
            return ""
        
        if numRows == 1 or len(s) <= numRows:
            return s
        
        ans = [""] * numRows
        index = 0
        indexAdd = 1
        
        for ch in s:
            ans[index] += ch
            
            if index == 0:
                indexAdd = 1
            elif index == numRows - 1:
                indexAdd = -1
            
            index += indexAdd
          
        res = ""
        
        for i in range(numRows):
            res += ans[i]
            
        return res