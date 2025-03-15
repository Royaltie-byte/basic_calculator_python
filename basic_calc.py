print("Enter two numbers that you want to perform an operation on :\n")
num1=float(input("First number :"))
num2=float(input("Second number :"))


#checking the validity of the operator so as to proceed.
while True:
    operator=input("Enter the operation that you wish to perform on the two numbers(+,-,*,/) :")
    if operator in ('+','-','*','/'):
        break
    else:
        print("Invalid operator!!!.Enter a valid  operator ")



if operator=='+':
    result=num1+num2

elif operator== '-':
    result=num1-num2
    

elif operator == '*':
    result=num1*num2
    

elif operator == '/':
    if num2 !=0:
        result=num1/num2
    else:
        result="Error !!!Division by zero is not allowed."
print(f"Result of {num1} {operator} {num2} = {result}")

  






