n1 = 25
g=1
print("Number of Guesses is limited to 8 times")
while (g<=8):
    n2 = int(input("Enter your Number Here:\n"))
    if (n1 < n2):
        print("!Pleace Reduce Your Number!")
    elif (n1 > n2):
        print("!Pleace Increase Your Number!")
    else:
        print("You Are Winner")
        print(g,"Number of Guesses take to finish this game.")
        break

    print(8-g,"Number of guesses left.")
    g=g+1

if (g > 8):
    print("Game Over!!")