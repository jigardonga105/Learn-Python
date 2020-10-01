'''
v1 = int(input("Enter Your First value:"))
v2 = int(input("Enter Your Second value:"))

if v1>v2:
    print(v1,"is maximum.")
elif v1==v2:
    print(v1,"&",v2,"is same value")
else:
    print(v2,"is maximum.")
'''

'''
list1 = [1,2,3,4,5,6,7,8,9,0]
print("select value in list:")
n1 = int(input(list1))
if n1 in list1:
    print(n1,"is in list.")
else:
    print(n1,"is not in list.")
'''
'''
list1 = [1,2,3,4,5,6,7,8,9,0]
print("select value in list:")
n1 = int(input(list1))
if n1 in list1:
    print(n1 in list1)                              #use of in & not in statement
else:
    print(n1 in list1)
'''

#short hand if else

a=int(input("Enter a=\n"))
b=int(input("Enter b=\n"))

print("a is greater than b") if a>b else print("b is greater than a")