class Calculator:
    def add(self,x,y):
        return x+y
    def subtract(self,x,y):
        return x-y
    def multiply(self,x,y):
        return x*y
    def divide(self,x,y):
        if y!=0:
            return x/y
        else:
            return("cannot divide by zero")
calculator=Calculator()
result=calculator.add(7,5)
print("7+5=",result)
result=calculator.subtract(7,5)
print("7-5=",result)
result=calculator.multiply(7,5)
print("7*5=",result)
result=calculator.divide(7,5)
print("7/5=",result)
