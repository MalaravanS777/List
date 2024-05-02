a=input().split()
n=int(input())
for i in range(0,n):
    a.append(a[i])
print(a)
for i in range(n-1,-1,-1):
    a.pop(i)
print(a)
