import math
import numpy as np
class Solution:
    #Un optimized recursive solution -Time limit exceed
    def count_path(self,R,D,paths):
        if R==0 and D==0:
            paths+=1
            return paths
        if R>0:
            paths=self.count_path(R-1,D,paths)
        if D>0:
            paths=self.count_path(R,D-1,paths)
        return paths
    
    #Memoization-Dynamic programming
    def count_path_dynamic(self,R,D,paths):
        for d in range(1,D):
            for r in range(1,R):
                paths[d,r]=paths[d-1,r]+paths[d,r-1]
        return paths,paths[D-1,R-1]
    
    def uniquePaths(self, m: int, n: int) -> int:
        if m==1 and n==1: return 1
        paths=np.zeros((m,n),dtype=int)
        paths[0,1:]=1
        paths[1:,0]=1
        paths,max_paths= self.count_path_dynamic(n,m,paths)
        print(paths)
        return max_paths
        
        