import numpy as np
class Solution:
    def swap(self,a,b):
        temp=a
        a=b
        b=temp
        return a,b

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)==0: return []
        if len(nums)==1: return nums
        l=len(nums)
        if nums[-2]<nums[-1]:
            nums[-1],nums[-2]=self.swap(nums[-1],nums[-2])
            return
        for idx in range(len(nums)-2,-1,-1):
            if nums[idx]<nums[idx+1]:
                key=nums[idx]
                s=sorted(set(nums[idx:]))[sorted(set(nums[idx:])).index(key)+1]
                print(s)
                sidx=nums[idx:].index(s)
                del nums[idx+sidx]
                print(nums)
                nums[idx:]=sorted(nums[idx:])
                print(nums)
                if idx==0: 
                    nums[:0]=[s] 
                else:
                    #nums=nums[:idx]+[s]+nums[idx:]
                    nums.insert(idx,s)
                return
        nums.reverse()
        
        
        
        
                
                
        
            
        
        
        
        