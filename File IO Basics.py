# File IO Basics

"""
"r" - open file for reading                    (rt & rb)  rt is defualt
"w" - open file for writing
"x" - creates file if not exists
"a" - add more content to a file
"t" - text mode
"b" - binary mode
"+" - read & write(update info.)
"""

# ------------>File Reading<--------------------

# f = open("file.txt")
# f = open("file.txt","rb")              #read file in binary using "rb" function

# print(f.readline())                  #read one by one line
# print(f.readline())
#
# print(f.readlines())                 #read file as list

# for line in f:                       #read file using for loop
#     print(line,end=(" "))

# content = f.read()                    #read first 3 chara. in file
# print(content)
# f.close()                              #always close file using this function

# ------------>File Writing<--------------------

# f = open("file.txt","w")                                  #  "w" --> write in file.here replace content with existing contents.
# f.write("hello friends  in python tutorial")
# f.close()

# ------------>File Appending<--------------------

# f = open("file.txt","a")                                     # "a" --> add content in file
# f.write("hello jigar\n")
# f.write("hello sanket\n")
# f.write("hello akshay\n")
# f.write("hello jay\n")
# a=f.write("hello friends welcome to python tutorial\n")           # a=f.write()  --> show number of character in file
# print(a)
# f.close()

# ------------>read & write File at same time<--------------------

# f = open("file.txt","r+")                                           # "r+" ---> read & write File at same time
# f.write("hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")       # write in file (like:-add content)
# print(f.read())                                                     # read file
# f.close()

# ------------>tell(),seek() function<--------------------

# f = open("file.txt")
#
# print(f.tell())                                         # show your file pointer in which position
# print(f.readline())
#
# print(f.seek(0))                                        # work of seek func. is it can set pointer on your argument position like, 0, 4, 486, etc.
# print(f.readline())
#
# f.close()

# ------------>with block<--------------------

with open("file.txt") as f:                               #this is use for file open and close at same line without use of close() function.
    a = f.readline()
    print(a)
#        OR
# f = open("file.txt")                                      # here we can use both of one.
# print(f.readline())
# f.close()
