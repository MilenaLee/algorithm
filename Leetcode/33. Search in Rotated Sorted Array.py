class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        if not nums:
            return -1
        
        # 0. find minimum value index of nums
        start, end = 0, len(nums)-1
        pivot = -1
        
        while start <= end:
            mid = (start+end)//2
            if nums[mid] < nums[0]:
                pivot = mid
                end = mid -1
            else:
                start = mid + 1        
        
        # 1. compare target and choose start and end index of binary search
        if pivot == -1:
            start, end = 0, len(nums) -1
        elif target >= nums[0]:
            start, end = 0, pivot - 1
        else:
            start, end = pivot, len(nums) - 1
        
        res = -1
        print(pivot)
        
        while start <= end:
            mid = (start+end)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid -1
            else:
                start = mid + 1  
        
        return res
