# Print the Subsequences whose sum is k
arr = list(map(int,input().split()))
k = int(input()) 

def subsequencesSum(idx,arr,k,s,n,temp):
    if idx == n :
        if s == k:
            print(temp)
            return
        return

    temp.append(arr[idx])
    s += arr[idx]
    subsequencesSum(idx+1,arr,k,s,n,temp)
    temp.pop()
    s -= arr[idx]
    subsequencesSum(idx+1,arr,k,s,n,temp)


subsequencesSum(0,arr,k,0,len(arr),[])
