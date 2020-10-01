i=0

while(True):
    if i+1<8:
        i = i + 1
        continue                    #loop run at this position

    print(i+1, end=" ")
    if (i==44):
        break                       #stop the loop
    i = i+1
