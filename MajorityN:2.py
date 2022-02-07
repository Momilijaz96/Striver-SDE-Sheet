class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums)==1: return nums[0]
        elem=0
        count=0
        for n in nums:
            if count==0:
                elem=n
            if n==elem:
                count+=1
            else:
                count-=1
        return elem
        
