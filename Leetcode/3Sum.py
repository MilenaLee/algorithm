class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        N = len(nums)
        nums.sort()
        ans = []
        
        for i in range(N-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = N - 1
            while(l < r):
                if nums[i] + nums[l] + nums[r] == 0:
                    ans.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    r -= 1
                    l += 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    l += 1
        
        return ans
    
s = Solution()
s.threeSum([-1, 0, 1, 2, -1, -4, -2 , 0, 0, 2, 2])