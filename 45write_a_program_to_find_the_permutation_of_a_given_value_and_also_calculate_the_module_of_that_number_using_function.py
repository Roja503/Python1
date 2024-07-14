def f(a):
    fact=1
    for i in range(1,a+1):
        fact=fact*i
    return(fact)
def main(n,r,m):
    x=n-r
    p=f(n)/(f(x)*f(r))
    print(p)
    c=p%m
    print(c)
n=int(input())
r=int(input())
m=int(input())
main(n,r,m)
