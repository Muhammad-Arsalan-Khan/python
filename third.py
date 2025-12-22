f = open("smaple.txt", "r")
data = f.read()
print(data)
f.close()

f1 = open("smaple.txt", "r")
data1 = f1.readline()
print(data1)

data2 = f1.readline()
print(data2)
f1.close()

f = open("smaple.txt", "r")
data = f.read(5)
print(data)
f.close()

# proper sytax
with open("smaple.txt", "r") as f:
    data = f.read()
    print(data, "\n using proper syntax")


# import os
# os.remove("deletekarniwalifilekanam.txt") # deletes the file permanently


with open("newfile.txt", "w") as f:
    f.write("hi everyone \ni am learning python \nthis is a new file created using java\nhave a nice day!")

with open("newfile.txt", "r") as f:
    data = f.read()
    new_data = data.replace("java", "python")
    print(new_data)
with open("newfile.txt", "w") as f:
    f.write(new_data)

with open("newfile.txt", "r") as f:
    data = f.read()
    result = data.find("learning")
    print("the index of learning is:", result)

def check_word_in_which_line(word, filename):
    with open(filename, "r") as f:
        lines = f.readlines()
        for index, line in enumerate(lines):
            if word in line:
                print(f"The word '{word}' is found in line {index + 1}: {line.strip()}")

check_word_in_which_line("python", "newfile.txt")

with open("numberfile.txt", "w") as f:
    f.write("1,2,3,4,5,6,7,8,9,10")

with open("numberfile.txt", "r") as f:
    data = f.read()
    numbers = data.split(",")
    total = 0
    even = 0
    odd = 0
    evennumber = 0
    oddnumber = 0
    for num in numbers:
        total += int(num)
        if int(num) % 2 == 0:
            even += int(num)
            evennumber += 1
        else:
            odd += int(num) 
            oddnumber += 1
    print("The sum of even numbers is:", even, "total even numbers are:", evennumber)
    print("The sum of odd numbers is:", odd, "total odd numbers are:", oddnumber)
    print("The sum of numbers in the file is:", total)

