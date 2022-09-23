# Print only one Subsequence whose sum is k

arr = list(map(int,input().split()))
k = int(input()) 

def subsequencesSum(idx,arr,k,s,n,temp):
    if idx == n :
        if s == k:
            print(temp)
            return True
        return False

    temp.append(arr[idx])
    s += arr[idx]
    if (subsequencesSum(idx+1,arr,k,s,n,temp) == True): return True
    temp.pop()
    s -= arr[idx]
    if (subsequencesSum(idx+1,arr,k,s,n,temp) == True): return True


subsequencesSum(0,arr,k,0,len(arr),[])
