print("\n [random.random() for i in range(100000)]. How would you prove that your answer is correct?")


def f1(lIn):
    l1 = sorted(lIn)
    l2 = [i for i in l1 if i<0.5]
    return [i*i for i in l2]

def f2(lIn):
    l1 = [i for i in lIn if i<0.5]
    l2 = sorted(l1)
    return [i*i for i in l2]

def f3(lIn):
    l1 = [i*i for i in lIn]
    l2 = sorted(l1)
    return [i for i in l1 if i<(0.5*0.5)]



print("\nMost to least efficient: f2, f1, f3. To prove that this is the case, you would want to profile your code. \nPython has a lovely profiling package that should do the trick.")
import random
import cProfile

#lIn = [random.random() for i in range(100000)]
lIn = [random.random() for i in range(100000)]
cProfile.run('f1(lIn)')
cProfile.run('f2(lIn)')
cProfile.run('f3(lIn)')

""" Locating and avoiding bottlenecks is often pretty worthwhile.
 A lot of coding for efficiency comes down to common sense - 
in the example above it's obviously quicker to sort a list if it's a smaller list, 
so if you have the choice of filtering before a sort it's often a good idea. 
The less obvious stuff can still be located through use of the proper tools.
It's good to know about these tools."""

#https://www.codementor.io/sheena/essential-python-interview-questions-du107ozr6
#http://techgeekbuzz.com/python-interview-questions/
