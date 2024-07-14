n1=input()
n2=input()
if len(n1)==len(n2):
    if sorted(n1)==sorted(n2):
        print("it is a anagram")
    else:
        print("it is not a anagram")
else:
    print("Length is not match")
