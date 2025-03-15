print("Enter two numbers that you want to perform an operation on :\n")
num1=float(input("First number :"))
num2=float(input("Second number :"))

operator=input("Enter the operation that you wish to perform on the two numbers(+,-,*,/) :")
if operator=='+':
    result=num1+num2
   
elif operator== '-':
    result=num1+num2
    
   
elif operator == '*':
    result=num1*num2
    
   
elif operator == '/':
    result = num1/num2
    
else:
    print("You entered a wrong operator, please enter the correct operator! ")

print(f"Result of {num1} {operator} {num2} = {result}")


