class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==0: return 0
        prev_maxsum=nums[0]
        maxsum=nums[0]
        for idx in range(1,len(nums)):
            curr_maxsum=max(prev_maxsum,0) + nums[idx]
            maxsum = max(curr_maxsum, maxsum)
            prev_maxsum=curr_maxsum
        return maxsum
        