class Solution:
    
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums)==0: return []
        if len(nums)==1: return nums
        elem=0
        cnta=0
        cntb=0
        a=None
        b=None
        
        for n in nums:
            
            if n==a:
                cnta+=1
            elif n==b:
                cntb+=1
            elif cnta==0:
                a=n
                cnta+=1
            elif cntb==0:
                b=n
                cntb+=1
            
            else:
                cnta-=1
                cntb-=1
                
        #Check if it is majority element
        cnta=0
        cntb=0
        for n in nums:
            if n==a:
                cnta+=1
            if n==b:
                cntb+=1
        res=[]
        if cnta>len(nums)/3:
            res.append(a)
        if cntb>len(nums)/3 and a!=b:
            res.append(b)
        return res
            