a=int(input())
count=0
i=0
for i in range(len(a)):
    if(a[i]=='a'or a[i]=='e'or a[i]=='i'or a[i]=='o'or a[i]=='u'):
        count=count+1
print(count)
