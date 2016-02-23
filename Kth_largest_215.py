# https://leetcode.com/problems/kth-largest-element-in-an-array/

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.compute(nums, len(nums)-k, 0, len(nums)-1)
        
    def compute(self, nums, k, start, end):
        if start >= end:
            return nums[start]
        pivot = start
        i = start + 1
        j = end
        while i <= j:
            if nums[i] < nums[pivot]:
                i += 1
            else:
                self.swap(nums, i, j)
                j -= 1
        i -= 1
        self.swap(nums, start, i)
        if i == k:
            return nums[i]
        elif i > k:
            return self.compute(nums, k, start, i-1)
        else:
            return self.compute(nums, k, i+1, end)
    
    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
