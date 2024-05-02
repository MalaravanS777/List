a=input().split()
lst=[]
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if(a[i]==a[j]):
            if(a[i] not in lst):
                lst.append(a[i])
print(lst)
