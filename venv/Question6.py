def f(x, l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)

f(2)
f(3, [3,2,1])
f(3)

#Explanation: Mutable types shouldn’t be used as default arguments.
#https://www.codementor.io/sheena/advanced-use-python-decorators-class-function-du107nxsv