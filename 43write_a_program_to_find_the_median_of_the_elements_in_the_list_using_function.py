def median(list):
    li=[]
    li=list.sort()
    n=len(list)
    m1=n//2
    m2=(n+1)//2
    if n%2==0:
        print(((m1)+((m1)+1))//2)
    else:
        print(m2)
list=[2,1,4,5,6,3]
median(list)
