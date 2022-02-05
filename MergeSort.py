def split(slist):
    idx=len(slist)//2
    return slist[:idx],slist[idx:]

def merge(l1,l2):
    res=[]
    while(len(l1)>0 and len(l2)>0):
        if l1[0]<l2[0]:
            res.append(l1.pop(0))
        elif l2[0]<l1[0]:
            res.append(l2.pop(0))
        else:
            res.append(l1.pop(0))
            res.append(l2.pop(0))
    if len(l1)>0: res+=l1
    elif len(l2)>0: res+=l2
    return res
    
def merge_sort(nums):
    if len(nums)==1:
        return nums
    left,right=split(nums)
    left=merge_sort(left)
    right=merge_sort(right)
    return merge(left,right)

if __name__=='__main__':
    x=list(map(int,input().split(' ')))
    print(merge_sort(x))
    