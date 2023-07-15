
#---DATA TYPES---#

#----NUMERICAL
#--- INTIGER(int)

# i  = 45
# print(i)

# num = 65
# print(num, type(num))

# a = int(input("enter the number"))
# print(a, type(a))

#--- FLOAT

# a = 45.2
# print(a) 

# f = 455.e3
# print(f, type(f))

#---  COMPLEX (REAL + IMAGINARY PART)

# a = 106+1j
# print(a, type(a))


# d = 892+0j
# print(d.real)

# d = 782+0j
# print(d.imag)

#---- SEQUENCE DATA TYPE ----#

#--- STRING " "

# A = "helo everone"
# print(A)

# str = "string is a sequence data type"
# print(str, type(str))

# z = 'hii...'
# print(z)

#---LIST[]

# l = [ 85, 96, 213.51, 4+45j]
# print(l)

# lst = [7, 465, "item" , 542]
# print(lst, type(lst))

# list_item = ["book", "pencil", "note nook", 562, 36.2]
# print(list_item, type(list_item))

#--- TUPLE()

# tup = (12, 560, 5633.5, "tuple", 795+4j)
# print(tup, type(tup))

# t = (5, 263, 952, 6.26, "person", [56,4],{"set"})
# print(type(t), t)

# t1 = ("messo", 78, (12,3), [1, 3.2], frozenset({45,632}))
# t2 = ("rabba", 451, 5923+5j, 78796)
# print(t1, type(t1), t2, type(t2))

#--- SET{}

# set = {45, 3, 5, 3, 53, 2, 6, frozenset({15, 563.3}) }
# print(set)

# s = {78, 52, (623, 546,"tuple"), range(1,2), "str"}
# print(s)

# s1 = {"lemmon",463, 52, 3.263, frozenset({45, 63})}
# print(s1, type(s1))

#---FROZENSET({})

# f = frozenset({451, 562, 23.6, 2, 465})
# print(f, type(f))

# froz = frozenset({45, 561, 54230, "immutable", (263)})
# print(froz)

# frozen = frozenset({"set", 465, 53.6, 56+5j,45 })
# print(frozen)

#--- RANGE(1,5)

# for i in range(1,5):
    # print(i)

# for product in [45, 63.2, 45]:
#     print(product)

# for j in range(1,51):
#     print(j)

#---BYTEARRAY

# a = [26, 65]
# b = bytearray(a)
# for i in b:
    # print(i)

# a = (1, 6)
# b = bytearray(a)
# for i in a:
#     print(i, type(i))

# z = [45, 49, 45,1]
# y = bytearray(z)
# for i in y:
#     print(i)

#--- MAPPING DATA TYPE
#---- DICTIONARY{"key1": "value1"}

# fruit = {"orange": 45, "water melon": 56, "sapota": 623}
# print(fruit)

# veg = {"spinach":12, "cluster bbens":50, "tomato":46, "brinjal":98}
# print(veg, type(veg))

# name_surname = {"hema": "malini", "amitab": "bachhan", "sani": "deol"}
# print(name_surname)


#--- BOOLean 
 
# print(bool(1))
# print(bool("str"))
# print(bool(1+5))
# print(bool(5))
# print(bool(0))


#----- OPERATORS -----#
#---- ARITHMATIC OPERATOR

# a = 4
# b = 9
# print(a + b)   # addition

# a = 8
# b = 9
# print(a - b)   # substraction operator

# s = 89
# h = 2
# print(s * h)    # multiplication operator

# b = 15
# c = 5
# print(b / c)   # division operator

# o = 8
# p = 6
# print(o % p)   # modulo operator

# t = 89 
# y = 96
# print(t // y)   # floor division operator

# r = 10
# t = 5
# print(r ** t)  # exponent/ power operator 

#---- RELATIONAL OPERATOR

# a = 2
# b = 4
# print("a < b is ", a < b)  

# c = 89
# d = 75
# print("c > d is ", c > d)

# e = 23
# f = 20
# print("e <= f is", e <= f)

# o = 89
# p = 51
# print("o >= p is", o >= p )

# a = 20
# s = 20
# print("a == s is", a == s)

# c = 89
# v = 53
# print("c != v is", c != v)

# #---- ASSIGNMENT OPERATOR 

# a = 10
# a += 10
# print(a)

# b = 45
# b -= 1
# print(b)

# c = 2
# c *= 10
# print(c)

# d = 80
# d /= 2
# print(d)

# e = 10
# e %= 3
# print(e)

# f = 50
# f //= 10
# print(f)

# g = 40
# g **= 2
# print(g)

# ----SPECIAL OPERATOR

#---- MEMBERSHIP OPERATOR

# a = "hello world"
# print("ll" in a)

# str = "if multiple oprators present"
# print("pre" in str )

# b = [5, 5, 320]
# for i not in [5]:
#     print(i)


#---- IDENTITY OPRATOR

# a = 20
# b = 10
# print(a is b)

# a = 80
# b = 60
# print(a is not b)

# a = "hello"
# b = "Hello"
# print(a is b)

#---- LOGICAL OPERATOR

# a = True
# b = False
# print(a and b)

# a = True
# c = True
# print(a and c)

# a = False
# b = False
# print(a and b)

# h = False
# n = True
# print(h and n)

#--- or operator

# s = True
# d = True
# print(s or d)

# a1 = True
# a2 = False
# print(a1 or a2)

# j = False
# k =  True
# print(j or k)

# l = False
# m = False
# print(l or m)

#--- NOT OPRATOR 

# print(not False)
# print(not True)

 #****-------ITERATION ONLY PERFORM ON SEQUENCE AND MAPPING DATA TYPES---------****

# for i in range(0,11):  #1st way
#     print(i)
 
# s= "hello everyone"    #2nd way
# for i in s:
#     print(i)

# for i in [4, 54, 45.2, "kgf", [5,32.6]]:
#     print(i)

# s = "hey cherry"
# for i in s:
#     print(i)

# for i in {2, 5, "god", 56.e2}:
#     print(i)

# for i in{"apple": 456, "mashmelo": 45}:   # only key are print in dict
    # print(i)

# for i in (45, 46, [516, 656, "str"], {"l", 32.2}):
#     print(i)

# for i in frozenset({5, 45, "srt" , (12, 563.3)}):
#     print(i)


#---CONVERT IN LIST AND PRINT---#

# r = list(range(0,20))
# print(r, type(r))
 
# r = list(range(1,31))
# for element in r:
#     print(element)

# r = list(range(1,5))
# print(r, end=" ")

# s =list("hellow miss") # seprated all characters
# print(s)
# print(s, end="")

# t = list((5, 45, 26.54, "str")) # in tuple double paranthesis are used
# print(t)

# s = list({5, 89.2, "str"}) 
# print(s)

# f = list(frozenset({56, 45, 23.3}))
# print(f)

# d = list({"key1": "val1", "key2": "val2"})
# print(d)

#---CONVERT IN TUPLE---#

# x = tuple(range(0,5))
# print(x, type(x) )

# a = tuple([4, 55, 26.3])
# print(a)

# b = tuple({"ninja", 54, 21})
# print(b)

# c = tuple("hello it is good")
# print(c)

# d = tuple({"puja": "kature", "sakshu": "kature"})
# print(d)

# e = tuple(frozenset({65, 54, "lmc"}))
# print(e)

# f = tuple(range(5,25))
# print(f)


#--CONVERT IN SET---#

# a = set(range(1,6))
# print(a)

# a = set("good good")
# print(a)
 
# b = set([5, 52, 23.2, 5])
# print(b)
 
# c = set((5555, 56, 263.263))
# print(c)

# c = set(range(2,10,2))
# print(c)

# d = set({"hema": 45})
# print(d)


#---CONVERT IN FROZENSET---#

# a = frozenset({range(8,25)})
# print(a, end=" ")

# e = set(frozenset({56, 26.2, "str"}))
# print(e)

# a =frozenset({45, 465.5})
# print(a)

# b = frozenset([61, 656, 462.23, "goodness"])
# print(b)

# c = frozenset("god bless you!")
# print(c)

# d = frozenset((56, 32.1))
# print(d)

# a = str([45, 620.26])
# print(a)


#---CONVERT IN DICT ( can not convert)

# b = dict(range(1,6))
# for i in b:
#     print(i)

# a = dict({465, 26, 626, 23})  #TypeError: cannot convert dictionary update sequence element #0 to a sequence
# print(a)

#---PRINT EVERY SINGLE ELEMENT---#

# for element in range(1,11):
#     print(element)

# s = " hey buddy!!"
# for i in s:
#     print(i)

# l = [12, 56.32, 3, "str", 8+6j, 00]   # 1st way
# for i in l:
#     print(i)

# for i in [45, 90, "wish", 3.2]:     #2nd way
#     print(i)

# t1 = (5, 96, 3.23, "youth", "ohh my goodness")
# for i in t1:
#     print(i)

# s = {20, 60, 10, 45+26j, "for loop", "while loop", 10, 10}
# for i in s:
#     print(i)

# f1 = ({45, 89, 203.1, 65, "pep8 rules", })
# for i in f1:
#     print(i)

# s = "variables should not start with digit"
# for i in s:
#     print(i)

# d1 = {"Aditi": "kature", "Saksham": "kature", "Darshana": "kature"}
# for i in d1:
#     print(i)

#----PRINT VALUE WITH ITS DATA TYPE---#


# s = [45, frozenset({5}) , 98, "/*", (45, 2.3), ".format", 96+9j, 36.e2 ,[20, 30], {1, 32, "case sensetive"}]
# for i in s:
#     print("OBJECT:-- ", i, "DATA_TYPE IS:--", type(i)) 


# s1 = { 45, 23, 56+5j, "set is mutable", frozenset({54, 32.03}),  "Mutable elements not allow here"}
# for i in set:
#     print("*object* :--", i, "**data_type** :--", type(i))


# t2 = ("im_mutable", 54, 23.3, {54, 3.2}, [45, "python"])
# for i in t2:
#     print("OBJECT:--", i, "DATA TYPE :--", type(i))

#----REMOVE SPACE FORM STRING---# there are two ways as fllows 

# s = " identifiers should not use special characters acept underscore(_)"
# for i in s:
#     if i != " ":
#         print(i)


# s2 = "iterate only over sequence data type and mapping data type"
# for i in s2:
#     if i == " ":
#         pass     #transfer statement
#     else:
#         print(i)

# a = "list, set, bytearray, dictionary are mutable data types"
# for i in a:
#     if i != " ":
#         print(i)

# -----FIND LENTH OF STRING----# ( 2 ways )

# s = "im_mutable data types are - string, tuple, range, byte, frozenset"
# str_len = len(s)
# print(str_len)

# a = "All fundamental data types are immuatable"
# n = 0
# for i in a:
#     n = n + 1;
# print(n)

# path = "class>C:/Users/Home/AppData/Local/Programs/Python/Python310/python.exe"
# str_len = len(path)
# print(str_len)


# file_name = "e:/python class/practice_HW.py"
# a = 0
# for i in file_name:
#     a = a + 1;
# print(a)

#----IF CONDITION IN FOR LOOP----#

# for i in range(0,51):
#     if i == 20:
#         print("tweenty")

#     print(i)

# fruits_name = {"kiwi": 100, "dragenfruit": 120, "orange": "200", "appple": 150, "sapota": 60, "grapes": 50}
# for i in fruits_name:
#     if i in ["dragenfruit"]:
# #         print("dragenfruit is 120 per kg")
# #     else:
# #         print(i)

# electronic_items = ["washing machine", "mobile", "lappy", "computer", "tab"]
# for i in electronic_items:
#     if i in ["lappy", "computer"]:
#         continue
#     print(i)
      
      
# furniture_items = {"table", "chair", "bed", "desk", 31.53, "dressers", 416, "cupboard"}
# for items in furniture_items:
#     if items not in ["chair", "cupboard"]:
#         print("OBJECT:-- ", items, "DATA TYPE:-- ", type(items))

#---- .FORMATE----#

# s = "my school name is {} international school".format("ira")    #1st way
# print(s)

# user_name = input("Enter tha name:- ")    #2nd way
# s =f"my name is :- {user_name}"
# print(s)

# user_input = input("Enter your degree name :- ")
# a = "i had finished my education in   {} ".format(user_input)
# print(a)

# a = "which is your favorite languge {}".format("marathi")
# print(a)

# d = "python is recommended as first {} language".format("programming")
# print(d)

# write = input("write your cast:- ")
# a = f"cast is {write}"
# print(a)

#ASSIGNMENT OPERATOR USE IN FUNCTION(METHOD)

#ADDITION OF TWO NUMBERS
# a = int(input("Enter the value:- "))
# b = int(input("Enter the value:-"))
# print(f"addition of {a} and {b} is {a+b}")
 
#SUBSTRACTION OF TWO NUMBERS

# a = eval(input("Enter the number:- "))
# b = eval(input("Enter the number:-"))
# print(f"substraction of {a} and {b} is {a-b}")

# MULTIPLICATION OF TWO NUMBERS

# a = eval(input("Enter first number:- "))
# b = eval(input("Enter second number:- "))
# print(f"multiplication of {a} and {b} is {a*b}")

#DIVISION OF TWO NUMBERS

# a = eval(input("Enter the number:- "))
# b = eval(input("Enter the number:- "))
# print(f"division of {a} and {b} is {a/b}")

# RELATIONAL OPERATOR USE

# num1 = eval(input("Enterfirst number:-"))
# num2 = eval(input("Enter second number:-"))
# print(f"num1 is greater than num2 :- {num1} and {num2} is {num1 > num2}")

# n1 = int(input("Enter the 1st number:- "))
# n2 = int(input("Enter the 2nd number:- "))
# print(f"n1 is less than n2:- {n1} < {n2} is {n1 < n2}")

#---USE BREAK IN  FOR LOOP---#

# for i in range(1,6):
#     if i == 5:
#         break
#     print(i)

# for i in[45, 65, 89, 63.2, "str"]:
#     if i in [63.2]:
#         break
#     else:
#         print(i)

# print(i)

# for i in{"kapil": "sharma", "aaliya": "bhatt", "kiyara": "advani"}:
#     if i not in {"aaliya": "bhatt"}:
#         break
# print(i)

# for i in[1, 20, 45, 10]:
#     if i in (45, 20):
#         break
#     print(i)

# s = "python program are portable"
# for i in s:
#     if i in ("y"):
#         break
#     print(i)

    
# for i in range(1,51):
#     if i % 2 == 0:
#         break
# print(i)

#--- USE OF CONTINUE---#

# for i in range(1,101):
#     if i == 50:
#         continue
#     # print(i)
# print(i)

# for i in [45, 53.2, 461, ["nested"]]:
#     if i == 461:
#         continue
#     else:
#         print(i)

# for i in( 78, 5, 79, 846.33, 45+65j, frozenset({15})):
#     if i in ( 45+65j, 79):
#         continue
#     print(i)

# cloths_name = {"top", "jense", "troser", "onepice", "twopice", "lehenga", "sharara"}
# for cloth in cloths_name:
#     if cloth not in {"troser", "lehenga", "sharara"}:
#         continue
#     else:
#         print(cloth)

# for elememts in {"kartik": "nayra", "virat": "sai", "aryan": "imli"}:
#     if elememts in {"virat": "sai"}:
#         print(elememts)
#     else:
#         continue

#----use of pass----#

# for i in range(0,21,2):
#     if i != 10:
#         pass
# print(i)


# vegitable_list= ["tomato", "brinjal", "brokli", "potatos", "biter groud", "cluster bines"]
# for vegitables in vegitable_list:
#     if vegitables == "biter groud":
#         pass
#     print(vegitables)

# for i in range(1,101):
#     if i != 60:
#         pass
#     print(i)

#----USE FOR WITH ELSE----#

# for i in range(1,21):
#     print(i == 10 * 2)
#     continue
# print("*" * 50)
# for i in (1,11):
#     print(i + 1)


# for j in range(1,15,3):
#     print(j)
# else:
#     print(j)
# # print(j*5)


# for i in range(1,11):
#     print(i)
# else:
#     print("for loop is completed")
# print("-" * 50)
# for j in range(1,6):
#     if j == 5:
#         print(j)
#         break
# else:
#     print("its complete")


# for i in [45, 63.2, 482, "str"]:
#     if i in [482, 45]:
#         print(i)
#     for i in [i == 45]:
#         print(i)
#         break
# else:
#     print("loop complete")

#---- NESTED FOR LOOP ----#

# for i in frozenset({45, 895, 563+6j, 452, "set"}):
#     for j in {2, 23.1, 4653, "45"}:
#         print(i,"*"*3, j)

# for i in range(1, 11):
#     for j in range(1,6):
#         if j <= 4:
#             print(j)


# for i in range(1,6):
#     if i <= 3:
#         print(i)
#         for j in range(10,16):
#             print(i, j)

#----LIST COMPREHENSION

# --- print even numbers using .append method
# Lst = []
# for i in range(1, 11):
#     if i % 2 == 0:
#         Lst.append(i)
# print(Lst)

#--- print table of 3 in list
# list = []
# for i in range(1, 101):
#     if i % 3 == 0:
#         list.append(i)
# print(list)

#--- print albhabets in dictionary("a": "A") 
# dict = {}
# for i in range(1, 27):
#     dict[chr(96+i)] = (chr(64+i)) #-----1st
#     dict[chr(96+i)] = chr(96+i).upper() #----2nd
# print(dict)

#--- print asci value 
# s = set()
# for i in range(1,6):
#     s = (chr(10+i),chr(30+i))
#     print(s)


#--- print even numbers in list :- 
# l1 = [i for i in range(1,51) if i % 2 == 0]
# print(l1)

#--- print values less thanand equal to 30
# l = [i for i in range(1,51) if i <= 30]
# print(l)

#--- print square root of 1 to 20
# l = [i**2 for i in range(1,21) ]
# print(l)

#--- print when i == 40, then its added by 5
# c = [i + 5 for i in range(1,51) if i == 40 ]
# print(c)

#--- print cube of cheks
# d = [i**3 for i in range(1,41) if i <= 40 and i >= 20]
# print(d)


# #--- print odd numbers in set:-
# s5 = {i for i in range(0, 51) if i % 2 != 0}
# print(s5)

#--- print value multiply by 5
# s = { k*5 for k in range(1,51) if (k <= 20 and k >= 10) or ( k <= 30 and k >= 20)}
# print(s)

#--- print value with adding it bt 10 and multyply bt 2
# s2 = {(i+10)*2 for i in range(10,40) if i <= 30 and i >= 20}
# print(s2)


#--- print alphabet ---2nd way
# d1 = {chr(96+i): chr(64+i) for i in range(1, 27)}
# print(d1)

# d2 = {chr(11+i): chr(21+i) for i in range(0,11)}
# print(d2)

#---- print valuse multiply by 10
# d = {i:i*10 for i in range(1,21)}
# print(d)

#--- print keys multiple by 2
# d3 = {i*2: i for i in range(40,101) if i <= 50}
# print(d3)

#---- print special characters ascii value keys
# d4 = {chr(42+i): chr(58+i) for i in range(1,7)}
# print(d4)

#---- star pattern


# for i in range(1,6):
#     print("*")

# for i in range(1, 6):
#     print("*" * 5)

# for i in range(1,5):
#     for j in range(1,5):
#         print("*" * 5)
#     print()

# for i in range(1,6):
#     for j in range(1,6):
#         print("*", end="")
#     print()

# s = {"*" * 2 for i in range(1,5)}  
# print(s)

#--- print pattern
# *
# **
# ***
# ****
# *****

# n = eval(input("Enter row:-"))
# for i in range(1,n +1):
#     print("*" * i)

#---- print pattern rectangle trangle
# *
# * *
# * * *
# * * * *
# * * * * *
# n = int(input("Enter the row:-"))
# for i in range(1,n + 1):
#     for j in range(1,i + 1):
#         print("*", end=" ")
#     print()

#---- print "*" pattern of 
# *
# * * *
# * * * * * *
# * * * * * * * * * *
# * * * * * * * * * * * * * * *

# a = int(input("Enter number of rows:- "))
# for i in range(1,a + 1):
#     for j in range(1,i + 1):
#         for k in range(1,j + 1):
#             print("*", end=" ")
#     print()


#---- WHILE LOOP ----#

# a = 5
# b = 10
# while a <= b:
#     print("yess")

#--- check a = 10 
# a = int(input("enter the number :- "))
# while a == 10:
#     print("done")

#---- cheack b is greater or not
# a = int(input("enter the first value:- "))
# b = int(input("enter the second number:- "))
# while a < b:
#     print("B is greater")











































