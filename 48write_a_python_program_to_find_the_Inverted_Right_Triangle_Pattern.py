n=int(input())
start=n*(n+1)//2
for i in range(n,0,-1):
    current=start
    for j in range(i):
        print(current,end="")
        current-=1
    print()
    start-=1
