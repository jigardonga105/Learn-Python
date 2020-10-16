print("how many row you want to print?:")
one = int(input("Enter Number:\n"))
print("type 1 or 0")
two = int(input())
new = bool(two)
#it repersent classes
if new==True:
    for i in range(one):
        for j in range(i+1):
            print("*",end=(""))

        print()

elif new==False:
    for i in range(one,0,-1):
        for j in range(1,i+1):
            print("*",end=(""))

        print()
