def uplow(string):
    lower=0
    upper=0
    for i in string:
        if(i.islower()):
            lower=lower+1
        else:
            upper=upper+1
    return(lower,upper)
print(uplow("LaDdu"))
