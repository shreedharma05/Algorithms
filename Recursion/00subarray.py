arr = list(map(int, input().split()))
n = len(arr)
res = []
for i in range(n):
    for j in range(i+1,n+1):
        temp = arr[i:j]
        res.append(temp)
        
print(res)

