
class ListElement():
    def __init__(self, *args):
       self.object = args[0]
       self.next = None
    
    def __str__(self):
        return str(self.object)


class List():
    def __init__(self) -> None:
       self.first = None

    def addElement(self, element):
        if(self.first == None):
            self.first = element
        else:
            iterator = self.first
            while(iterator.next != None):
                iterator = iterator.next
            iterator.next = element
    
    def getFirstElement(self):
        return self.first
    
    def getLength(self):
        counter = 0
        iterator = self.first
        while(iterator.next != None):
            counter +=1
            iterator = iterator.next
        return counter + 1
    
    def pop(self):
        iterator = self.first
        while(iterator.next.next != None):
            iterator = iterator.next
        iterator.next = None
        return True
        

    def deleteElement(self, element):
        #does not work up to now
        iterator = self.first
        while(iterator.next != None):
            if(iterator.next == element):
                iterator.next == element.next
            iterator = iterator.next
        return True

    def findObj(self, element):
        iterator = self.first
        while(iterator != element):
            if(iterator != None):
                iterator = iterator.next
            else:
                return None
        return iterator
    
    def printList(self):
        iterator = self.first
        out = "["
        while iterator != None:
            out += iterator.__str__() + " "
            iterator = iterator.next
        out += "]"
        return out
    
    def reverseList(self):
        pass

    def index(self, element):
        iterator = self.first
        counter = 0
        while(iterator != element):
            if(iterator != None):
                iterator = iterator.next
                counter +=1
            else:
                return None
        return counter


def main():
    list = List()
    ele1 = ListElement("E1")
    ele2 = ListElement("E2")
    ele3 = ListElement("E3")
    list.addElement(ele2)
    list.addElement(ele1)
    list.addElement(ele3)
    print("Ausgabe:", list.printList())
    print("Counter", list.getLength())
    print("Pop", list.pop())
    print("Ausgabe:", list.printList())
    print("FindObj:", list.findObj(ele3))
    print("Index", list.index(ele1))



if __name__ == "__main__":
    main()
