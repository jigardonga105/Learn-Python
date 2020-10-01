Client_list = {1:"Harry",2:"Jarry",3:"Garry",4:"Carry"}
log_list = {1:"exercise",2:"diet"}

def gatetime():
    import datetime
    return datetime.datetime.now()


try:
    again = "y"
    while (again != "n"):
        print("--->Welcome to Health Management System<---")
        print()
        print("Select Client Name:")

        for key, value in Client_list.items():
            print("Press ", key, ":", value)

        Client_name = int(input())
        print("Selected Client name is", Client_list[Client_name])
        print()

        print("Press 1 : Log\n"
              "Press 2 : Retrive")

        Ch = int(input())
        print("You select", Ch)
        print()


        if (Ch==1):
            for key,value in log_list.items():
                print("Press",key,":",value)
            log_name = int(input())
            print("Selected Choise name is",log_list[log_name])
            print()
            print("Enter your "+log_list[log_name]+" Name here:\n")

            with open(Client_list[Client_name]+"_"+log_list[log_name]+".txt","a") as f:
                a = "y"
                while(a != "n"):
                    print("Add Details:")
                    detail = input()
                    print("You enter:" + detail + "\n")
                    f.write("[ " + str(gatetime()) + " ] : " + detail + "\n")
                    a = input("Add more Details: y/n \n")
                    continue

        elif (Ch==2):
            for key,value in log_list.items():
                print("Press",key,":",value)

            log_name = int(input())
            print("Selected Choise name is",log_list[log_name])

            print(Client_list[Client_name]+"_"+log_list[log_name]+" Report is:\n")

            with open(Client_list[Client_name]+"_"+log_list[log_name]+".txt") as d:
                detail = d.readlines()
                for line in detail:
                    print(line,end=(""))

        else:
            print("Envalid Input!!")

        again = input("Run Again: y/n \n")
        continue

except Exception as e:
    print("Envalid Input!!")