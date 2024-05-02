a=input().split()
lst=[]
max=a[0]
for i in range(len(a)-1):
    for j in range(i,len(a)):
        if(a[i]>a[j]):
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
for i in a:
    if(i not in lst):
        lst.append(i)
print(lst)
