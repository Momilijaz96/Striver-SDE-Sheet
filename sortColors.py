class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)==0:
            return
        fmap={0:0,1:0,2:0}
        for n in nums:
            if n==0:
                fmap[0]+=1
            if n==1:
                fmap[1]+=1
            if n==2:
                fmap[2]+=1
        nums[:fmap[0]]=[0]*fmap[0]
        nums[fmap[0]:fmap[0]+fmap[1]]=[1]*fmap[1]
        nums[fmap[0]+fmap[1]:]=[2]*fmap[2]
        