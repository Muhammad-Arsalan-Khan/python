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

class deleteExample:
    def __init__(self, name):
        self.name = name
        print(f"object {self.name} created")

    def __del__(self):
        del self.name
        # print(f"object {self.name} is being deleted")


# obj1 = deleteExample("obj1")
# print("before delete",obj1.name)
# obj1.__del__()
# print("after delete",obj1.name)


class simple_delete:
    def __init__(self, name):
        self.name = name
        print(f"object {self.name} created")

obj = simple_delete("simple_obj")
print("before delete",obj.name)
del obj 
# print("after delete",obj.name)


# private 
class bankAccount:
    def __init__(self, accountNumber, balance):
        self.__account_number = accountNumber
        self.__balance = balance
        print("bank account created")

    def __privateMethod(self):
        return f"Account Number: {self.__account_number}"

    def deposit(self, amount):
        self.__balance += amount
        print(f"{self.__privateMethod()} deposited {amount}. new balance is {self.__balance}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("insufficient balance")
        else:
            self.__balance -= amount
            print(f"{self.__privateMethod()} withdrawn {amount}. new balance is {self.__balance}")

    def get_balance(self):
        print(f"{self.__privateMethod()} your current balance is {self.__balance}")


acc = bankAccount("1181911214", 5000)
acc.deposit(2000)
acc.withdraw(1000)
acc.get_balance()
# print(acc.__balance) # in ko hum class ky bahir access nahi kar sakty err aye ga  q ky ye private hai
# print(acc.__privateMethod()) # in ko hum class ky bahir access nahi kar sakty err aye ga  q ky ye private hai

# inheritance example sigle level inheritance
class parent:
    @staticmethod
    def show():
        print("i am parent class method called")
    
class child(parent):
    def display(self):
        print("child class method called")

c = child()
c.display()
c.show()

print("-----")
# multilevel inheritance  
class grandparent:
    @staticmethod
    def greet():
        print("hello from grandparent class")

class parent(grandparent):
    @staticmethod
    def show():
        print("i am parent class method called")

class child(parent):
    def display(self):
        print("child class method called")

c = child()
c.display()
c.show()
c.greet()
    
print("-----")
# multiple inheritance
class A:
    def method_a(self):
        print("method from class A")

class B:
    def method_b(self):
        print("method from class B")

class C(A, B):
    def method_c(self):
        print("method from class C")

obj = C()
obj.method_a() 
obj.method_b()
obj.method_c()


print("-----")


class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        super().sound()
        print("Dog barks")

dog = Dog("Buddy", "Golden Retriever")
print(f"Dog Name: {dog.name}, Breed: {dog.breed}")
dog.sound()

print("-----")
# example of employee management system using inheritance
class employee:
    def __init__(self, name , salary):
        self.name = name 
        self.salary = salary
        print("adding a new employee ....")

    def show_details(self):
        print(f"employee name is {self.name} and salary is {self.salary}")


class manager(employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def show_details(self):
        super().show_details()
        print(f"manager department is {self.department}")

class developer(employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def show_details(self):
        super().show_details()
        print(f"developer programming language is {self.programming_language}")

m1 = manager("Alice", 90000, "Sales")
m1.show_details()   
d1 = developer("Bob", 80000, "Python")
d1.show_details()   


# jb mujha class ky andar kisi attribute ki value change karni ho tu classmethod ka use kartay hain
class Temperature:
    unit = "Celsius"
    print(f"Temperature unit {unit}")

    def check_unit(self):
        print(f"Current temperature unit is {self.unit}")

    @classmethod
    def change_unit(cls, new_unit):
        cls.unit = new_unit
        print(f"Temperature unit changed to {cls.unit}")

Temperature.check_unit(Temperature)
Temperature.change_unit("Fahrenheit") 
Temperature.check_unit(Temperature)   

print("--------")
# or tareeqay jis se class ky attribute ko change kar sakty hain without classmethod
class Temperature2:
    unit = "Celsius"
    print(f"Temperature2 unit {unit}")

    def check_unit(self):
        print(f"Current temperature2 unit is {self.unit}")

    def change_unit(self, new_unit):
        Temperature2.unit = new_unit
        print(f"Temperature2 unit changed to {Temperature2.unit}")

    def change_unit2(self, new_unit):
        self.__class__.unit = new_unit
        print(f"Temperature2 unit changed to {Temperature2.unit}")


temp2 = Temperature2()
temp2.change_unit("FAHRENHEIT")
print(Temperature2.unit) 
temp2.change_unit2("KELVIN")
print(Temperature2.unit)

# @ property decorator
print("--------")
class student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
    @property
    def percentage(self):
        # total = self.phy + self.chem + self.math
        # percent = (total / 300) * 100
        # return percent
        return (self.phy + self.chem + self.math) / 300 * 100
    
s1 = student(90, 80, 70)
print("student percentage is:", s1.percentage)
s1.phy = 95
print("after updating physics marks, student percentage is:", s1.percentage)


print("--------")
# getter setter deleter example
class employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        if new_salary < 0:
            print("Salary cannot be negative.")
        else:
            self._salary = new_salary

    @salary.deleter
    def salary(self):
        del self._salary
        print("Salary attribute deleted.")      

emp = employee("John", 50000)
print("Initial Salary:", emp.salary)    # getter
emp.salary = 60000                      # setter
print("Updated Salary:", emp.salary)
emp.salary = -1000
# del emp.salary                       # deleter
print("--------")


# polymorphism example
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

a1 = Dog()
a2 = Cat()

a1.sound()
a2.sound()

print("--------")
# operator overloading example
class complex:
    def __init__(self, real, image):
        self.real = real
        self.image = image

    def add1(self, other):
            real = self.real + other.real
            image = self.image + other.image
            return complex(real, image)
    
    # operator overloading dunder method
    def __add__(self, other):
        real = self.real + other.real
        image = self.image + other.image
        return complex(real, image)  
    
    def __sub__(self, other):
        real = self.real - other.real
        image = self.image - other.image
        return complex(real, image)  

    def shownumber(self):
        print(f"{self.real}i + {self.image}j")


num1 = complex(7, 6)
num2 = complex(3, 4)
result = num1.add1(num2)
print(f"Addition using method: {result.real}i + {result.image}j")

num3 = num1 + num2  
num3.shownumber()
num3 = num1 - num2 
num3.shownumber()

print("--------")

class circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
    
    def parameter(self):
        return 2 * 3.14 * self.radius
    
c1 = circle(5)
print("Area of circle:", c1.area()) 
print("Parameter of circle:", c1.parameter())


class employee:
    def __init__(self, name , salaray):
        self.name = name 
        self.salary = salaray
        print("adding a new employee ....") 
    def show_details(self):
        print(f"employee name is {self.name} and salary is {self.salary}")

e1 = employee("arsalan", 90000)
e1.show_details()

class engineer(employee):
    def __init__(self , depart , age):
        super().__init__("arsalan", 80000)
        self.depart = depart
        self.age = age

    def show_engineer_details(self):
        print(f"engineer department is {self.depart} and age is {self.age}")

eng1 = engineer("software", 25)
eng1.show_details() 
eng1.show_engineer_details()

print("--------")

# abstraction example
class order:
    def __init__(self, item , price):
        self.item = item
        self.price = price

    def __gt__(self, other):
        return self.price > other.price


order1 = order("laptop", 100000)
order2 = order("phone", 50000)

print(order1 < order2)
print(order1 > order2)