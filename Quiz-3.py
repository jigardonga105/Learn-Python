list = ["jigar","sanket",4,5,6,2,6,9,66,44,99,55,77,22,666,987,45,"jay","akshay"]

for item in list:
    if str(item).isnumeric() and item > 6:
        print(int(item))