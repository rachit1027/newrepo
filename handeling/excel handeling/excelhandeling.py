#  import openpyxl
# how to install openpyxl?
# -- pip install openpyxk

# how to check apney pass kitti liabrary hai ?
#-- pip freeze

# how to un-install liabrary?
#-- pip uninstall (library name) openpyxl

# how to install specific version?
# -- pip install openpyxl == (version name) 3.1.2

# dheko excel ek workbook ho gayi jisme apan operations kar skatey hai isliye usko wrkbook boltey hai
# to ab apan ko pyhton ke through kuch bhi karna hai to kaisee karey excel me.

#ex.
# from openpyxl import Workbook, load_workbook
# FILE_PATH = r"D:\oops_concept\handeling\sample_excel.xlsx"

#ex. (data kaise daaley)
# wb = Workbook() # workbook ka object crete kar liya
# activesheet = wb.active  # workbook ke anadar sheet hota hai to pehla sheet jab open hota hai usko active sheet boltey hai (iska naam sheet rahega python se banaenge to)
# activesheet.cell(row=1,column = 1).value = "Python"
# wb.save(filename = "D:\oops_concept\handeling\sample_excel.xlsx") #creating a worbook  ( ye yaad rakhna aakhri me xlsx de dena varna kuch kaam nahi krega)

#ex. (doosra tarika)
# wb = Workbook()
# active_sheet = wb.active
# active_sheet.cell(row =2 ,column = 2).value = "Python" # pehla upar wla tarika 
# active_sheet.cell(row=1,column=1,value="JAVA") # doosra tarika
# wb.save(filename="D:\oops_concept\handeling\sample_excel.xlsx")
# AB YE BAAT HO GAYI FILE ME WRITE KARNEY KE LIYE.
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Ab koi existing file ko open karna hai to 
# to apan ko openpyxl se ek or cheez import karni padegi vo hai (load_worbook)
# or isko filename bhi lagta hai 2b = load_workbook(filename = "filepath de do idhar")

# FILE_PATH = r"D:\oops_concept\handeling\sample_excel.xlsx" # apan ne path ka variable bana liya hai

# wb = load_workbook(filename= FILE_PATH)
# activesheet = wb.active
# activesheet.cell(1,1,"EMPID")
# activesheet.cell(1,2,"empname")
# activesheet.cell(1,3,"empage")

# wb.save(FILE_PATH) # yaha pe save karna bhi zaruri hai filepath ke saath
# and ye koi data override nahi karega kkyoki apan bas read kar rahe hai.

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# import time


# FILE_PATH = r"D:\oops_concept\handeling\sample_excel.xlsx"

# wb = Workbook()
# activesheet = wb.active
# activesheet["A1"] = 87
# activesheet["A2"] = "rachit"
# activesheet["A3"] = "33.3"
# activesheet["A4"] = 10

# now = time.strftime("%x")
# activesheet["A5"] = now

# wb.save(FILE_PATH)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ab jaise multiiple data apan ko upload karna hai (WRITE) 

# FILE_PATH = r"D:\oops_concept\handeling\sample_excel.xlsx"

# wb = Workbook()
# activesheet  = wb.active

# data = (
#     (1,2,3),
#     (4,5,6),
#     (7,8,9),
#     ("rachit","bose","OM")
# )

# for i in data:
#     activesheet.append(i)

# wb.save(FILE_PATH)
# IMP POINT
# jaise sheet me pehle se hi data hai to vo aagey vaale row me jaa ke appen karega usko override nahi karega)
# and list or iska append bhot diffrent hai confuse mat hona.
# #####

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ab data read karna hai apan ko 
# FILE_PATH = r"D:\oops_concept\handeling\sample_excel.xlsx"
# wb = load_workbook(filename=FILE_PATH)
# activesheet = wb.active

# x1 = activesheet["A1"]
# x2 = activesheet['A2']
# x3 = activesheet.cell(row=3,column=1) #same hi hora hai upar jaise bas isme cell function liya hai

# print("the first cell value",x1.value)
# print("the first cell value",x2.value)
# print("the first cell value",x3.value)

# ------------------------------------------------------------------------------------------------------------------------------------------------
 
# ab multiple data read karna hai 
# to ab me practise ke iye multiple write karungaa fir read

# FILE_PATH = r"D:\oops_concept\handeling\sample_excel.xlsx"
# w = Workbook()
# activesheet = w.active

# data = (
#     (1,2,3),
#     (4,5,6),
#     (7,8,9)
# )

# for i in data:
#     activesheet.append(i)

# w.save(FILE_PATH)  # multiple data bana diya hai apan ne 

# ------ ab apan pehele ek ek data read kartey hai

# FILE_PATH = r"D:\oops_concept\handeling\sample_excel.xlsx"
# w = load_workbook(filename=FILE_PATH)
# activesheet = w.active
# x1 = activesheet.cell(row=1,column=2)
# x2 = activesheet.cell(row=2,column=2)
# x3 = activesheet.cell(row=3,column=2)

# print("row 1 data and colum 2 is",x1.value)
# print("row 2 data and colum 2 is",x2.value)
# print("row 3 data and colum 2 is",x3.value)
# - apan ne ek ek data to read kar liya 

# -- multiplle data read karney se pehle apan usme data or daal dete hai 
# FILE_PATH = r"D:\oops_concept\handeling\sample_excel.xlsx"
# wb = load_workbook(filename=FILE_PATH)
# activesheet = wb.active
# activesheet.cell (row = 4,column=4,value ="rachit")
# activesheet.cell (row = 5,column=4,value ="dubey")
# activesheet.cell (row = 6,column=4,value ="yes sir")

# wb.save(FILE_PATH)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


