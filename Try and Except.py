n1 = int(input("Enter your n1:\n"))
n2 = (input("Enter your n2:\n"))

try:                                                 #solve error but when error dosen't solve then it's print error message and run program continueslly
    print("Sum of this two number is=",n1+n2)
except Exception as e:
    print(e)

print("this line is very important. print this line")