# there are two types of handling.
# -- file handling
# -- exception handling

# apan ne padha hai python is not compiled but hota hai vo compile but in background jo apan ko dhikta nahi hai
# actual me  python compile hota hai but vo backend me hota hai
# .py -- .pyc -- 
# .py matlab python file compile hoti hai .pyc file me  byt backend me hota hai vo .
# .pyc file matlab compiled code or compile code me convert karney wala compiler hotaa hai
# .py -- .pyc -- machine code(PVM convert karta hai machine code me compile code ko) -- binary code

## types of error
# -- Compile time error
# -- Run Time error
# -- Logical error

################COMPILE TIME 
# (jab python file(.py) convert hota hai compile code me tab error aata ahi ye)

##1.
# s = 10
# print(s  #SyntaxError

##2
# s = 10
#               print(s)  #IndentationError

######## RUN TIME ERROR
# jab python code ka execution ho rah ahai tab koi error aana usko runtime error boltey hai

##1.
# print(2//0) #ZeroDivisionError

##2.
# l1 = [1,2,3]  #IndexError
# print(l1[4])

##3.
# l = ()    #AttributeError
# l.append(10)

##4.
# for i in range(1,100000000000): # memory error
#     print (i)
# memory error jab aata hai jab aapki ram hi kaafi nahi hai uss function ko run karney ke liye

##5.
# how to open a file 
# f = open("file path")
#ex.
# f = open(r"D:\oops_concept\sampple.txt") # isko hamesha raw string hi lo kyoki \n apan ko apata hai new line hojata to kabhi slash ke baad n aa gya to vo as a new line consider karega
#ex.2 ( ab apan galat file dete hai)
# f = open("D:\oops_concept\sampple123.txt") #FileNotFoundError

#------------------------------------------------------------------------------------------------------------------------------------
# Python line by line execute hota hai to agar koi code me kuch galat ho gaya to aagey wala chalega hi nahi.
# Uska tarika hota hai ki agar ek code me problem aaye to dusra code uski vajah se nahi ruke
# ------------------------------------------------------------------------------------------------------------------------------------------------

# EXCEPTION HANDELING
#ex.1
# user_inp1 = int(input("enter the number"))
# user_inp2 = int(input("enter the number"))

# print(user_inp1//user_inp2)  # RISKY CODE(apan ko pata hai ki kuch galti hui to error raise kar skta hai isliye risky code bolenge isko)
# # aar iss code me apan kuch galti se string de dete hai to error de dega neeche wala code bhi nahi chalega 
# # to apan ko ye handel karna hai
# # agar apan dono integer dete hai fir sahi hai fir neeche waala loop bhi chlega
# # -----------------------------------------------------------
# # upar or neeche waaley code ka koi lena dena nahi hai 

# for i in range(1,11):
#     print("x" *i)
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#IMPORTANT POINT ----------------------------------------------------------------------------------------------------------------------------------------
#  jaise upar wala scene dheka to ye sab dikkat na ho baad wala code execute ho jaae runtime me koi problem nahi aaye isliye exception handeling use hogi.
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------

### what is abnormal terminantion?
# jaise abhi ho raha hai koi msg nahi kuch nahi code terminate ho raha hai galat values daalne se. To isko boltey hai abnornal termination.
# -------------------------------------------------------------------------------------------------------------------------------------------------

### what is normal termination?
# jab code poora execute ho jaae matlab upar ke question ko le to input bhi sahi diya integer me print ho gya and for loop bhi chal gaya poora usko normal termination bolenge.
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------------------------------------------------
# error 2 type ki hoti hai :-
# --  ek jisko apan handel kar saktye hai
# --  ddooasri jisko  hum handel nahi kar saktey hai
#### jo error hum handel kar saktey hai usse hum execption boltey hai

# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# #############EXCEPTION
## JO Error hum handel kar saktey hai usse hum exception kehtey hai
# try, except, else, finally

# how to handel exception ??
#ex.1
# user_input = int(input("eneter a digit"))
# user_input1 = int(input("eneter a digit"))

# try:
#     print(user_input//user_input1)
# except ZeroDivisionError as msg:     # apan ko idhar error likhna hai jo aa sakta hai as a developer humko pata rehna chiye ki konse error aa saktey hai
#     print(msg)     # this is called HANDLER STATEMENTS
# # except block me jab jaaega jab apan zero de denge apan ne upar zero division error de rakha hai.
# # jab koi error nahi aaega jab vo except block me jaaega hi nahi simple as that.
# # but ab neeche wala loop chal jaaega 
# # agar zero denge to error dega but neeche waala code execute hoga

# # -------------------------------------------
# for i in range(1,11):
#     print("*"*i)   

#ex.2 ( ab koi apney mann se msg ena hai)
# user_input = int(input("eneter the number"))
# user_input1 = int(input("eneter the number"))

# try:
#     print(user_input//user_input1)
# except ZeroDivisionError as msg:   # agar error aaye to
#     print("idhar zero matr doo") ## aaise mannn se bhi de saktye hai apan message 


# # ---------------------------
# for i in range(1,11):
#     print("*" * i)

# ab ye idhar normal termination ho gaya hai kyoki aagey waale code bhi execute ho rahe hai
#  ---------------question over------------------------------------------------------------------------------

# ab dheko jaise apnn string de dete hai to abnormal termination ho jaaega 
# koi neecghe wala code execute nahi hoga 
# kyoki apan ne usko sirf abhi zero divison wlal error hi de rakha hai .

#ex. ( jaise apan ne string de diya)
# u_inp = int(input("eneter a digit"))         
# u_inp1 = int(input("eneter a digit"))

# try:
#     print(u_inp//u_inp1)
# except ZeroDivisionError as msg:
#     print("zero mat do")
# except TypeError as msg:
#     print("sirf integer values do")
# # apan idhar multiple except bhi use kar saktey hai to apan type error ke liye bhi ek block baana denge 
# # ki agar galti se string de diya to vo abnormal termination na ho jaae neeche waala code execute hona chaiye hamesha


# # ---- ye neeche wala code apan example ke liye loikh rahe hai bas dhekne ke liye kab kkaam kar raha hai and kab nahi
# # -----------------------------------
# for i in range(1,11):
#     print("*"*i)   

# -------------------------question end ------------------------------------------------------------------------------------------------

# apan manually bhi error raise kar saktey hai
#ex.
# raise KeyError

# print(hello) # ye nahi hoga kyoki apan ne manually error raise kar rakha haai upar

#ex. (message bhi provide kar saktey hai)
# raise KeyError("not present")
# print("hello")

#ex.
# try:
#     raise KeyError("not present")
# except KeyError as msg:
#     print(msg)
# -----------------------------------------------------------------------------------------------------------

#ex.
# import pqr  # ModuleNotFoundError
# ---------------------------------------------------------------------------------------------------------------------

# to stop code execution
# import sys
# sys.exit()

#ex.
# while True:
#     user_input = input("eneter name")
#     if user_input == "rachit": # jab tak rachit nahi aaye break mat karo jab aaye fat se break kar do
#         break
#         # break se aagey waaley satement bhi honge execute
#         # matlab "hello " hoga execute 
#         # or sys.exit() se aagey ka kuch execute nahi hoga 
#         # dheko neeche wwaaley example me 

# print("hello")

#ex (sys.exit())
# import sys

# while True:
#     user_input = input("eneter name")
#     if user_input == "rachit":
#         sys.exit()

# print("hello") # hello execute hi nahi hora hai

#ex.
# import sys
# age = 17
# if age<18:
#     sys.exit("age less than 18")
# else:
#     print("age not less than 18")
# -----------------------------------------------------------------------------------------------------------------------------------------------

#ex.
# try:
#     inp1 = int(input("enter number"))
#     inp2 = int(input("enter another number"))
#     print("3rd line of final block")
# except ValueError as msg:
#     print("only integer values plzz")

# print("after")

# isme kya hora hai kahi bhi error aaega direct vo except me jaaega 
# or agar sahi dete hai sab to upar wala bhi print(3rd line wlaa) hoga and after
# ---------------------------------------------------------------------------------------------------------------------------------------

### ELSE ab
# except me jaata hao else me nahi jaaega.
# or agar except me nahi jaatata to 100 percent else me jaaega.


#ex.
# try:
#     print("in try block")
#     input1 = int(input("enter number")) 
#     input2 = int(input("enter number"))
# except ValueError as msg:
#     print("in except block")
#     print("integer do sirf")
# else:
#     print("in else block")
#     print(input1//input2)
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------
# NESTED TRY
# nested try ka ye matlab nahi hai9 ki try kr aanadr hi try rahega kahi bhi ho sakta hya

#ex.
# try:
#     print("in try")
#     u_inp1 = int(input("enter number")) # (SIRF CONVERSION HO RAHA HAI IDHAR)ab idhar apan assign kar rahe hai jab to vo error nahi dera
#     u_inp2 = int(input("enter number")) # matlab idhar abhi 0 bhi diya idhar error nahsi dega vo. Dikkat neeche else me aaegi kyoki vaha apan divide kar rehe hai
# except ValueError as msg:
#     print('in except')
#     print("enter integer onlyy")
# else:
#     print("in else")
#     try:
#         print(u_inp1//u_inp2) 

#     except ZeroDivisionError as msg:
#         print("zero mat doo")
# # ------------
# print("after")
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#FINALLY
# finally hamesha hi execute hoga alwaayyssssss
# finally iss kaam aata hai ki jaise apan ne koi try me file open kar li uspe operations perfome kar liye to usko close bhi karna hota hai.
# nahi to open hi rahegi and apni memory consume karegi bejabran.
# or ek reason or hai ki agar file eopen reh gayi to koi bhi developer aap=ka data dhek sakta hai

#ex.1
# try:
#     print("in try")
#     u_inp2 = int(input("enter number"))
#     u_inp1 = int(input("enter number"))
# except ValueError as msg:
#     print("in except")
#     print("integer values do")
# else:
#     print("in else")
#     try:
#         print(u_inp1//u_inp2)
#     except ZeroDivisionError as msg:
#         print("zero mat do idhar bosee")
# finally:
#     print("in finally block")
#     print("connnection is closed")

# # -----------------------------
# print("after")
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ---- Point to rembember --------------------------------------------------------------------------------------------------------------------------------
# agar aapney finally nahi likha to jaise aapney exception handel hi nahi kiya koi or exception aa raha hai to usme kya hoga aapki file close hi nahi hogi
# ---------------------------------------------------------------------------------------------- ------------------------------------------------------------------

# apan side by side bhi exception likh saktey hai dhekoo
#ex.
# try:
#     print(10//0)
# except (TypeError,ZeroDivisionError) as msg:
#     print("provide non zero and integer values")

#ex.2
# try:
#     print(10//"sd")
# except (TypeError,ZeroDivisionError,ValueError) as msg:
#     print("zero mat do and sirf integer hi do and  ")
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# EXCEPTION
# apan ko pata nahi ho error konsa aa raha hai to exception use kartey hai.
# exception har kisis error ka parent class hota hai
# directly bhi ho sakta hai and in directly bhi (dierctly matlab uska dirct parent indirectly means uske parent ke parent ka parent)
# ek base exception bhi hota hai jo exception ka bhi parent hota hai

# Sab ka MRO apan check kar saktey hai
# print(ZeroDivisionError.__mro__) #(<class 'ZeroDivisionError'>, <class 'ArithmeticError'>, <class 'Exception'>, <class 'BaseException'>, <class 'object'>)
# print(IndentationError.__mro__) #(<class 'IndentationError'>, <class 'SyntaxError'>, <class 'Exception'>, <class 'BaseException'>, <class 'object'>)
# print(ValueError.__mro__)  #(<class 'ValueError'>, <class 'Exception'>, <class 'BaseException'>, <class 'object'>)
# print(IndexError.__mro__) #(<class 'IndexError'>, <class 'LookupError'>, <class 'Exception'>, <class 'BaseException'>, <class 'object'>)

#ex.
# try:
#     lst = [1,2,3]
#     value = lst[5] # indexing error
#     print(10//0) # zerodivision error
# except Exception as msg:
#     print(msg)
    
#ex.2
# try:
#     print("a"* "a") #can't multiply sequence by non-int of type 'str'
#     print(10 + "abc") #unsupported operand type(s) for +: 'int' and 'str'
#     print(10//"a")  #unsupported operand type(s) for //: 'int' and 'str'
# except Exception as msg:
#     print(msg)

# EXCEPTION me dikkat ye hai ki user ke hisab se apn de nahi paaenge msg.
# upar ke examples me apan ne aaram se msg de diya but idhar nahi de paaenge
# isliye apan ek ek error hi manage karenge har baar 
# exception zyda use nahi karenge 

#ex. ( ye hi sahi way hai)
# try:
#     lst = [1,2,3]
#     v = lst[5]
#     print(10//0)
#     f = open("D:\oops_concept\sampple.txt", "r")
# except (IndexError,ZeroDivisionError.FileNotFoundError) as msg:
#     print("ye wala index hai hi nahi and zero mat do and file hai hi nhai ")

#ex.
# try:
#     lst = [1,2,3]
#     # c = lst[5]
#     # print(10//0)
#     f = open("D:\oops_concept\sampple.txtsd", "r")
# except IndexError as msg: # konse konse error aa skatye hai likhoo
#     print("index hai hi nahi ye")

# except ZeroDivisionError as msg:
#     print("zero mat do ")

# except FileNotFoundError as msg:
#     print(" ye file hai hi nahi")

# dheko apan ne exception handel kar liya hai to apan upar waala variable bhi use kar saktey hai dheko kaise
#ex.
# try:
#     lst = [1,2,3]
#     v = lst[6]
#     print(10//0)
#     print(20//v)
#     f = open("D:\oops_concept\sampple.txtsd", "r")
# except IndexError as msg:
#     print("sahi index do")
# except ZeroDivisionError as msg:
#     print("zero mat do")
# except FileNotFoundError as msg:
#     print("file hai hi nahi ")

# # ----------------dheko ab apan upar waali lst use kar rahe hai 
# print(lst)  #[1, 2, 3]
# print(lst*2)  #[1, 2, 3]
# ye sab koi local variable nahi hai sab global hai bas aap try except ke aandar unko lle ke kuch perfome kar rahe ho.
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ek or funda dheko EXCEPTION ka 
# jaisse apan ne exception saare errors ke upar de diya to exception hi saarye errors handel karega 
# dhekoo

#ex.
# try:
#     lst = [1,2,3]
#     v = lst[6]
#     print(10//0)
#     print(20//v)
#     f = open("D:\oops_concept\sampple.txtsd", "r")
# except Exception as msg:
#     print("sab ye hi handel karega neeche nahi jaaega kuch") # sab kuch is handeled by exception sabka parent hota hai kyoki
# except IndexError as msg:
#     print("sahi index do")
# except ZeroDivisionError as msg:
#     print("zero mat do")
# except FileNotFoundError as msg:
#     print("file hai hi nahi ")

# to iska tarika ye hai ki sab ke baad hi exception lagao saarey errors handel karney ke baad
#ex.
# try:
#     lst = [1,2,3]
#     v = lst[6]
#     print(10//0)
#     print(20//v)
#     f = open("D:\oops_concept\sampple.txtsd", "r")
# except IndexError as msg:
#     print("sahi index do")
# except ZeroDivisionError as msg:
#     print("zero mat do")
# except FileNotFoundError as msg:
#     print("file hai hi nahi ")
# except Exception as msg:
#     print("idhar lagao ")
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#COMBINATIONS 
#ex.1 (sahi)
# try:
#     pass
# except:
#     pass

#ex.2 (galat)
# try:
#     pass
# else:
#     pass

#ex.3(sahi)
# try:
#     pass
# finally:
#     pass

#ex.4 (galat)
# try:
#     try: # try ke sath apan sirf try use nahi kar saktey 
#         pass
# except:
#     pass

#ex.5 (sahi)
# try:
#     try:
#         pass
#     except:
#         pass

## bhot saarey hotey hai durga notes me dhek lo isko
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ASSERT statement
# aapkey expectations kya hai and actual me kya ho raha hai assert ka matlab hota hai

#ex.
# assert 2 == 3 #AssertionError
# left wla expected value and right wlaa actual value

#ex.
# assert True # true aya to thik hai
# assert False  #AssertionError(false aaya to error raise ho jaaega assert ye hota hai)

#ex. (msg dena hai jaise)
# assert False, "Invalid"  #AssertionError: Invalid

#ex.
# VALUE ="rachit"
# user_input = (input("enter a name")) 
# assert VALUE == user_input # rachit ki jagah kuch or denge to error raise kar dega 
                           # rachit ki jagah kuch bhi de diya to assertion error de 

#ex. msg bhi de saktey hai 
# VALUE = "rachit"
# user_input = input("eneter a name")
# assert VALUE == user_input, "rachit hi do udhar"

#ex.
# x = 7    
# y = 1    
# # It uses assert to check for 0     
# print ("x / y value is : ")     
# assert y != 0, "Divide by 0 error"    
# print (x / y)     

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# CUSTOM EXCEPTION / USER DEFINED EXCEPTION
# --  kuhud se error bananan
# -- custom exception banane ke liye inherit karna padehga EXCEPTION ko 

#EX.
# class CustomError(Exception): # ye apan ne naya error bana diya
#     pass


# raise CustomError("invalidd") #CustomError: invalidd

#ex.2
# class HelloError(Exception):
#     pass

# raise HelloError("maamle complex hai")

#ex. ISKO HANDEL KARNA
# class HelloError(Exception):
#     pass

# try:
#     raise HelloError("invalid hello")
# except HelloError as msg:
#     print(msg)

#ex.
# class InvalidAgeException(Exception):
#     pass
# number = 18
# try:
#     input_age = int(input("enter age"))
#     if input_age < number:
#         raise InvalidAgeException
#     else:
#         print("eligible to vote")
# except InvalidAgeException as msg:
#     print("Invalid age exception occured")

# # ------
# print("handel hoo raha hai ")

#ex.
# dct = {"keychain":25,"pen":10,"pencil":90}

# class ProductValueTooLarge(Exception):
#     pass

# def check_value(d):
#     for key,value in d.items():
#         if value > 100:
#             raise ProductValueTooLarge("value of product is more than 100rs")
#         else:
#             print("product value perfect")

# dct = {"keychain":25,"pen":10,"pencil":90,"rubber":1000}

# try:
#     check_value(dct)
# except ProductValueTooLarge as msg:
#     print(msg)

#ex.

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------







    







