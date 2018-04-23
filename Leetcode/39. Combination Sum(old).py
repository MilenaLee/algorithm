class Solution(object):
    def dfs(self, cur, target, lis):        
        if target - self.c[cur] < 0:
            return
        
        if target - self.c[cur] == 0:
            _lis = lis + [self.c[cur]]
            self.res.append(_lis)
            return
        
        for i in range(cur,len(self.c)):
            _lis = lis + [self.c[cur]]
            self.dfs(i, target-self.c[cur], _lis)
    
    
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        self.res = []
        self.c = sorted(candidates)
        
        for i in range(len(self.c)):
            self.dfs(i, target, [])
            
        return self.res