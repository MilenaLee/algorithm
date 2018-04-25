class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = [0] + nums
        self.fenwick = [0 for _ in range(len(nums) + 1)]
        
        for i, num in enumerate(nums):
            idx = i + 1
            while idx < len(self.fenwick):
                self.fenwick[idx] += num
                idx += (idx & -idx)

                
    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        i += 1
        update_value = val - self.nums[i]
        self.nums[i] = val

        while i < len(self.fenwick):
            self.fenwick[i] += update_value
            i += (i & -i)
        
        
    def _sumRange(self, i):
        ret = 0
        while i > 0:
            ret += self.fenwick[i]
            i &= (i-1)
        return ret

    
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        i, j = i, j+1
        return self._sumRange(j) - self._sumRange(i)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)