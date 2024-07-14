num = int(input())
sum = 0
a= num
while a > 0:
    digit = a % 10
    sum += digit * digit * digit
    a = a//10
if sum == num:
    print(' Armstrong number')
else:
    print('not an Armstrong number')
