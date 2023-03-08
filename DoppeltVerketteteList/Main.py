
class ListElement():
    def __init__(self, *args):
       self.object = args[0]
       self.next = None
       self.prev = None
    
    def __str__(self):
        return str(self.object)


class Double_List():
    def __init__(self) -> None:
       self.first = None
       self.tail = None

    def append(self, value):
        element = ListElement(value)
        if(self.first == None):
            self.first = element
            self.tail = element
        else:
            last = self.tail
            last.next = element
            element.prev = last
            self.tail = element
    
    def getFirstElement(self):
        return self.first
    
    def getLength(self):
        counter = 0
        iterator = self.first
        while(iterator != self.tail):
            counter +=1
            iterator = iterator.next
        return counter + 1

    def extend(self, *args):
        for el in args:
            self.append(el)
    
    def pop(self):
        last = self.tail
        prelast = last.prev
        prelast.next = None
        self.tail = prelast
        return True

    def clear(self):
        self.first.next = None
        self.tail = None
        self.first = None

    def getSmallest(self):
        iterator = self.first
        smallest = self.first
        while(iterator != self.tail):
            if(iterator.object < smallest.object):
                smallest = iterator
            iterator = iterator.next
        return smallest

    def sort(self):
        pass
            
    def deleteElement(self, element):
        if(element == self.first.object):
            self.first = self.first.next
            return
        iterator = self.first
        while(iterator.object != element):
            iterator = iterator.next
        iterator.prev.next = iterator.next

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
        return self.tail
    
    def reverseList(self):
        if(self.first == None): return
        list2 = Double_List()
        iterator = self.tail
        while(list2.getLength() < self.getLength()):
            list2.append(iterator)
            iterator = iterator.prev
        return list2

    def getIndex(self, element):
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
    
    def getElement(self, index):
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
    list = Double_List()
    list.append(2)
    list.append(1)
    list.append(4)
    list.append(3)

    print("Ausgabe:", list.printList())
    print("Counter", list.getLength())
    print("Pop", list.pop())
    print("Ausgabe:", list.printList())
    print("FindObj:", list.findObj(3))


if __name__ == "__main__":
    main()
