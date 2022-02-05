def getInversions(arr, n) :
    if len(arr)==0: return 0
    m=min(arr)
    X=max(arr)
    midx=argmin(arr)
    Xidx=argmax(arr)
    inv=len(arr[Xidx+1:])+len(arr[:midx])
    if Xidx<midx: inv-=abs(Xidx-midx)
    return inv

# Taking inpit using fast I/O.
def takeInput() :
    n = int(input())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n

# Main.
arr, n = takeInput()
print(getInversions(arr, n))