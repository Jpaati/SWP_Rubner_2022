import copy

arr = [1, 5, 3, 4]
arr2 = []
smallest = 100

for i in range(len(arr)):
    for ele in arr:
        if(ele < smallest):
            smallest = ele
    print(smallest)
    arr.remove(smallest)
    arr2.append(smallest)

print(arr2)


arr2 = copy.deepcopy(arr)

print(id(arr), id(arr2))

zahl1 = 8
zahl = 8

breakpoint()

print(id(zahl1) == id(zahl))


arr2 = map(lambda x: x+1, arr)
print(list(arr2))

dic = {"Hallo": 1, "Stop": 1}



arr.sort()

class Person():
    hall = ""
    def __init__(self, name, age):
        self.name = name,
        self.age = age

class Mitarbeiter(Person):
    def __init__(self, name, age, id):
        pass