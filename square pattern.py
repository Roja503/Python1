c=3
r=3
for i in range(r):
    for j in range(c):
        print("*",end="")
        if j==1 or j==0:
            print("-",end="")
    print()
