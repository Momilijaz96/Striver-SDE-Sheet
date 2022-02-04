import numpy as np
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if len(matrix)==0: return 
        if len(matrix[0])==1: return 
    
        #Transpose
        idx=0
        for l in list(map(list,zip(*matrix))):
            matrix[idx]=l
            idx+=1
            
        print(matrix)
        
        #reverse rows in transposed matrix
        for idx,row in enumerate(matrix):
            print(matrix[idx][::-1])
            matrix[idx]=matrix[idx][::-1]
        print(matrix)   