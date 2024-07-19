m=int(input())
a=str(m)
b=len(a)//2
c=sorted(a[:b])+sorted(a[b:],reverse=True)
print(''.join(c))
