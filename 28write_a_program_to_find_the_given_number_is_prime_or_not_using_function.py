def prime_not(a):
    count=0
    for i in range(1,a+1):
        if(a%i==0):
            count=count+1
    if(count==2):
        return "prime"
    else:
        return "not a prime"
print(prime_not(5))
