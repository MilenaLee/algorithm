class Solution(object):
    def dfs(self, candidates, index, target, path, res):        
        if target< 0:
            return
        
        if target == 0:
            res.append(path)
            return
        
        for i in range(index,len(candidates)):
            self.dfs(candidates,i,target-candidates[i],path+[candidates[i]], res)
    
    
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        res = []
        candidates.sort()
        self.dfs(candidates, 0, target, [], res)      
        
        return res