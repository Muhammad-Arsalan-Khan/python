class student:
    def __init__(self, name , marks):
        self.name = name
        self.totalmarks = marks
        print("adding a new student ....")

s1 = student("arsalan", 90)
print(s1, "Arsalan full obj")
print(s1.name, s1.totalmarks)

s2 = student("Asim", 98)
print(s2, "Asim full obj")
print(s2.name, s2.totalmarks)


class uni:
    university_name = "ABC University"
    name = "anonymous"
    def __init__(self, name , marks):
        self.name = name
        self.totalmarks = marks
        print("adding a new student ....")
    def show_details(self):
        print(f"student name is {self.name} and total marks are {self.totalmarks} from {self.university_name}")

s3 = uni("arsalan", 90)
s3.show_details()   

print(s3.university_name)
print(uni.university_name)


class student2:
    def __init__(self, name , mark1, mark2, mark3):
        self.name = name
        self.phy = mark1
        self.chem = mark2
        self.math = mark3
        print("adding a new student ....")

    def average(self):
        avg = (self.phy + self.chem + self.math) / 3
        print(f"the average marks of {self.name} is {avg}")
        return avg
    
s4 = student2("arsalan", 90, 80, 70)
s4.average()
s5 = student2("asim", 95, 85, 75)
s5.average()

class hello:
    @staticmethod
    def greet():
        print("hello everyone! welcome to the python programming world.")

hello.greet()

class account:
    balance = 0

    def __init__(self, bankAccountNumber):
        self.account_number = bankAccountNumber
        print(f"account created with account number {self.account_number}")

    def credit(self, amount):
        self.balance += amount
        print(f"deposited {amount}. new balance is {self.balance}") 

    def debit(self, amount):
        if amount > self.balance:
            print("insufficient balance")
        else:
            self.balance -= amount
            print(f"withdrawn {amount}. new balance is {self.balance}")

    def check_balance(self):
        print(f"your current balance is {self.balance}")

acc1 = account("1181911214")
acc1.credit(10000)
acc1.debit(5000)
acc1.check_balance()

print(acc1.account_number)

acc1.credit(4000)
acc1.debit(2456)