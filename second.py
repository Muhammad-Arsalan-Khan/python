# # # # # i = 1
# # # # # while i <= 100:
# # # # #     print(i)
# # # # #     i += 1

# # # # # i = 100
# # # # # while i >= 1:
# # # # #     print(i)
# # # # #     i -= 1


# # # # # i = 1
# # # # # while i <= 10:
# # # # #     print("3",i, 3*i)
# # # # #     i += 1

# # # # # idx = 0
# # # # # list = [1,34, 56,78, 90, 70, 77]
# # # # # while idx <= (len(list) - 1):
# # # # #     print(list[idx])
# # # # #     idx+=1

# # # # # # print(i)
# # # # # idxx = 0
# # # # # x = int(input("enter the number"))
# # # # # tupp = (1,3,5,7,8,9,44,66)
# # # # # while idxx < len(tupp):
# # # # #     if x == tupp[idxx]:
# # # # #         print(f"found the X{x}: is idx {idxx}")
# # # # #     idxx +=1


# # # # # idxxx = 0
# # # # # xy = int(input("enter the number"))
# # # # # tupp = (1,3,5,7,8,9,44,66)
# # # # # while idxxx < len(tupp):
# # # # #     if xy == tupp[idxxx]:
# # # # #         print(f"found the X{xy}: is idx {idxxx}")
# # # # #     else:
# # # # #         print("finding...")
# # # # #     idxxx +=1

# # # # # # breake

# # # # # index = 0
# # # # # xyz = int(input("enter the number"))
# # # # # tupl = (1,3,5,7,8,9,44,66)
# # # # # while index < len(tupl):
# # # # #     if xyz == tupl[index]:
# # # # #         print(f"found the X{xyz}: is idx {index}")
# # # # #         break
# # # # #     else:
# # # # #         print("finding...")
# # # # #     index +=1

# # # # h = 1
# # # # while h <= 10:
# # # #     if(h == 4):
# # # #         h+=1
# # # #         continue
# # # #     print(h)
# # # #     h+=1
# # # # print("-------------------")
# # # # list2 = [1,2,3,55,77,88,99]

# # # # for i in list2:
# # # #     print(i)

# # # # print("-------------------")

# # # # for i in range(1, 6):
# # # #     print(i)

# # # # print("-------------------")

# # # # for i in range(1, 4):
# # # #     print(i)
# # # # else:
# # # #     print("Loop complete ho gaya")

# # # # print("-------------------")

# # # # for i in range(1, 6):
# # # #     if i == 3:
# # # #         break
# # # #     print(i)
# # # # else:
# # # #     print("Loop complete ho gaya")

# # # # print("-------------------")

# # # # numbers = [1, 3, 5, 7]

# # # # for n in numbers:
# # # #     if n == 4:
# # # #         print("Number mil gaya")
# # # #         break
# # # # else:
# # # #     print("Number nahi mila")


# # # # j = 0
# # # # f = int(input("enter the number"))
# # # # t = (1,3,5,7,8,9,44,66)
# # # # for i in t:
# # # #     if f == t[j]:
# # # #         print(f"found the X{f}: is idx {j}")
# # # #         break
# # # #     else:
# # # #         print("finding...")
# # # #     j +=1
# # # # else:
# # # #     print("kuch ni mila")

# # # # seq = range(1,5)
# # # # for i in seq:
# # # #     print(i)

# # # # for i in range(1,10):
# # # #     print(i)

# # # # for i in range(10):
# # # #     print(i)

# # # for i in range(2,22,2):
# # #     print(i)

# # # n = int(input("enter the number"))
 
# # # for i in range(1, 11):
# # #     print(n, i , n*i)

# # # for i in range(20):
# # #     pass
# # # print("pass pass ho gaya")

# # n = int(input("enter the number"))
# # sum = 0
# # count = 1
# # while count <= n: 
# #     sum += count
# #     count+=1

# # print(sum)

# # # factorial
# # nn = int(input("enter the number"))
# # mul = 1
# # count = 1
# # while count <= nn: 
# #     mul *= count
# #     count+=1

# # print(mul)

# # nnn = int(input("enter the number"))
# # fact = 1
# # for i in range(1, nnn+1):
# #     fact *= i

# # print(fact)

# def sum(a, b):
#     return a + b

# sum_value1 = sum(3,45)
# sum_value2 = sum(2,10)
# sum_value3 = sum(7789,41)
# print(sum_value1, sum_value2, sum_value3)

# def sum2(a = 1, b =1):
#     return a + b

# print(sum2(3,5))
# print(sum2())

list1 = ["arsalan", "mazhar", "usman", "asim"]
list2 = ["phy", "chemistry", "math", "bio", "urdu","computer science"]

def length_of_list(list):
    print(len(list))

length_of_list(list1)
length_of_list(list2)

def fnx_for_wrt_in_single_line(list):
    for i in list:
        print(i, end=" ")

fnx_for_wrt_in_single_line(list1)

def find_the_fact(num):
    fact = 1
    for i in range(1, num+1):
        fact*=i
    return fact

        
print(find_the_fact(5))


def convert_usd_to_pkr(usd):
    print(usd * 280.82)

convert_usd_to_pkr(12)