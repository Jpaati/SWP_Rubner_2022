
class ArrayList():
    def __init__(self):
       self.listd = []

    def append(self, value):
        self.listd.append(value)
    
    def getFirstElement(self):
        return self.listd[0]
    
    def getLength(self):
        return len(self.listd)

    def extend(self, *args):
        self.listd.extend(args)
    
    def pop(self):
        self.listd.pop()

    def clear(self):
        self.listd.clear()

    def getSmallest(self):
        self.listd.sort()
        return self.listd[0]

    def sort(self):
        self.listd.sort()
            
    def deleteElement(self, element):
        self.listd.remove(element)
    
    def printList(self):
       return self.listd

    def getLastElement(self):
        return self.listd[len(self.listd)]
    
    def reverseList(self):
        return self.listd.reverse()

    def getIndex(self, element):
        self.listd.index(element)
    

def main():
    listD = ArrayList()
    for i in range(0,5):
        listD.append(5-i)

    print("Ausgabe:", listD.printList())
    print("Counter", listD.getLength())
    
    # Das letzte Element löschen
    listD.pop()
    # Das Element 2 löschen
    listD.deleteElement(5)
    print("Ausgabe:", listD.printList())
    print("Smallest:", listD.getSmallest())
    


if __name__ == "__main__":
    main()
