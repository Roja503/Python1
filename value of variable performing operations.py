n=["X++","X++","++X","++X"]
a=0
for i in n:
    if i=="X++" or i=="++X":
        a+=1
    else:
        a-=1
print(a)
