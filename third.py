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