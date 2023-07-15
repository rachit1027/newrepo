# how to read a text file in python ?
# -- pehele ek avriable assign karo.
# f = open()
# open ko basically 2 arguments lagtey hai file and mode
# -- file = konsi file open karni hai
# -- mode = rear(r), write(w),append(a),readbytes(rb),writebytes(wb),r+,w+
# ye saarey modes hootey hai
# ek point important hai jaise agar koi file me kuch likhna hao to write se to overwrite ho jata hai vo  to append use karna hoga koi bhi existing file me kuch add karney ke liye.


#jaise kuch read karna ho to kaise karey?
# FILE_PATH = r"D:\oops_concept\filehandel_sample.txt" # humney isko raw string bana diya hai ki koi bhi escape sequence work na katrey galti se
# f = open(FILE_PATH,"r",encoding='utf-8') # r matlab read de diya apn ne mode
# data = f.read()
# print(data)

# apan file ko ek hi baar read kar saktey hai. agar avapas rerad karna hai to vapas open karo usko.
# FILE_PATH = r"D:\oops_concept\filehandel_sample.txt"
# f = open(FILE_PATH,"r",encoding= 'utf-8')
# data  = f.read()
# data1 = f.read() # nahi hogaa
# print(data)

#
# FILE_PATH = r"D:\oops_concept\filehandel_sample.txt"
# f = open(FILE_PATH,"r",encoding= 'utf-8')
# data  = f.read()
# print(data)
# f = open(FILE_PATH,"r",encoding='utf-8')  # open karo vapas fir aa jaaega
# data1 = f.read() 
# print(data1)

# file readable hai ki nahi cheak karna.
# FILE_PATH = r"D:\oops_concept\filehandel_sample.txt" 
# f = open(FILE_PATH,"r",encoding='utf-8')
# print(f.readable())   #True

# file writeable hai ki nahi check karna.
# FILE_PATH = r"D:\oops_concept\filehandel_sample.txt" 
# f = open(FILE_PATH,"r",encoding='utf-8')
# print(f.writable()) #False
# False dega kyoki apan ne upar mode abhi read de rakha hai

#file closed hai ki open ?
# FILE_PATH = r"D:\oops_concept\filehandel_sample.txt" 
# f = open(FILE_PATH,"r",encoding='utf-8')
# print(f.closed) # False aaega kyki apan ne close nahi ki hai abhi
# f.close()
# print(f.closed) # True aaega kyoki apan ne upar band kar di hai file

# READLINE (ek ek line read karta hai ye) dheko
# FILE_PATH = r"D:\oops_concept\filehandel_sample.txt" 
# f = open(FILE_PATH,"r",encoding='utf-8')
# data = f.readline()
# print(data) # pehli line read kar li us para ki
# data = f.readline()
# print(data) # doosri line read kar li
#jab saari lines khatam ho jaaengi to vo blank dhikhane lagega

#READLINES (ye list of lines dega)
# FILE_PATH = r"D:\oops_concept\filehandel_sample.txt" 
# f = open(FILE_PATH,"r",encoding='utf-8')
# data = f.readlines()
# print(data)
# print(len(data)) # list me jitte bhi lines hai vo bata dega

# ------------------------------POINT TO REMBEMBER --------------------------------------------------------
# read ek hi baar hoga uske baad aapko vapas open karna padega vo file ko.
# chahe ho readlines ho, readline ho kuch bhi ho
# ------------------------------------------------------------------------------------------------------------------------------

# get the number of words.
# FILE_PATH = r"D:\oops_concept\filehandel_sample.txt"
# f =  open(FILE_PATH, "r", encoding='utf-8')


# def get_thewords():
#     f = open(FILE_PATH,"r",encoding='utf-8')
#     return len(f.read().split())

# print(get_thewords())

# get the number of lines.
# FILE_PATH = r"D:\oops_concept\filehandel_sample.txt"

# def get_lines():
#     f = open(FILE_PATH,"r",encoding='utf-8')
#     return len(f.readlines())

# print(get_lines())

# ab koi specific word chaiye ki kitti baar aaya hai vo para me.
# FILE_PAth = r"D:\oops_concept\filehandel_sample.txt"
# def occurances(word):
#     f = open(FILE_PAth,"r",encoding='utf-8')
#     return f.read().split().count(word)
# print(occurances("the")) # yaha pe dikkat ye hai ki case sensictive hota hai to big lettres wala nahi dhikaega idhar

#solve kaise kare ki jaise bade chote sab dhika de ye 
# FILE_PATH = r"D:\oops_concept\filehandel_sample.txt"
# def occurances(w):
#     f = open(FILE_PATH,"r",encoding='utf-8')
#     lst = f.read().split()
#     n_lst = []
#     for word in lst:
#        n_lst.append(word.lower())
#     print(n_lst.count(w))
# occurances("the")

# same question upar wala bina dheke
# FILE_PATH = r"D:\oops_concept\filehandel_sample.txt"
# def occurances(w):
#     f = open(FILE_PATH,"r",encoding='utf-8')
#     lst = f.read().split()
#     new_lst = []
#     for word in lst:
#         new_lst.append(word.lower())
#     print(new_lst.count(w))
# occurances("the")

#without using count
# FILE_PATH = r"D:\oops_concept\filehandel_sample.txt"
# def occurance(w):
#     f = open(FILE_PATH,"r",encoding='utf-8')
#     lst = f.read().split()
#     counter = 0
#     for word in lst:
#         if word == w:
#             counter += 1
#     print(counter)
    
# occurance("The") # isme case sensitive wala scene a jaaega

# ab dono ke liye acse sensitive ans in sensitive.
# FILE_PATH = r"D:\oops_concept\filehandel_sample.txt"
# def occurance(w,case_sen = True):
#     f = open(FILE_PATH,"r",encoding = 'utf-8')
#     lst = f.read().split()
#     if case_sen:
#         counter = 0
#         for word in lst:
#             if word == w:
#                 counter =+1
#         print(counter)
#     else:
#         counter = 0 
#         final_lst = list(map(lambda word:word.lower(),lst))
#         for word in final_lst:
#             if word == w.lower():
#                 counter += 1
#         print(counter)

# occurance("the",case_sen=False)

#saarey numbers mikalo para se.
# FILE_PATH = r"D:\oops_concept\filehandel_sample.txt"
# def get_number():
#     f = open(FILE_PATH,"r",encoding='utf-8')
#     lst = f.read().split()
#     numberlst = []
#     for word in lst:
#         if word.isdigit():
#             numberlst.append(int(word))
#     print(numberlst)

# get_number()

# ab sum of saarey numbers chaiye
# FILE_PATH = r"D:\oops_concept\filehandel_sample.txt"
# def getnumber_add():
#     f = open(FILE_PATH,"r",encoding='utf-8')
#     lst = f.read().split()
#     new_lst = []
#     for word in lst:
#         if word.isdigit():
#             new_lst.append(int(word))
#     print(sum(new_lst))

# getnumber_add()

#koi particular line chaiye para me se to
# FILE_PATH = r"D:\oops_concept\filehandel_sample.txt"
# def get_line():
#     f = open(FILE_PATH,"r",encoding='utf-8')
#     lst = f.readlines()
#     print(lst[3])
# get_line()

# dheko ab exception bhi handel kar rahe hai 
# FILE_PATH = r"D:\oops_concept\filehandel_sample.txt"
# def get_line():
#     f = open(FILE_PATH,"r",encoding='utf-8')
#     try:
#         lst = f.readlines()
#         print(lst[10])
#     except  IndexError as msg:
#         print("Index value sahi do please")

# get_line()

# ab apan ko ek ek line split l
# FILE_PATH = r"D:\oops_concept\filehandel_sample.txt"
# f = open(FILE_PATH,"r",encoding='utf-8')
# lst = f.readlines()
# splst = lst[3].split()
# print(splst)

#ab saari lines ek ek kar ke split
# FILE_PATH =r"D:\oops_concept\filehandel_sample.txt"
# f = open(FILE_PATH,"r",encoding='utf-8')
# alllines = f.readlines()
# for line in alllines:
#     splitedlines = line.split()
#     print(splitedlines)

#vdo 38 58.20 min

# FROM BEGINNING

#how to open a file
# f =  open()

# methods
# read(r), write(w), append(a)

#ex.
FILE_PATH = r"D:\oops_concept\handeling\filehandel_sample.txt"
# f = open(FILE_PATH,"r",encoding='utf-8')
# data = f.read()
# f = open(FILE_PATH,'r',encoding='utf-8') # wapas open karna padega fir open hoga vo
# data1 = f.read()
# print(data)

# print(f.readable()) # vo dtat readable hai ki nahi  #Trur
# print(f.writable()) # vo writeable hai ya nahi to apan ne abhi "r" de rakha hai false aaega. #False
# print(f.closed) # file close hai ya nahi #False 
# f.close()
# print(f.closed) # upar close kar diya isliye ab True dega # True

# ab apan line read kar rahe hai ek ek kar ke
# data1 = f.readline()
# print(data1) # ek ek line read karega
# data1 = f.readline()
# print(data1)
# data1 = f.readline()
# print(data1)
# data1 = f.readline()
# print(data1)

# ab apan ko list me chaiye to
# data2 = f.readlines()
# print(data2) #list me de dedega
# print(len(data2)) #8 lines hai 


# ab one by one line print karte hai 
# data4 = f.readlines() # list aa gayi
# for i in data4:
#     print(i) # one by one eline dedega

#ab agar single single word chiye ho to
# data5 = f.read()
# print(data5.split()) # ek ek word aa gye
# for i in data5:
#     print(i)

# kitte words hai?
# data = f.read()
# print(len(data.split()))

# nahi to function bana lo
# def words():
#     data = f.read()
#     return len(data.split())

# print(words())

# ab number of lines ke liye function

# def get_lines():
#     f = open(FILE_PATH,"r",encoding='utf-8')
#     data = f.readlines() # list de di
#     return len(data)

# print(get_lines())

# ab koi specific word chaiye
# def occurances():
#     f = open(FILE_PATH,"r",encoding='utf-8')
#     data = f.read().split()
#     print(data)
#     counter = 0
#     for word in data:
#         if word == "the":
#             counter += 1
#     print(counter)
# occurances()

# ab count use kar ke 
# def occurances(word):
#     f = open(FILE_PATH,"r",encoding='utf-8')
#     return  f.read().split().count(word)
 

# print(occurances("the"))

# ab "The" count kartey
# def occurances(word):
#     f = open(FILE_PATH,"r",encoding="utf-8")
#     return f.read().split().count(word)
# print(occurances("The"))

# ab apan ko saaret the chiye "the" bhi and "The" bhi
# def occurances(word):
#     f =open(FILE_PATH,"r",encoding='utf-8')
#     return f.read().lower().split().count(word)

# print(occurances("the"))

# ab vahi cheez bina count ke
# def occurances(word):
#     f= open(FILE_PATH,"r",encoding="utf-8")
#     data = f.read().lower().split()
#     counter = 0
#     for word in data:
#         if word == "the":
#             counter += 1
#     print(counter)

# occurances("the")       

#ab jaise koi new list me append karna hai
# def occurances(w):
#     f = open(FILE_PATH,"r",encoding="utf-8")
#     lst = f.read().lower().split()
#     newlst = []
#     for word in lst:
#         if word == "the":
#             newlst.append(word)
#     print(newlst)

# occurances("the")

# ab new list se count karna hai apan ko word
# def occurance(w):
#     f = open(FILE_PATH,"r",encoding="utf-8")
#     lst = f.read().lower().split()
#     print(lst)
#     newlst = []
#     for word in lst:
#         if word == "the":
#             newlst.append(word)
#     print(len(newlst)) # print(newlst.count(w)) # dono tarike se kar skatey hai

# occurance("THE")
# occurance("the")
# occurance("THe") # kaise bhi do sab aa jaaega 

#MAP----------------------------------------------------------------------------------------------------------------------------------------------
# MAp requires a function and a iterable
# a = [10,20,30,40,50]
# def inc(n):
#     return n+2

# result = list(map(inc,a))
# print(result) #<map object at 0x0000013511F3ED00>
# print(type(result)) #<class 'map'>
# for i in result:
#     print(i)

# upar waali cheez hi lambda use kar ke
# a = [10,20,30,40,20]
# result = list(map(lambda n : n+2,a))
# for i in result:
#     print(i)

# ab jaise 2 list add karn hai
# a = [10,20,30,40,50]
# b= [1,2,3,4,5] # elements same honey chaiye
# result = list(map(lambda n,m:n+m,a,b))
# for i in result:
#     print(i)
# # ----------------------------------------------------------------------------------------------------------------------------------------------------------

# back to file haneling
# upar wla question hi karna hai thoda optimize
# MAP use kar ke 
# def occurance(w):
#     f = open(FILE_PATH,"r",encoding="utf-8")
#     lst = f.read().split()
#     final_lst = list(map(lambda word: word.lower(),lst)) # bas yaha pe lower me convert kar rahe hai upar waali list ko or kuch nahi
#     # print(final_lst)
#     print(final_lst.count(w.lower())) # ye bas user ke liye kiya hai kyoki vo kaise bhi pass kar sakta hai

# occurance("the")

#ab apan case sensitive and in sensitive banatey hai
# def get_word_occ(w,casesen = True):
#     if casesen == False:
#         f = open(FILE_PATH,"r",encoding='utf-8') # incase sensitive
#         lst = f.read().lower().split() # matlab kuch bhi do aa jaaega
#         print(lst)
#         flst = []
#         for word in lst:
#             if word == w:
#                 flst.append(word)
#         print(flst)
#         print(len(flst))   
#     else:
#         f = open(FILE_PATH,"r",encoding="utf-8") # ye case sensitive ke iye
#         lst = f.read().split()
#         counter = 0
#         for word in lst:
#             if word == w:
#                 counter += 1
#         print(counter)     

# get_word_occ("the",casesen=False)
# get_word_occ("the",casesen=True)

# ab upar wla code kaise optimize kar saktey hai
# def get_word_occ(w,case_Sen=True):
#     f = open(FILE_PATH,"r",encoding='utf-8')
#     lst = f.read().split()

#     if case_Sen:
#         final_lst = lst
#     else:
#         final_lst = list(map(lambda word : word.lower(),lst))
#         w = w.lower()
#     counter = 0
#     for word in final_lst:
#         if word == w:
#             counter =+ 1
#     print(counter)

# get_word_occ("The",case_Sen=True)

#ab kya apan ko poore para me jitte number hai vo chiye 
# def get_num():
#     f = open(FILE_PATH,"r",encoding='utf-8')
#     lst = f.read().split()
#     for n in lst:
#         if n.isdigit():
#          print(n)
# get_num()

#ab sab kki addition chaiye
# def get_num():
#     f = open(FILE_PATH,"r",encoding='utf-8')
#     lst = f.read().split()
#     nlst = []
#     for n in lst:
#         if n.isdigit():
#           nlst.append(int(n))
#     print(sum(nlst))
# get_num()

# ab koi specific liine chaiye
# def get_spec_line(l):
#     f = open(FILE_PATH,"r",encoding='utf-8')
#     try:
#         lst = f.readlines()[l-1]
#     except IndexError as msg:
#         print("index sahi do plzz")
#     else:
#         print(lst)

# get_spec_line(10)
# dheko ab isme kya hora hai ki jab apan index galat denge to koi lst banegi hi nahi
# lst banaega hi nahi to vo unbound error dedega 

# ab jaise ek ek line split karna hai 
# def split_line():
#     f = open(FILE_PATH,"r",encoding='utf-8')
#     lst = f.readlines()
#     splitline = lst[3].split()
#     print(splitline)

# split_line()

# ab saari line ek saath split karni hai to
# def split_line():
#     f = open(FILE_PATH,"r",encoding='utf-8')
#     lst = f.readlines()
#     # print(lst)
#     for line in lst:
#         print(line.split())

# split_line()

# ab apan ko ye karna hai ki pehle line me "the" kitti baar aaya doosrey me kitti baar aaya aaise karna hai 
# def get_wword_occ_for_lines():
#     f = open(FILE_PATH,"r",encoding='utf-8')
#     all_lines = f.readlines()
#     for line in all_lines:
#         single_sp_line = line.split()
#         print(single_sp_line.count("The"))
# get_wword_occ_for_lines() 

# ab dictionary me chaaiye 
# def indict(w):
#     f = open(FILE_PATH,"r",encoding='utf-8')
#     all_lines = f.readlines()
#     final_dict = {}
#     counter = 1 # kyoki lines 1 se chalu hoti hai
#     for line in all_lines:
#         single_sp_line = line.split()
#         # print(single_sp_line)
#         final_dict[counter] = single_sp_line.count(w)
#         counter += 1
#     print(final_dict) 

# indict("the")

# waps upar wala question repeat 
# def indict(w):
#     f = open(FILE_PATH,"r",encoding='utf-8')
#     all_lines = f.readlines()
#     final_dict = {}
#     counter =1
#     for line in all_lines:
#         single_sp_line = line.split()
#         final_dict[counter] = single_sp_line.count(w)
#         counter += 1
#     print(final_dict)

# indict("the")

# get word with sub stringg
# jaise jiss word me "in" hai vo chiye
# def get_word_by_sub(subs):
#     f = open(FILE_PATH,"r",encoding='utf-8')
#     all_words = f.read().split()
#     for word in all_words:
#         if subs in word:
#             print(word)

# get_word_by_sub("in")

#jaoise upar waale isme "in" bhi aaega to sirf jiss word ke aandar "in" aata hai vo chaiye 
# def getin(subs):
#     f = open(FILE_PATH,"r",encoding='utf-8')
#     all_words = f.read().split()
#     for word in all_words:
#         if subs in word:
#             if subs != word:
#                 print(word)

# getin("in")

# ab jaise repeated words nahi chaiyye
# def get_sub_strings(subs):
#     f = open(FILE_PATH,"r",encoding='utf-8')
#     all_words = f.read().split()
#     lst_ofsub = []
#     for word in all_words:
#         if subs in word:
#             if subs != word: # len same nahi hai "in" nahi aaega isme
#                 if word not in lst_ofsub:
#                     lst_ofsub.append(word)
#     print(lst_ofsub)

# get_sub_strings("in") 

#ab jo word t se start ho raeh hai vo chiye
# def get_words_start_with_t():
#     f = open(FILE_PATH,"r",encoding='utf-8')
#     all_words = f.read().split()
#     # print(all_words)
#     for word in all_words:
#         if word[0] == "t":
#             print(word)

# get_words_start_with_t()

# saarey special character hataney ke liye?

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#WRITE

# fw = open(FILE_PATH,"w") 
# fw.write("hello\n")
# fw.write("my\n")
# fw.write("name\n")
# fw.write("is\n")
# fw.write("rachit\n")

# fw = open(FILE_PATH,"w") 
# while True:
#     u_inp = input("enter a name")
#     if u_inp == "exit":
#         break
#     fw.write(u_inp + "\n")

# fw = open(FILE_PATH,"a") # append diya hai idhar to aagey se append hoga
# while True:              # override nahi hoga data
#     u_inp = input("Enter a name")
#     if u_inp == "exit":
#         break
#     fw.write(u_inp+"\n")

#writelines (isko iterables chiaye hotey hai )

# fw =open(FILE_PATH,"a") #(FILE_PATH,"w")
# fw.write("ID \t\t\t\tName\t\t\t\tAge\t\t\t\tSalary\n")
# fw.writelines(["101\t\t\t\tABCD\t\t\t\t23\t\t\t\t25k\n"])
# fw.writelines(["102\t\t\t\trachit\t\t\t\t23\t\t\t\t20k\n"])
# fw.writelines(["103\t\t\t\thoney\t\t\t\t23\t\t\t\t55k\n"])

#Context Manager -- responsible for opening file and closing file 
#WITH 
# file kabhi bhi open nahi rehni chaiye kypki galti se koi neeche access kar le usko to code me dikkat aa sakti hai 
# with open(FILE_PATH,"r") as f:
#     print(f.read())
#     print(f.closed)#False(close nahi hai) # file close hai ki nahi ye check kar rahe hai apan
#     # to abhi to open dhikaega kyoki apan with ke aandar check kar rahe hai
#     # agar with ke bahar check karenge to close hi bataega matlab False
# print(f.closed) #True (ha close ho gayi)

# class ke saath ek question.
# class Employee:
#     def __init__(self,eid,ename,esal):
#         self.EmpID = eid
#         self.EmpName = ename
#         self.Empsal = esal

# e1 = Employee(eid=101,ename='A',esal=25000)
# e2 = Employee(eid=102,ename='B',esal=35000)
# e3 = Employee(eid=103,ename='C',esal=45000)
# e4 = Employee(eid=104,ename='D',esal=55000)
# e5 = Employee(eid=105,ename='E',esal=65000)

# lst = [e1,e2,e3,e4,e5]

# FILE_PATH = r"D:\oops_concept\handeling\filehandel_sample.txt"
# # fw = open(FILE_PATH,"w")
# # # fw.write("ID\t\t\tName\t\t\tSalary\n")
# # for emps in lst:
# #     fw.write(f"{emps.EmpID}\t\t\t{emps.EmpName}\t\t\t{emps.Empsal}\n")  
# # using context manager
# with open(FILE_PATH,"a") as fw:
#     for emp in lst:
#         fw.write(f"{emp.EmpID}\t\t\t{emp.EmpName}\t\t\t{emp.Empsal}\n")

# context manager me 2 important method hai
# -- __enter__(opening the file)
# -- __exit__(closing the file)

# structure of context manager
# class ContMan: # ye kisi ka child nahi rahega
#     def __init__(self):
#         print("in init ") # PEHLE ISKE PASS JAAEGA #1ST

#     def __enter__(self): # dusRA ISKE PASS SAAREY METHODS JO HONGEY EXECUTE KAREGA #2ND
#         print("in enter")

#     def __exit__(self): # FIR SAB HONEY KE BAAD EXIT KAR DEGA #3RD
#         print("in exit")

# with ContMan() as test:
#     print("in with")

# JAB APAN ConMan( execute karenge abhi to errr dega kyoki exit ko 4 arguments chaiye hotey hai)
# exception type, exception value, exception traceback

#dheko
# class ContMan: # ye kisi ka child nahi rahega
#     def __init__(self):
#         print("in init ") # PEHLE ISKE PASS JAAEGA #1ST

#     def __enter__(self): # dusRA ISKE PASS SAAREY METHODS JO HONGEY EXECUTE KAREGA #2ND
#         print("in enter")

#     def __exit__(self,exp_type,exp_val,exp_traceback): # FIR SAB HONEY KE BAAD EXIT KAR DEGA #3RD
#         print("in exit")

# with ContMan() as test:
#     print("in with")

# exit ko 4 arguments de diye to aa gaya (sahi se pprin ho gaya ).

#ab upar apan ne structure dheka an actual use kartey hai dheko.

# class FileManager: # ye kisi ka child nahi rahega
#     def __init__(self,filepath,filemode):
#         self.FilePath = filepath
#         self.FileMode = filemode

#     def __enter__(self): # yaha pe aapn apni file open kartey hai
#         self.file = open(self.FilePath,self.FileMode)
#         return self.file

#     def __exit__(self,exc_type,exc_val,exc_traceback): # FIR SAB HONEY KE BAAD EXIT KAR DEGA #3RD
#         self.file.close()

# with FileManager(FILE_PATH,"r") as f:
#     print(f.read())







