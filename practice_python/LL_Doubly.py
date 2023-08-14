class Node:
    def __init__(self, dataVal=None):
        self.dataVal = dataVal
        self.prev = None
        self.next = None

class LL_Doubly:
    def __init__(self):
        self.headVal = None
        self.endVal = None

    def showhead(self):
        printVal = self.headVal
        while printVal is not None:
            print(printVal.dataVal)
            printVal = printVal.next

    def showEnd(self):
        printVal = self.endVal
        while printVal is not None:
            print(printVal.dataVal)
            printVal = printVal.prev

lld = LL_Doubly()
n1 = lld.headVal = Node("Mon")
n2 = n1.next = Node("Tue")
n3 = n2.next = Node("Wed")
n4 = n3.next = Node("Thu")
n5 = n4.next = Node("Fri")
n6 = n5.next = Node("Sat")
n7 = n6.next = Node("Sun")

n2.prev = n1
n3.prev = n2
n4.prev = n3
n5.prev = n4
n6.prev = n5
n7.prev = n6
lld.endVal = n7

print("\n Show data using head: \n")
lld.showhead()
print("\n Show data using end: \n")
lld.showEnd()