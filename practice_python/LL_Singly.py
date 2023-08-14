'''
class Node:
    def __init__(self, dataVal=None):
        self.dataVal = dataVal
        self.nextVal = None

class LLSingly:
    def __init__(self):
        self.headVal = None

    def display_LL_Singly(self):
        printVal = self.headVal
        while printVal is not None:
            print(printVal.dataVal)
            printVal = printVal.nextVal

list1 = LLSingly()
list1.headVal = Node("MON")

n2 = Node("TUE")
list1.headVal.nextVal = n2

n3 = Node("WED")
n2.nextVal = n3

n4 = Node("THU")
n3.nextVal = n4

print("\nTravering the linkled list \n ")
print(list1.display_LL_Singly())

'''

class Node:
    def __init__(self, dataVal=None):
        self.dataVal = dataVal
        self.nextVal = None

class LinkedList:
    def __init__(self):
        self.headVal = None

    def showData(self):
        printVal = self.headVal
        while printVal is not None:
            print(printVal.dataVal)
            printVal = printVal.nextVal

ll = LinkedList()

ll.headVal = Node("JAN")

n2 = Node("FEB")
ll.headVal.nextVal = n2

ll.showData()