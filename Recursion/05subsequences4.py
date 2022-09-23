# Print number of Subsequence whose sum is k

arr = list(map(int,input().split()))
k = int(input()) 

def subsequencesSum(idx,arr,k,s,n):
    if idx == n :
        if s == k : return 1
        else : return 0

    s += arr[idx]
    l = subsequencesSum(idx+1,arr,k,s,n)

    s -= arr[idx]
    r = subsequencesSum(idx+1,arr,k,s,n)

    return l + r


print(subsequencesSum(0,arr,k,0,len(arr)))
