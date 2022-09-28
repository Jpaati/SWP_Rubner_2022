from random import randint

def get_random_six(startValue, endValue, rangeD):
    list_return = []
    for item in range(startValue, endValue+1):
        list_return.append(item)
        list_stat[item] = 0
    print(list_return) 
    print(list_stat)   
    
    for el in range(rangeD):
        lastPos = len(list_return)-1-el
        print(lastPos)
        ran = randint(startValue, endValue)
        print(ran)            #range immer -1 hinten
        list_return[ran], list_return[lastPos] = list_return[lastPos], list_return[ran] 
    print(list_return)
    return list_return[:-rangeD]

def get_statistic(list):
    for element in list:
        list_stat[element+startValueZ] = list_stat[element+startValueZ] +1


def print_list(list):
    counter = 0
    for element in list:
        print("Zahl" , counter, ":",element)
        counter = counter +1

endValueZ = 95
startValueZ = 50
rangeZ = 6

list_stat = {}

for index in range(0, 1001):
    rand = get_random_six(startValueZ, endValueZ, rangeZ)
    print(rand)
    get_statistic(rand)





