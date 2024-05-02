a=input().split()
j=-1
for i in range(0,len(a)//2):
    temp=a[i]
    a[i]=a[j]
    a[j]=temp
    j-=1
print(a)
