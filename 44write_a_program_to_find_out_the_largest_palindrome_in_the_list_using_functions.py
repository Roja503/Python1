def largest_palindrome(li):
    lr=-1
    for i in li:
        s=str(i)
        if s==s[::-1]:
            if i>lr:
                lr=i
    print(lr)
li=[1,232,54545,99991]
largest_palindrome(li)
