#----->import modules<-----

#import flask
#import pandas

#----->comments<------

'''here it is a singal line comment:'''
#hii my name is jigar

"""    here it is amultiline comments:
hii
my name
is jigar
"""

#------>Print Message<-----


'''
print("Hello World", end=" "                  #here 'end' work is print new line after one space.
      "hello Python\n")

print("Hello World", end="&"                  #here 'end' not put space.     end="<here give command>"
      "hello Python\n")

print("Hello World", end=" % "                  #here 'end' put space.and print '%' between two lines.     end="<here give command>"
      "hello Python\n")

print(2 * "\nWikipedia is a free online encyclopedia, created and edited by volunteers around the world and hosted by the Wikimedia Foundation.\n")

'''

#------>Variable<-------

'''
var1="Wikipedia is a free online encyclopedia, created and edited by volunteers around the world and hosted by the Wikimedia Foundation."
var2=45
var3=29.4
print(var1)
print(var2+var3)
'''

#------>Data Type<-------

'''
print(type(var1))
print(type(var2))
print(type(var3))

'''
#------>Type Casting<-------

'''
int()
str()
float()
'''
#print(str(var1)+str(var2))

#------>Take User Input<-------

'''
var1=input()
print("You Entered", var1)
'''

#------>String Slicing<-------

'''
mystr="hello Jigar.How are you?"
print(len(mystr))
print(mystr)          #print string
print(mystr[0:5])     #print first four character
print(mystr[0::2])    #Skip every second number
print(mystr[::-1])    #reverse this string
print(mystr[::-2])    #reverse this string & skip every second chara.
'''

#------>String Function<-------

'''
mystr="Hello Jigar.How are You?"

print(mystr.isalnum())
print(mystr.isalpha())
print(mystr.endswith("You?"))
print(mystr.count("o"))
print(mystr.capitalize())
print(mystr.find("are"))
print(mystr.lower())
print(mystr.upper())
print(mystr.replace("are" , "is"))
'''

#------>Brackets of List,Tupple,Dictionary<-------

'''
                    Format:

List        ---->   ["","", ,""]          # "<enter string>" & <enter integer value>
Tupple      ---->   (,,,,)
Dictionary  ---->   {"_" : "_", "_" : "_"}
set         ---->   set_name = set ()        #output will be show on this format {}
'''


#------>List Slicing<-------

'''
List1=["jigar","sanket","Akshay","jay","uttam","Aakash","neel"]
print(List1)
print(List1[::-1])          #reverse list
print(List1[2:6])           #show list elements on 2 to 6

print(type(List1))

#List1.reverse()            #reverse list
print(List1)

List1.append("nas")          #add element on last position
List1.append("wbefb")
List1.remove("nas")          #remove element
List1.insert(2,"nas")        #insert element on particular space
List1.pop()                  #delete last element of list
List1[1]="kothiya"           #"kothiya" replace at 1st position
print(List1)
'''

'''
mutable = can change
immutable = can not change
'''

#------>Tupple<-------

'''
tp=(1,2,3,4,5,6,7,8,9,0)
#tp[1]=20                       #give error message-->tupple can not change(immutable) but list is mutable(can change)
print(tp)
'''

#------>Swapping in Python<-------

'''
a=3
b=6
a,b = b,a
print(a,b)
'''

#------>Dictionary<-------

#dictionary is nothing but key value pairs

'''
d1={"jigar":"10","sanket":"27","akshay":"23","radhen":"22","jay":{"j1":"4","j2":"59","j3":"45"}}
#print(type(d1))
#print(d1)

d1["neel"]="47"          #add in dict.
d1["bodar"]="66"
print(d1)
print(d1["jigar"])      #show key value
print(d1["jay"])
print(d1.get("jay"))         #get your item detail
d1.update({"yash" : "8"})    #update your dictionary
del d1["neel"]          #delete this element

print(d1)

d2 = d1                 #use dict d1 as refference and changes will apply both dictionary
d2 = d1.copy()          #make a copy of dict. d1
del d2["akshay"]

print(d1)
print(d2)

print(d1.keys())       #show the keys
print(d1.items())      #show the item
'''

#------>Sets<-------

'''
s1 = set ()
s1.add(1)                                #add element in sets
s1.add(1)                                #we can not add any element again
s1.add(2)
print(type(s1))
print(s1)

"""
functions of set
"""

s4 = s1.union({1,2,3,4})                #union with set s1
print(s4)
s4 = s1.intersection({1,2,3,4})         #intersection with set s1
print(s4)
print(len(s4))                          #find length of set s4
print(min(s4))                          #find minimum value of set s4
print(max(s4))                          #find maximum value of set s4

#print(s1)


#print(type(s1))

s2 = {1,2,3,4,5,6}                       #create set diff. type
print(type(s2))
print(s2)

s3_from_list = set([1,2,3,4,5,6,7,8,9,0])          #create set using list
print(type(s3_from_list))
print(s3_from_list)
'''
