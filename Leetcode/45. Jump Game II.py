class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) < 2:
            return 0
        
        level, currentMax, i, nextMax = 0, 0, 0, 0
        
        while (currentMax-i+1>0):
            level += 1
            while i <= currentMax:
                nextMax = max(nextMax, nums[i]+i)
                if nextMax >= len(nums)-1:
                    return level
                i += 1
            currentMax = nextMax
        return 0
                    
