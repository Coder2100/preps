
print("\nBecause composition and object construction is what objects are all about.\nObjects are composed of stuff and they need to be initialised somehow.\nThis also ties up some stuff about recursion and use of generators.Generators are great.\nYou could have achieved similar functionality to print_all_2 by just constructing a big long list and then printing it's contents.\nOne of the nice things about generators is that they don't need to take up much space in memory.\nIt is also worth pointing out that print_all_1 traverses the tree in a depth-first manner, \nwhile print_all_2 is width-first.\n Make sure you understand those terms.\n Sometimes one kind of traversal is more appropriate than the other. \nBut that depends very much on your application.\n")
class Node(object):
    def __init__(self,sName):
        self._lChildren = []
        self.sName = sName
    def __repr__(self):
        return "<Node '{}'>".format(self.sName)
    def append(self,*args,**kwargs):
        self._lChildren.append(*args,**kwargs)
    def print_all_1(self):
        print(self)
        for oChild in self._lChildren:
            oChild.print_all_1()
    def print_all_2(self):
        def gen(o):
            lAll = [o,]
            while lAll:
                oNext = lAll.pop(0)
                lAll.extend(oNext._lChildren)
                yield oNext
        for oNode in gen(self):
            print(oNode)

oRoot = Node("root")
oChild1 = Node("child1")
oChild2 = Node("child2")
oChild3 = Node("child3")
oChild4 = Node("child4")
oChild5 = Node("child5")
oChild6 = Node("child6")
oChild7 = Node("child7")
oChild8 = Node("child8")
oChild9 = Node("child9")
oChild10 = Node("child10")

oRoot.append(oChild1)
oRoot.append(oChild2)
oRoot.append(oChild3)
oChild1.append(oChild4)
oChild1.append(oChild5)
oChild2.append(oChild6)
oChild4.append(oChild7)
oChild3.append(oChild8)
oChild3.append(oChild9)
oChild6.append(oChild10)

# specify output from here onwards

print("oRoot.print_all_1() prints:\n")
oRoot.print_all_1()
print("\noRoot.print_all_2() prints:\n")
oRoot.print_all_2()

#https://www.codementor.io/sheena/essential-python-interview-questions-du107ozr6