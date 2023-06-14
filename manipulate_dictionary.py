class DictionaryOperation:
    def __init__(self):
        self.dict = {}

    def insertElemenst(self, key, value):
        if key in self.dict.keys():
            pass
        else:
            self.dict[key] = value

    def addElementFromAnotherDict(self, anotherDict):
        self.dict.update(anotherDict)

    def updateElement(self, index, element):
        self.dict[index] = element

    def clearDictionary(self):
        self.dict.clear()

    def printElements(self):
        if len(self.dict)==0:
            print("Its empty bro !")
        for key, value in self.dict.items():
            print("Key: ", key, ",Value: ", value)

d1 = DictionaryOperation()
d1.insertElemenst(1, "Aman")
d1.insertElemenst(2, "Nikita")
d1.insertElemenst(3, "Chicks")
d1.insertElemenst(4, "Chikki")

#d1.printElements()
d1.updateElement(1, "AmanChick")
d1.printElements()

newDictionary = {9: "Nikhil", 10: "Nidhi"}
d1.addElementFromAnotherDict(newDictionary)

d1.printElements()

d1.clearDictionary()
d1.printElements()