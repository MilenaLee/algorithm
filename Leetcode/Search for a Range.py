
class Solution(object):
    def minBinary(self, nums, target):
        start, end = 0, len(nums) - 1
        sol = None

        while start<=end:
            mid = (start+end)//2
            print(nums[mid])
            if nums[mid] < target:
                start = mid + 1
            else: # nums[mid] >= target
                end = mid - 1
                if nums[mid] == target:
                    sol = mid

        return sol


    def maxBinary(self, nums, target):
        start, end = 0, len(nums) - 1
        sol = None

        while start<=end:
            mid = (start+end)//2
            if nums[mid] <= target:
                start = mid + 1
                if nums[mid] == target:
                    sol = mid  
            else: # nums[mid] >= target
                end = mid - 1
        return sol


    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mini = self.minBinary(nums, target)

        if mini is None:
            return [-1,-1]

        maxi = self.maxBinary(nums, target)

        return [mini, maxi]

"""
def searchRange(self, nums, target):
    def search(lo, hi):
        if nums[lo] == target == nums[hi]:
            return [lo, hi]
        if nums[lo] <= target <= nums[hi]:
            mid = (lo + hi) / 2
            l, r = search(lo, mid), search(mid+1, hi)
            return max(l, r) if -1 in l+r else [l[0], r[1]]
        return [-1, -1]
    return search(0, len(nums)-1)

#https://leetcode.com/problems/search-for-a-range/discuss/14707/9-11-lines-O(log-n)
"""
