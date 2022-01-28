class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows<=0: return []
        res=[[1]]
        numRows-=1
        while(numRows>0):
            temp=[1]
            if len(res[-1])>=2:
                for i in range(len(res[-1])-1):
                    temp.append(res[-1][i]+res[-1][i+1])
            temp.append(1)
            res.append(temp)
            numRows-=1
        return res
        