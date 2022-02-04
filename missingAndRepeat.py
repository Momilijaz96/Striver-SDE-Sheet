#NOT WORKING!
import math
import numpy as np
import cmath
from decimal import Decimal
def missingAndRepeating(arr, n):
    A=list(map(float,arr))
    C1=Decimal(math.factorial(n))
    C2=Decimal(np.prod(A))
    Asum=float(sum(A))
    Tsum=float(sum(np.arange(n+1,dtype=float)))
    K=Decimal(Tsum-Asum)
    d=Decimal(1)/(C1-C2)
    y=((C2)*d*K)
    y=float(y)
    x=(float(K)+(y))
    return int(np.round(x)),int(np.round(y))


    


