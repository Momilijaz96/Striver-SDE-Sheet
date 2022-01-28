class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if len(matrix)==0: return 0
        zero_row=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    zero_row.append(str(i)+'-'+str(j))
        for idx in zero_row:
            i,j=idx.split('-')
            matrix[int(i)]=[0]*len(matrix[0])
            for row in range(len(matrix)):
                matrix[row][int(j)]=0
            
                    
        
        
        