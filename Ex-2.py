#Faulty Calculator
#design a calculator which will correctly solve all the problem except the following ones:
#56 + 9 = 77
#45 * 3 = 555
#56/6 = 4


print("Enter first number")
num1=int(input())

print("Enter second number")
num2=int(input())

print("enter your operator")
op=input()

if op=='+' and num1==56 and num2==9 :
    print("77")
elif op=='*' and num1==45 and num2==3 :
    print("555")
elif op == '/' and num1 == 56 and num2 ==4:
    print("4")
elif op=='+':
    print(num1+num2)
elif op=='-':
    print(num1-num2)
elif op=='*':
    print(num1*num2)
elif op=='/' :
    print(num1/num2)
else:
    print("Invalid Input")