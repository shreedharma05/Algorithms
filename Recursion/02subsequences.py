def subSequence(i,arr,n,res):
    if i >= n:
        print(res)
        return
    res.append(arr[i])
    subSequence(i+1,arr,n,res)
    res.pop()
    # res.remove(arr[i])
    subSequence(i+1,arr,n,res)

arr = list(map(int, input().split()))
n = len(arr)
subSequence(0,arr,n,[])

