import copy

class ListElement():
    def __init__(self, *args):
       self.object = args[0]
       self.next = None
    
    def __str__(self):
        return str(self.object)


class List():
    def __init__(self) -> None:
       self.first = None

    def addElement(self, value):
        element = ListElement(value)
        if(self.first == None):
            self.first = element
        else:
            iterator = self.getLastElement()
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

    def extend(self, *args):
        for el in args:
            self.addElement(el)
    
    def pop(self):
        iterator = self.first
        while(iterator.next.next != None):
            iterator = iterator.next
        iterator.next = None
        return True

    def clear(self):
        self.first.next = None
        self.first = None

    def getSmallest(self):
        iterator = self.first
        smallest = self.first
        while(iterator != None):
            if(iterator.object < smallest.object):
                smallest = iterator
            iterator = iterator.next
        return smallest

    def sort(self):
        sorted_list = List()
        for i in range(self.getLength()):
            ele = self.getSmallest()
            sorted_list.addElement(ele)
            self.deleteElement(ele.object)
        return sorted_list
            
    def deleteElement(self, element):
        if(element == self.first.object):
            self.first = self.first.next
            return
        iterator = self.first
        prev = self.first
        while(iterator.object != element):#
            print(iterator)
            prev = iterator
            iterator = iterator.next
        prev.next = iterator.next

    def findObj(self, element):
        iterator = self.first
        if(self.first == None): return
        while(iterator.object != element):
            if(iterator.next != None):
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

    def getLastElement(self):
        iterator = self.first
        if(self.first == None): return
        while(iterator.next != None):
            iterator = iterator.next
        return iterator
    
    def reverseList(self):
        if(self.first == None): return
        list1 = copy.deepcopy(self)
        list2 = List()
        while(list1.getLength() > 1):
            lastE = list1.getLastElement()
            list2.addElement(lastE)
            list1.pop()
        list2.addElement(list1.first)
        return list2

    def getIndexFromElement(self, element):
        iterator = self.first
        if(self.first == None): return
        counter = 0
        while(iterator.object != element):
            if(iterator != None):
                iterator = iterator.next
                counter +=1
            else:
                return None
        return counter
    
    def getElementFromIndex(self, index):
        iterator = self.first
        if(self.first == None): return
        if(index > self.getLength()):
            raise IndexError("Index out of Bounce")
        counter = 0
        while(counter < index):
            iterator = iterator.next
            counter += 1
        return iterator


def main():
    list = List()
    list.addElement(2)
    list.addElement(1)
    list.addElement(4)
    list.addElement(3)

    print("Ausgabe:", list.printList())
    print("Counter", list.getLength())
    #print("Pop", list.pop())
    print("Ausgabe:", list.printList())
    print("FindObj:", list.findObj(2))

    print("IndexFromElement", list.getIndexFromElement(3))
    print("LastElement:", list.getLastElement())

    list2 = list.reverseList()
    print("Ausgabe:", list2.printList())
    #list.clear()

    print("Ausgabe:", list.printList())
    print("ElementFromIndex:", list.getElementFromIndex(0))

    list.extend(5, 6, 7)
    print("Ausgabe:", list.printList())
    # print("DeleteElemntByIndex:", list.deleteElementByIndex(1))

    list3 = list.sort()
    print("Ausgabe: NEU", list3.printList())


if __name__ == "__main__":
    main()
