def add (num1,num2,num3):
    return num1+num2+num3
def subtract (num1,num2,num3):
    return num1-num2-num3
def multiply (num1,num2,num3):
    return num1*num2*num3
def divition (num1,num2,num3):
    return num1/num2/num3

print("select your options:\n")
"1.adding\n"\
"2.subtract\n"\
"3.multiply\n"\
"4.divition\n"\

select = int(input("choose your option from:1,2,3,4:"))
num1 = int(input("Enter your first number:"))
num2 = int(input("Enter your second number:"))
num3 = int(input("Enter your third number:"))

if select ==1:
    print(num1,"+",num2,"+",num3,"=",add(num1,num2,num3))

elif select ==2:
    print(num1,"-",num2,"-",num3,"=",subtract(num1,num2,num3))

elif select ==3:
    print(num1, "*", num2, "*", num3,"=",multiply(num1,num2,num3))

elif select ==4:
    print(num1, "/", num2, "/", num3, "=", divition(num1, num2, num3))

else:
    print("invalid input")