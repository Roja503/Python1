n="192.168.1.32"
a=""
for char in n:
    if char==".":
        a+="[.]"
    else:
        a+=char
print(a)
