def f(a):
    fact=1
    for i in range(1,a+1):
        fact=fact*i
    return(fact)
def main(n,r):
    x=n-r
    p=f(n)/f(x)
    print(p)
    c=f(n)/(f(x)*f(r))
    print(c)
main(3,2)

