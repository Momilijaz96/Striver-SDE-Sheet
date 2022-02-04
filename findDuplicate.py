class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if len(nums)==1: return None
        if len(nums)==2 and nums[0]==nums[1]: return nums[0]
        nums.sort()
        for idx in range(1,len(nums)):
            if nums[idx]-nums[idx-1]==0:
                return nums[idx]