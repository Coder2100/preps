#Question: Write code to get the current file directory.
import os

print(os.__file__)

def mul3(num):
    return num*3
num=[1,2,3,4,5]
res=map(mul3,num)
print(list(res))

lis=[10,23,24,25]
rest=list(filter(lambda x: x%2==0,lis))
print(rest)


print("hello", end='')
print("world")#end value is \n y default
print("go for", end="-")
print("it")

lis = [1,2,3,4]
print("The HELP RESULTS")
help(list)

str ="hello world i am here to stay"

print(str.split())
print(str.split('e'))
user = "zukile MTOTSO"
print(user.title())


from random import randint
print("Random Number between 1 and 10: ", end='')
print(+randint(1,10))
print("Recursion syntax")

def fac(n):
    if n ==1:
        return 1 #
    else:
        return n * fac(n-1)
    print(fac(0))

mylist = [1,2,3, "hello", "world"]
print(mylist[-1])
#Floor division
print(6//9)
print(6/9)
#What are the Generators in python?
def rev():
    i = 4
    while i > 0:
        i = 1-1
        for i in rev():
            print(i)

# decorator
my_fun = my_dec(my_fun)
@my_dec