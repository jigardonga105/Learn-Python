# Write a program to display the following sequence.
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

'''
ch='A'
print(type(ch))
for j in range(1,27):
     print(ch)
     ch=chr(ord(ch)+1)
'''

# f=lambda x:x*x
# value = f(5)
# print(value)

def fahrenheit(T):
 return ((float(9)/5)*T + 32)
def celsius(T):
 return (float(5)/9)*(T-32)
temp = (36.5, 37, 37.5,39)
F = map(fahrenheit, temp)
C = map(celsius, F)
print(F)
print(C)