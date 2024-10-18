def factor(n,k):
    count=0
    a=[]
    for i in range(1,n+1):
        if n%i==0:
            count+=1
            a.append(i)
    if k<=len(a):
        return a[k]
    else:
        return 1
n=int(input())
k=int(input())
result=factor(n,k)
print(result)
