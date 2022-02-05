def split(slist):
    idx=len(slist)//2
    return slist[:idx],slist[idx:]

def merge(left,right,inv):
    res=[]
    while(len(left)>0 and len(right)>0):
        if left[0]<right[0]:
            res.append(left.pop(0))
        elif right[0]<left[0]:
            res.append(right.pop(0))
            inv+=len(left)
        else:
            res.append(left.pop(0))
            #res.append(right.pop(0))
    if len(left)>0: 
        res+=left
    elif len(right)>0: 
        res+=right
    return res,inv

def merge_sort(nums,inv):
    if len(nums)==1:
        return nums,inv
    left,right=split(nums)
    left,inv=merge_sort(left,inv)
    right,inv=merge_sort(right,inv)
    res,inv= merge(left,right,inv)
    return res,inv

def getInversions(arr, n) :
    if len(arr)==0: return 0
    inv=0
    res,inv=merge_sort(arr,inv)
    return inv 

# Taking inpit using fast I/O.
def takeInput() :
    n = int(input())
    arr = list(map(int, input().split(" ")))
    return arr, n

# Main.
arr, n = takeInput()
print(getInversions(arr, n))