class Solution:
    def binarySearch(self,arr,tgt):
        print(arr)
        idx=len(arr)//2
        if arr[idx]==tgt:
            return True
        elif arr[idx]>tgt and len(arr)>1:
            return self.binarySearch(arr[:idx],tgt)
        elif arr[idx]<tgt and len(arr)>1:
            return self.binarySearch(arr[idx:],tgt)
        
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix)==1 and len(matrix[0])==1:
            return matrix[0][0]==target
        
        #Flatten matrix to make list
        for idx in range(1,len(matrix)):
            matrix[0]+=matrix[idx]
        matrix=matrix[0]
        print(matrix)
        #Perform binary search
        return self.binarySearch(matrix,target)
    