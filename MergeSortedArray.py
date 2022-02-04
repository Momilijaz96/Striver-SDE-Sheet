class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m==0: 
            nums1[0:]=nums2
            return
        if n==0: 
            return
        #nums1[m:]=nums2
        #nums1.sort()
        m_idx=0 #index of nums1 goes upto m
        n_idx=0
        temp=[]
        while(m_idx<m and n_idx<n):
            n1=nums1[m_idx]
            n2=nums2[n_idx]
            if n1==n2:
                temp.append(n1)
                temp.append(n2)
                m_idx+=1
                n_idx+=1
            elif n1<n2:
                temp.append(n1)
                m_idx+=1
            elif n2<n1:
                temp.append(n2)
                n_idx+=1
        if m_idx<m: temp+=nums1[m_idx:m]
        elif n_idx<n: temp+=nums2[n_idx:]
        print(temp)
        nums1[0:]=temp
        
            
            
            