# COMMA SEPERATED VALUES
# ye lightweight hota hai 
# to isko download karney ki zarurat nahi hoti
# direct import kar saktey hai isko

import csv
#READ (reader)
# FILE_PATH = r"D:\oops_concept\handeling\csv handeling\B9_csv.csv.txt"
# with open(FILE_PATH,"r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row) # list me output deta hai ye

#WRITE (writerow)
FILE_PATH = r"D:\oops_concept\handeling\csv handeling\B9_csv.csv.txt"
# with open(FILE_PATH,"w",newline="") as file:
    # writer = csv.writer(file)
    # writer.writerow(["SN","Movie","Hero"]) # ab jaise read kartey samey list me data aa raha hai write kartey samey bhi list hi dena padega
    # writer.writerow([1,"harry potter","daniel"])
    # writer.writerow([2,"dilwale","shahrukh"])

#WRITE(writerows) #isko ek saath list of list dedo
# agar kabhi list of ist hai usko write karna hai ek saath to ye use karo
# csv_rowlist = [["SN","Movie","Hero","Year"],[1,"Herry Potter","Daniel",2022],[2,"Dilwale","Shahrukh",2021],[3,"Kabirsingh","shahid",2022],[4,"Piku","irfan",2021],[5,"YJHD","ranbir",2022],[6,"Dilwale","shahrukh",2021]]
# with open(FILE_PATH,"w",newline="") as file:
#     writer = csv.writer(file)
#     writer.writerows(csv_rowlist)

#DICT READER (directly dictionary de degi)
# with open(FILE_PATH,"r") as file:
#     csv_file = csv.DictReader(file)
#     for row in csv_file:
#         print(row)

# ab jo dta hai apan ko uspe ooperations karna hai
# with open(FILE_PATH,"r") as file:
#     csv_file = csv.DictReader(file)
#     for row in csv_file:
#         if row ["Movie"] == "YJHD":
#             print(row)

#ek or example (nahi ho raha dheko ek baar isko)
# with open(FILE_PATH,"r") as file:
#     hellofile = csv.DictReader(file)
#     for row in hellofile:
#         if row["Movie"] == "Dilwale" and row["Year"] == 2021:
#             print(row)

#DICTIONARY writer
# with open(FILE_PATH,"w",newline="") as file:
#     fieldnames = ['player_name',"rating"] # headers
#     writer = csv.DictWriter(file,fieldnames=fieldnames) 

#     writer.writeheader() # header chale gaye idhar
#     writer.writerow({"player_name":"Rachit","rating":2020})
#     writer.writerow({"player_name":"BOney","rating":2021})
#     writer.writerow({"player_name":"suddi","rating":2022})

# ek or fopr practise
# with open(FILE_PATH,"w",newline="") as file:
#     field_names = ['player_name',"player_age"]
#     writer = csv.DictWriter(file,fieldnames=field_names)

#     writer.writeheader()
#     writer.writerow({"player_name":"rachit","player_age":10})
#     writer.writerow({"player_name":"bones","player_age":10})
#     writer.writerow({"player_name":"honey","player_age":10})
#     writer.writerow({"player_name":"vinni","player_age":10})
#     writer.writerow({"player_name":"sunny","player_age":10})
#     writer.writerow({"player_name":"noni","player_age":10})
#     writer.writerow({"player_name":"minnie","player_age":10})

# ab read kar raha hu (dictreader se)
# with open(FILE_PATH,"r") as file:
#     read_file = csv.DictReader(file)
#     for row in read_file:
#         if row["player_age"] == 10:
#             print(row)

# simple read
# with open(FILE_PATH,"r") as file:
#     csv_file = csv.reader(file)
#     for row in csv_file:
#         print(row)