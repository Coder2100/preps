x = 35
y = 75
min = x if x < y else y

print(min)

def fun1(func2, arg):
    return func2(func2(arg))
def mul(n):
    return n * 2

print(fun1(mul,10))

print("5"*4)
a,b,*c = [1,2,3,4,5]

print(a)
print(b)
print(c)
lis = [[]]*3
lis[0].append(4)
print(lis)

import array as arr

my_array =arr.array('i', [1,2,3,4])
my_list = 1, 'abc', 12.3
print(my_array)
print(my_list)

class Employee:
   # def
    def __init__(self, name, age,salary):
        self.name = name
        self.age = age
        self.salary = 20000
E1 = Employee("ZUKILE", 23, 20000)
# E1 is the instance of class Employee.
#__init__ allocates memory for E1.
print(E1.name.title())
print(E1.age)
print("$", end='')
print(E1.salary)

print("Lambda function")
a = lambda x, y : x+y
print(a(5, 6))

def myLambda(x,y):
    return x+y
print(myLambda(5,5))


from random import shuffle
x = ['Keep', 'The', 'Blue', 'Flag', 'Flying', 'High']
shuffle(x)
print(x)
abcc = "ABC"
print(abcc.capitalize())
#https://www.edureka.co/blog/interview-questions/python-interview-questions/

#https://stackoverflow.com/jobs/96553/senior-frontend-engineer-nomanini?so=i&pg=1&offset=0