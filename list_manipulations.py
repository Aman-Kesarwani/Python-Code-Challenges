class ListManipulation:

    def __init__(self, ):
        self.myList =[]

    def addElement(self, element):
        self.myList.append(element)

    def addElementsOfAnotherList(self, anotherList):
        self.myList.extend(anotherList)

    def removeElementByValue(self, value):
        self.myList.remove(value)

    def deleteElementByIndex(self, index):
        del self.myList[index]

    def clearList(self):
        self.myList.clear()

    def getLengthOfList(self):
        return len(self.myList)
    
    def printList(self):
        print(self.myList)
    
newList = ListManipulation()

newList.addElement(4)
newList.addElement(5)
newList.addElement(10)
newList.addElement(15)

newList.printList()

newList.addElementsOfAnotherList([000, 90, 100, 110])
newList.printList()

newList.removeElementByValue(110)
newList.printList()

newList.deleteElementByIndex(0)
newList.printList()

print(newList.getLengthOfList())

newList.clearList()
newList.printList()