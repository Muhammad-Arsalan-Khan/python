# from datetime import datetime

# day = int(input("enter your birthday date only"))
# Month = int(input("enter your birthday Month only. like this january = 1 , feb = 3 , march = 3" ))
# year = int(input("enter your birthday year only"))

# now = datetime.now()
# current_day = now.day
# current_month = now.month
# current_year = now.year

# if(current_month >= Month):
#     if(current_day >= day):
#         print("your age is", current_year - year , "year", (current_month - Month) - 1 , "Months", current_day , "days older" )
#     else:
#          print("your age is", current_year - year , "year", (current_month - Month) - 1 , "Months", current_day , "days older" )
# else:
#     print("your age is", current_year - year , "years", current_month , "Months", current_day , "days older" )


# from datetime import datetime

# def calculate_age(birth_day, birth_month, birth_year):
#     today = datetime.now()

#     # Birth date object
#     birth_date = datetime(birth_year, birth_month, birth_day)

#     # Calculate difference in years, months, days
#     years = today.year - birth_date.year
#     months = today.month - birth_date.month
#     days = today.day - birth_date.day

#     # Adjust if day or month difference is negative
#     if days < 0:
#         months -= 1
#         # Get number of days in previous month
#         previous_month = (today.month - 1) if today.month > 1 else 12
#         if previous_month in [1,3,5,7,8,10,12]:
#             days += 31
#         elif previous_month in [4,6,9,11]:
#             days += 30
#         else:  # February
#             # Check leap year
#             if (today.year % 4 == 0 and today.year % 100 != 0) or (today.year % 400 == 0):
#                 days += 29
#             else:
#                 days += 28

#     if months < 0:
#         years -= 1
#         months += 12

#     return years, months, days

# # Example input
# day = int(input("Enter birth day (e.g., 12): "))
# month = int(input("Enter birth month (e.g., 5): "))
# year = int(input("Enter birth year (e.g., 1998): "))

# y, m, d = calculate_age(day, month, year)
# print(f"You are {y} years, {m} months, and {d} days old.")


# str = "as salamu alaykum mera nam muhammad arsalan khan hain"
# print(len(str))
# print(str[2:6])
# print(str[:6])
# print(str[2:])
# print(str[-9:-5])
# print(str.endswith("in"))
# print(str.capitalize())
# print(str.replace("a", "b"))
# print(str.find("a"))
# print(str.count("a"))

# user_data = input("enter your name")
# print("you name is", user_data, "and your name length is", len(user_data))

# check_number = int(input("enter the number"))
# if(check_number % 2 == 0):
#     print(f"{check_number} is even")
# else:
#     print(f"{check_number} is odd")


# multi_7 = int(input("enter the number"))
# if(multi_7 % 7 == 0):
#     print(f"{multi_7} is multiple of 7")
# else:
#     print(f"{multi_7} is not multiple of 7")

# a = int(input("enter the first number"))
# b = int(input("enter the second number"))
# c = int(input("enter the third number"))
# d = int(input("enter the fourth number"))

# if ( a > b and a > c and a > d):
#     print("a is greater")
# elif(b> c and b > d):
#     print("b is greater")
# elif(c> d):
#     print("c is greater")
# else:
#     print("d is greater")


# list is mutable/ changable

list = ["arsalan", 21, "bbsul", "dj sindh"]
print(list)

new_list = [4,3,2,1]
# list.append(5)
# new_list.sort()
# new_list.sort(reverse=True)
# new_list.reverse()
# new_list.insert(5, 5)
# new_list.remove(4)
# new_list.pop(1)
print(new_list)

# tuple is immutiable
tup = (1,2,3,4,5)
print(tup)
tup_new = (1,)
print(type(tup_new))
similar_to_tup = (1) # ans int hoga Q ky python main sigle tuple ho , se likhte hain 
print(type(similar_to_tup))

# cout = 0
# movieList = []
# while cout < 3 :
#     movieList.append(input(f"enter your {cout+1} fav movie"))
#     cout += 1
# print(movieList)

# list = ["m", "a", "d", "a", "m"]
# listCopy = list.copy()
# list.reverse()
# if(list == listCopy):
#     print("list is palindrome")
# else:
#     print("not palindrome")

# print(list, listCopy)

#dictionary ya changeable hain
dic = {
    "name" : "arsalan",
    "age": 21,
    "subject":{
        "chemistry": 66,
        "phy": 88
    }
}

# print(dic)
# print(dic["name"])
# # print(dic["name2"]) #  ya error dega 
# print(dic.get("name2")) # ya eerror ni dega agar kuch ni hoga tu none dega
# print(dic.keys())
# print(dic.values())
# print(dic.update({"city": "karachi"}))
# dic["name"] = "m arsalan"
# print(dic)

# marks = {}
# x = input("enter the phy marks")
# marks.update({"phy": x})
# x = input("enter the chem marks")
# marks.update({"chem": x})
# x = input("enter the math marks")
# marks.update({"math": x})
# print(marks)


# set immmutable
sett = {1, 2, 3, "arsalan", "khan", "bbsul"}
print(sett)
collection = set() # empty set
print(collection)

set1 = {1,2,3}
set2 = {2,3,4}
set3 = {1,2,3,21,"bbsul","smit", "zaib"}
set3.add("Dj sindh")
set3.add(("hello i am tup"))
#set3.add(["hello i am tup"]) ##ya error de ga Q ky list add ni hoti set hain Q ky changable hain or koi b chez jo change ho wo sret main add ele ky tour pr nihogi pr set khud changeable hain 
set3.remove(2)
# set3.clear()
print(set3.pop())
print(set3)
print(len(set3))
print(set1.union(set2))
print(set1.intersection(set2))

language = {"python", "java", "c", "javascript", "python", "c", "javascript"}
print(len(language)) # ya double value ko ignore karta hain 

# python main 9 or 9.0 same hota hain is leaya hum set main dono ak sarh nni rakkh sakty ya tu tup main dena hoga ya data type change karni hogi
set4 = {9, 9.0, 8, 8.0}
print(set4)
set5 = {9, "9.0", "8", 8.0}
print(set5)
set6 = {("int", 9), ("float", 9.0)}
print(set6)