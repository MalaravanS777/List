a=input().split()
if(a[0]>a[2]):
    max1=a[0]
    max2=a[1]
else:
    max2=a[0]
    max1=a[1]
for i in range(len(a)):
        if(a[i]>max1):
            max2=max1
            max1=a[i]
        elif(a[i]>max2):
            max2=a[i]
print(max2)
