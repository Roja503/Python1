stones="AAbbb"
jewels="Aa"
count=0
for i in stones:
    for j in jewels:
        if i==j:
            count+=1
            break
print(count)  
