# print your name n times using recursion
# def fun(i,n):
#     if i > n:
#         return
#     print('Shree dharma')
#     fun(i+1,n)

# n = int(input())
# fun(1,n)

# print 1-n using recursion
# def fun(i,n):
#     if i > n:
#         return
#     print(i)
#     fun(i+1,n)

# n = int(input())
# fun(1,n)

# print n-1 using recursion
# def fun(n):
#     if n==0:
#         return
#     print(n)
#     fun(n-1)

# n = int(input())
# fun(n)

# print 1-n without incrementing i 
# def fun(n):
#     if n < 1:
#         return
#     fun(n-1)
#     print(n)
# n = int(input())
# fun(n)

# print n-1 without decrementing i
# def fun(i,n):
#     if i > n:
#         return
#     fun(i+1,n)
#     print(i)
# n = int(input())
# fun(1,n)

# print factorial of n using functional recursion
# def fun(n):
#     if n == 1:
#         return 1
#     return n * fun(n-1)
# n = int(input())
# print(fun(n))

# reverse an array using recursion with only one pointer
# def fun(arr, i, n):
#     if i >= n/2:
#         return arr
#     arr[i],arr[n-i-1] = arr[n-i-1],arr[i]
#     return fun(arr,i+1,n)
# arr = list(map(int, input().split()))
# print(fun(arr, 0, len(arr)))

# check if a string is palindrome using recursion
# def fun(s,i,n):
#     if i >= n-i-1: return True
#     if s[i] != s[n-i-1]: return False
#     return fun(s,i+1,n)
# s = input()
# print(fun(s,0,len(s)))

#  print nth fibonacci value
def fun(n):
    if n <= 1:
        return n
    return fun(n-1) + fun(n-2)
n = int(input())
print(fun(n))
